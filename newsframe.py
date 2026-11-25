#!/usr/bin/env python3
"""Canvas, text and PNG output for the news image.  Standard library only.

Text is rendered from grayscale coverage glyphs (fontdata.py): each pixel
is blended fg*coverage + bg*(1-coverage), so edges are antialiased, never
1-bit thresholded.  PNG is encoded by hand (zlib + chunk CRCs) so the
program needs no third-party module at run time.
"""
import os
import struct
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fontdata

FONTS = fontdata.FONTS

W = 1024
H = 1024


class Canvas:
    def __init__(self, w=W, h=H, bg=(250, 247, 240)):
        self.w = w
        self.h = h
        self.px = bytearray(bg * (w * h))

    def _idx(self, x, y):
        return (y * self.w + x) * 3

    def set(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = self._idx(x, y)
            self.px[i] = color[0]
            self.px[i + 1] = color[1]
            self.px[i + 2] = color[2]

    def blend(self, x, y, color, cov):
        """Blend color over the pixel with coverage 0..255."""
        if cov <= 0 or not (0 <= x < self.w and 0 <= y < self.h):
            return
        if cov >= 255:
            self.set(x, y, color)
            return
        i = self._idx(x, y)
        a = cov
        inv = 255 - a
        self.px[i] = (color[0] * a + self.px[i] * inv) // 255
        self.px[i + 1] = (color[1] * a + self.px[i + 1] * inv) // 255
        self.px[i + 2] = (color[2] * a + self.px[i + 2] * inv) // 255

    def fill_rect(self, x, y, w, h, color):
        x0 = max(0, int(x))
        y0 = max(0, int(y))
        x1 = min(self.w, int(x + w))
        y1 = min(self.h, int(y + h))
        row = bytes(color) * (x1 - x0)
        for yy in range(y0, y1):
            i = self._idx(x0, yy)
            self.px[i:i + len(row)] = row

    def rect(self, x, y, w, h, color, t=1):
        self.fill_rect(x, y, w, t, color)
        self.fill_rect(x, y + h - t, w, t, color)
        self.fill_rect(x, y, t, h, color)
        self.fill_rect(x + w - t, y, t, h, color)

    def hline(self, x, y, w, color, t=1):
        self.fill_rect(x, y, w, t, color)

    def vline(self, x, y, h, color, t=1):
        self.fill_rect(x, y, t, h, color)

    def line(self, x0, y0, x1, y1, color, t=1):
        """Bresenham line with thickness t (odd)."""
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        half = t // 2
        while True:
            for a in range(-half, half + 1):
                for b in range(-half, half + 1):
                    self.set(x0 + a, y0 + b, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def circle(self, cx, cy, r, color, fill=True):
        r = int(r)
        for yy in range(cy - r, cy + r + 1):
            for xx in range(cx - r, cx + r + 1):
                d2 = (xx - cx) ** 2 + (yy - cy) ** 2
                if fill:
                    if d2 <= r * r:
                        self.set(xx, yy, color)
                else:
                    if r * r - r <= d2 <= r * r + r:
                        self.set(xx, yy, color)

    def poly(self, pts, color):
        """Scanline fill of a polygon given as [(x,y), ...]."""
        if len(pts) < 3:
            return
        ys = [p[1] for p in pts]
        for y in range(max(0, min(ys)), min(self.h, max(ys) + 1)):
            xs = []
            n = len(pts)
            for i in range(n):
                x0, y0 = pts[i]
                x1, y1 = pts[(i + 1) % n]
                if (y0 <= y < y1) or (y1 <= y < y0):
                    if y1 != y0:
                        xs.append(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
            xs.sort()
            for k in range(0, len(xs) - 1, 2):
                xa = max(0, int(xs[k]))
                xb = min(self.w, int(xs[k + 1]) + 1)
                for x in range(xa, xb):
                    self.set(x, y, color)

    def poly_line(self, pts, color, t=1):
        for i in range(len(pts) - 1):
            self.line(int(pts[i][0]), int(pts[i][1]),
                      int(pts[i + 1][0]), int(pts[i + 1][1]), color, t)

    # ---- text ----
    def text_width(self, font_key, text):
        f = FONTS[font_key]
        w = 0
        for ch in text:
            g = f["glyphs"].get(str(ord(ch)))
            if g is None:
                g = f["glyphs"].get("63")  # '?'
            w += g[0]
        return w

    def draw_text(self, x, baseline_y, font_key, text, color):
        """Draw text with its baseline at baseline_y. Returns width used."""
        import base64 as _b64
        f = FONTS[font_key]
        cx = int(x)
        for ch in text:
            g = f["glyphs"].get(str(ord(ch)))
            if g is None:
                g = f["glyphs"].get("63")
            adv, xoff, yoff, gw, gh, comp = g
            if gw and gh:
                raw = zlib.decompress(_b64.b64decode(comp))
                for yy in range(gh):
                    for xx in range(gw):
                        cov = raw[yy * gw + xx]
                        if cov:
                            self.blend(cx + xoff + xx, baseline_y + yoff + yy,
                                       color, cov)
            cx += adv
        return cx - int(x)

    def draw_text_right(self, x_right, baseline_y, font_key, text, color):
        w = self.text_width(font_key, text)
        return self.draw_text(x_right - w, baseline_y, font_key, text, color)

    def draw_text_center(self, cx, baseline_y, font_key, text, color):
        w = self.text_width(font_key, text)
        return self.draw_text(cx - w // 2, baseline_y, font_key, text, color)

    def wrap(self, font_key, text, max_w):
        """Greedy word wrap. Returns a list of lines."""
        words = text.split(" ")
        lines = []
        cur = ""
        for word in words:
            trial = (cur + " " + word).strip()
            if self.text_width(font_key, trial) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        return lines

    def draw_wrapped(self, x, y_top, font_key, text, max_w, line_h, color,
                     max_lines=None):
        """Draw wrapped text starting at y_top (top of first line).
        Returns the number of lines drawn."""
        lines = self.wrap(font_key, text, max_w)
        if max_lines is not None:
            lines = lines[:max_lines]
        f = FONTS[font_key]
        y = y_top + f["ascent"]
        for ln in lines:
            self.draw_text(x, y, font_key, ln, color)
            y += line_h
        return len(lines)

    # ---- PNG ----
    def to_png_bytes(self):
        raw = bytearray()
        stride = self.w * 3
        for y in range(self.h):
            raw.append(0)  # filter: none
            raw += self.px[y * stride:(y + 1) * stride]
        comp = zlib.compress(bytes(raw), 9)

        def chunk(typ, data):
            c = struct.pack(">I", len(data)) + typ + data
            c += struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)
            return c

        ihdr = struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0)
        return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) +
                chunk(b"IDAT", comp) + chunk(b"IEND", b""))

    def save(self, path):
        with open(path, "wb") as f:
            f.write(self.to_png_bytes())


# ---- simplified world map ----
# Coarse continent outlines in (lon, lat).  Drawn small; dots placed by
# the same equirectangular projection, so relative positions stay right.
CONTINENTS = [
    # North America
    [(-168, 65), (-155, 58), (-140, 60), (-130, 54), (-125, 48), (-120, 40),
     (-114, 32), (-105, 22), (-97, 16), (-92, 15), (-83, 9), (-79, 9),
     (-85, 15), (-90, 21), (-97, 26), (-93, 30), (-84, 30), (-80, 32),
     (-76, 35), (-75, 40), (-70, 42), (-68, 45), (-60, 47), (-55, 52),
     (-60, 55), (-65, 58), (-70, 58), (-75, 62), (-85, 66), (-95, 68),
     (-110, 68), (-125, 70), (-140, 70), (-155, 71), (-168, 66)],
    # Greenland
    [(-45, 60), (-40, 65), (-30, 68), (-22, 70), (-25, 76), (-35, 80),
     (-55, 76), (-58, 70), (-53, 64), (-45, 60)],
    # South America
    [(-79, 9), (-72, 12), (-64, 10), (-59, 8), (-52, 5), (-50, 0),
     (-44, -3), (-38, -5), (-35, -8), (-38, -15), (-40, -22), (-48, -28),
     (-55, -35), (-62, -41), (-65, -45), (-68, -50), (-70, -54), (-73, -50),
     (-73, -40), (-72, -30), (-70, -20), (-75, -15), (-80, -6), (-81, 0),
     (-80, 6), (-79, 9)],
    # Africa
    [(-17, 15), (-15, 20), (-10, 28), (-5, 35), (0, 36), (10, 37),
     (20, 32), (30, 31), (32, 27), (35, 20), (38, 18), (43, 12), (48, 11),
     (51, 10), (46, 5), (41, 0), (40, -5), (40, -12), (36, -18), (32, -25),
     (28, -32), (20, -35), (16, -28), (12, -18), (12, -8), (9, 4), (4, 6),
     (-5, 5), (-10, 6), (-13, 8), (-17, 15)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (2, 51), (5, 53), (8, 57), (10, 59),
     (5, 60), (10, 62), (18, 65), (21, 69), (25, 71), (30, 70), (32, 66),
     (35, 65), (40, 66), (42, 60), (45, 55), (48, 50), (45, 45), (40, 45),
     (35, 44), (30, 45), (28, 44), (23, 40), (20, 40), (15, 44), (12, 44),
     (8, 44), (3, 43), (0, 40), (-2, 37), (-6, 36), (-10, 36)],
    # Asia
    [(30, 70), (40, 68), (50, 69), (60, 69), (70, 72), (80, 73), (90, 75),
     (100, 77), (110, 76), (120, 73), (130, 72), (140, 72), (150, 70),
     (160, 68), (170, 66), (178, 65), (170, 60), (162, 58), (158, 52),
     (150, 50), (142, 45), (140, 40), (135, 35), (130, 33), (127, 35),
     (122, 38), (120, 32), (115, 25), (110, 20), (108, 12), (105, 8),
     (100, 8), (97, 15), (92, 20), (90, 22), (86, 20), (80, 15), (77, 8),
     (75, 12), (72, 20), (68, 23), (66, 25), (62, 25), (58, 26), (56, 28),
     (54, 26), (52, 25), (50, 28), (48, 30), (45, 30), (42, 32), (40, 36),
     (36, 36), (33, 38), (30, 40), (30, 45), (28, 44), (30, 45), (32, 50),
     (35, 55), (38, 60), (35, 65), (32, 68), (30, 70)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (125, -32), (130, -32),
     (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27),
     (150, -22), (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
     (132, -12), (130, -13), (126, -14), (122, -17), (118, -20), (113, -22)],
    # UK
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (0, 53), (-1, 51), (-5, 50)],
    # Japan
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 42), (143, 44),
     (145, 44), (141, 40), (140, 36), (136, 34), (132, 33), (130, 31)],
    # Indonesia band
    [(95, 5), (100, 0), (105, -5), (110, -7), (115, -8), (120, -10),
     (125, -9), (130, -4), (135, -3), (140, -4), (145, -6), (140, -8),
     (130, -8), (120, -6), (110, -4), (100, -2), (95, 5)],
]


def project(lon, lat, x, y, w, h):
    """Equirectangular: lon -180..180 -> x..x+w, lat 80..-55 -> y..y+h."""
    px = x + (lon + 180.0) / 360.0 * w
    py = y + (80.0 - lat) / 135.0 * h
    return int(px), int(py)


def draw_map(canvas, x, y, w, h, dots, land=(196, 205, 190),
             sea=(222, 232, 238), line_c=(120, 130, 120)):
    """dots: list of (lon, lat, number, region_color)."""
    canvas.fill_rect(x, y, w, h, sea)
    for poly in CONTINENTS:
        pts = [project(lon, lat, x, y, w, h) for lon, lat in poly]
        canvas.poly(pts, land)
        canvas.poly_line(pts + [pts[0]], line_c, 1)
    for lon, lat, num, color in dots:
        px, py = project(lon, lat, x, y, w, h)
        canvas.circle(px, py, 7, (255, 255, 255))
        canvas.circle(px, py, 6, color)
        canvas.draw_text_center(px, py + 3, "sans_bold_8", str(num),
                                (255, 255, 255))

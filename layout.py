#!/usr/bin/env python3
"""Section builders for the fixed news-image style (3 leads + 12 pictures
+ briefs), plus multi-element scene illustrations.  Written fresh for the
24 November field; no code is copied from earlier fields.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from newsframe import Canvas, draw_map  # noqa: F401  (re-exported)

INK = (18, 18, 18)
RED = (178, 30, 30)
RED_DK = (140, 20, 20)
NAVY = (22, 42, 92)
GRAY = (110, 110, 110)
LINE = (180, 180, 180)
PAPER = (255, 255, 255)
CREAM = (250, 247, 240)

REGION_COLORS = {
    "Americas": (30, 90, 160),
    "Europe": (200, 120, 20),
    "Africa": (160, 40, 90),
    "Asia": (30, 140, 90),
    "Middle East": (120, 60, 160),
    "Latin America": (200, 60, 60),
    "Oceania": (20, 140, 180),
}
REGION_ORDER = ["Americas", "Europe", "Africa", "Asia", "Middle East",
                "Latin America", "Oceania"]


# ---------------------------------------------------------------- scenes
def _chip(c, x, y, w, h):
    """Motherboard scene: dark board, gold traces, black chips, capacitors."""
    c.fill_rect(x, y, w, h, (16, 66, 38))
    # gold traces: right-angle runs with via dots
    gold = (198, 158, 40)
    for (x0, y0, x1, y1) in [
        (0.05, 0.15, 0.30, 0.15), (0.30, 0.15, 0.30, 0.45),
        (0.55, 0.10, 0.55, 0.35), (0.55, 0.35, 0.80, 0.35),
        (0.08, 0.70, 0.35, 0.70), (0.35, 0.70, 0.35, 0.90),
        (0.70, 0.60, 0.90, 0.60), (0.90, 0.60, 0.90, 0.85),
        (0.15, 0.45, 0.15, 0.65), (0.15, 0.65, 0.28, 0.65),
    ]:
        c.line(x + int(x0 * w), y + int(y0 * h), x + int(x1 * w),
               y + int(y1 * h), gold, 2)
    for (fx, fy) in [(0.30, 0.45), (0.55, 0.35), (0.35, 0.70), (0.90, 0.60),
                     (0.15, 0.65), (0.80, 0.35)]:
        c.circle(x + int(fx * w), y + int(fy * h), 3, gold)
    # main chip
    cx, cy, cw, ch = int(0.38 * w), int(0.42 * h), int(0.24 * w), int(0.34 * h)
    c.fill_rect(x + cx, y + cy, cw, ch, (12, 12, 12))
    c.rect(x + cx, y + cy, cw, ch, (90, 90, 90), 1)
    for i in range(5):
        c.fill_rect(x + cx + 4 + i * (cw // 5), y + cy - 4, 3, 4, (160, 160, 160))
        c.fill_rect(x + cx + 4 + i * (cw // 5), y + cy + ch, 3, 4, (160, 160, 160))
    c.draw_text(x + cx + 6, y + cy + ch // 2 + 3, "sans_bold_8", "CPU",
                (200, 200, 200))
    # small chip + capacitors
    c.fill_rect(x + int(0.68 * w), y + int(0.70 * h), int(0.10 * w),
                int(0.16 * h), (20, 20, 20))
    for fx in (0.66, 0.72):
        c.fill_rect(x + int(fx * w), y + int(0.18 * h), 4, 10, (150, 150, 150))
        c.fill_rect(x + int(fx * w), y + int(0.18 * h) + 10, 4, 4, (60, 60, 60))


def _sea(c, x, y, w, h):
    """Naval battle scene: sky, clouds, coast, warship, freighter, drone,
    explosion."""
    c.fill_rect(x, y, w, h, (168, 198, 222))
    # clouds
    for (fx, fy, fw) in [(0.08, 0.10, 60), (0.55, 0.06, 70), (0.78, 0.16, 50)]:
        c.fill_rect(x + int(fx * w), y + int(fy * h), fw, 10, (235, 240, 245))
        c.circle(x + int(fx * w) + 12, y + int(fy * h) - 2, 8, (235, 240, 245))
    # distant coast
    c.poly([(x, y + int(0.42 * h)), (x + int(0.30 * w), y + int(0.34 * h)),
            (x + int(0.45 * w), y + int(0.42 * h)), (x, y + int(0.42 * h))],
           (120, 140, 110))
    # sea
    c.fill_rect(x, y + int(0.42 * h), w, h - int(0.42 * h), (32, 78, 128))
    for fy in (0.55, 0.68, 0.82):
        for k in range(6):
            fx = 0.05 + k * 0.16
            c.line(x + int(fx * w), y + int(fy * h),
                   x + int((fx + 0.08) * w), y + int(fy * h),
                   (140, 190, 230), 1)
    # warship
    hx, hy = x + int(0.18 * w), y + int(0.50 * h)
    c.poly([(hx, hy + 22), (hx + 8, hy + 22), (hx + 14, hy + 6),
            (hx + 150, hy + 6), (hx + 168, hy + 22), (hx, hy + 22)],
           (52, 58, 66))
    c.fill_rect(hx + 30, hy - 14, 70, 20, (66, 72, 82))  # bridge
    for i in range(5):
        c.fill_rect(hx + 36 + i * 13, hy - 10, 8, 8, (255, 220, 120))
    c.line(hx + 60, hy - 14, hx + 60, hy - 34, (40, 44, 52), 2)  # radar mast
    c.circle(hx + 60, hy - 36, 4, (200, 200, 200))
    c.fill_rect(hx + 108, hy - 8, 10, 14, (40, 44, 52))  # funnel
    c.circle(hx + 113, hy - 12, 5, (180, 180, 180))
    c.circle(hx + 118, hy - 16, 7, (200, 200, 200))
    c.fill_rect(hx + 130, hy - 2, 16, 8, (40, 44, 52))  # turret
    # bow wave
    c.poly([(hx + 168, hy + 22), (hx + 185, hy + 26), (hx + 168, hy + 30)],
           (220, 235, 245))
    # freighter silhouette behind
    fx0, fy0 = x + int(0.62 * w), y + int(0.44 * h)
    c.fill_rect(fx0, fy0, 90, 16, (40, 52, 70))
    for i in range(4):
        c.fill_rect(fx0 + 8 + i * 20, fy0 - 8, 14, 8, (60, 74, 96))
    # drone with dashed trajectory
    dx, dy = x + int(0.80 * w), y + int(0.18 * h)
    for k in range(6):
        c.line(dx - k * 12, dy + k * 3, dx - k * 12 - 6, dy + k * 3 + 2,
               (255, 255, 255), 1)
    c.fill_rect(dx - 6, dy - 3, 14, 6, (30, 30, 30))
    c.fill_rect(dx - 2, dy - 6, 4, 12, (30, 30, 30))
    # explosion
    ex, ey = x + int(0.48 * w), y + int(0.30 * h)
    c.circle(ex, ey, 16, (255, 200, 60))
    c.circle(ex, ey, 10, (255, 120, 30))
    c.circle(ex, ey, 5, (255, 240, 180))
    c.circle(ex - 14, ey - 18, 8, (120, 120, 120))
    c.circle(ex + 12, ey - 22, 6, (140, 140, 140))
    for (ox, oy) in [(-24, 8), (26, 4), (-8, 16), (20, 14)]:
        c.fill_rect(ex + ox, ey + oy, 3, 3, (60, 60, 60))


def _chart(c, x, y, w, h):
    """Trading screen: dark bg, volume bars, two crossing trend lines."""
    c.fill_rect(x, y, w, h, (24, 24, 28))
    # grid
    for gy in (0.25, 0.50, 0.75):
        c.hline(x, y + int(gy * h), w, (60, 60, 66), 1)
    # volume bars along the bottom
    import random as _r
    rnd = _r.Random(42)
    bw = w // 18
    for i in range(18):
        bh = rnd.randint(4, int(0.22 * h))
        col = (60, 160, 90) if rnd.random() > 0.4 else (200, 70, 60)
        c.fill_rect(x + i * bw + 2, y + h - bh, bw - 4, bh, col)
    # falling red dashed line
    pts = []
    for i in range(9):
        pts.append((x + int(0.04 * w) + i * int(0.10 * w),
                    y + int((0.28 + i * 0.045) * h)))
    for i in range(len(pts) - 1):
        c.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1],
               (220, 70, 60), 2)
    # rising green line
    pts2 = []
    for i in range(9):
        pts2.append((x + int(0.04 * w) + i * int(0.10 * w),
                     y + int((0.62 - i * 0.05) * h)))
    for i in range(len(pts2) - 1):
        c.line(pts2[i][0], pts2[i][1], pts2[i + 1][0], pts2[i + 1][1],
               (70, 200, 110), 2)
    c.draw_text(x + int(0.06 * w), y + int(0.14 * h), "sans_bold_14", "+4.7%",
                (90, 220, 130))


def _court(c, x, y, w, h):
    """Courthouse: columns, pediment, steps."""
    c.fill_rect(x, y, w, h, (178, 172, 158))
    c.poly([(x + int(0.10 * w), y + int(0.30 * h)), (x + int(0.50 * w), y + int(0.08 * h)),
            (x + int(0.90 * w), y + int(0.30 * h))], (140, 128, 105))
    c.circle(x + int(0.50 * w), y + int(0.20 * h), 7, (110, 100, 80))
    for i in range(5):
        cx = x + int((0.14 + i * 0.18) * w)
        c.fill_rect(cx, y + int(0.32 * h), 12, int(0.42 * h), (238, 235, 225))
        c.rect(cx, y + int(0.32 * h), 12, int(0.42 * h), (120, 110, 90), 1)
        c.fill_rect(cx - 3, y + int(0.30 * h), 18, 5, (215, 212, 200))
        c.fill_rect(cx - 3, y + int(0.74 * h), 18, 5, (215, 212, 200))
    for i in range(3):
        c.fill_rect(x, y + h - 12 - i * 6, w, 5, (150, 146, 134))


def _summit(c, x, y, w, h):
    """Summit table: flags row, table, microphones."""
    c.fill_rect(x, y, w, h, (44, 66, 110))
    for i, col in enumerate([(180, 40, 40), (40, 90, 180), (220, 200, 60),
                             (40, 140, 80), (200, 120, 40)]):
        fx = x + int((0.08 + i * 0.19) * w)
        c.fill_rect(fx, y + int(0.12 * h), 26, 17, col)
        c.line(fx + 13, y + int(0.12 * h), fx + 13, y + int(0.38 * h),
               (220, 220, 220), 1)
    c.fill_rect(x + int(0.08 * w), y + int(0.55 * h), int(0.84 * w),
                int(0.22 * h), (120, 80, 50))
    c.fill_rect(x + int(0.08 * w), y + int(0.55 * h), int(0.84 * w), 4,
                (170, 120, 70))
    for i in range(4):
        mx = x + int((0.22 + i * 0.20) * w)
        c.line(mx, y + int(0.55 * h), mx, y + int(0.44 * h), (30, 30, 30), 2)
        c.circle(mx, y + int(0.42 * h), 4, (30, 30, 30))
    for i in range(5):
        c.circle(x + int((0.18 + i * 0.16) * w), y + int(0.86 * h), 8,
                 (230, 210, 180))


def _storm(c, x, y, w, h):
    """Storm: dark cloud, rain, lightning, flooded street."""
    c.fill_rect(x, y, w, h, (70, 90, 120))
    c.circle(x + int(0.30 * w), y + int(0.25 * h), 22, (50, 55, 65))
    c.circle(x + int(0.55 * w), y + int(0.20 * h), 26, (45, 50, 60))
    c.circle(x + int(0.75 * w), y + int(0.28 * h), 18, (55, 60, 70))
    c.fill_rect(x + int(0.12 * w), y + int(0.22 * h), int(0.76 * w),
                int(0.22 * h), (50, 55, 65))
    c.poly([(x + int(0.55 * w), y + int(0.40 * h)),
            (x + int(0.45 * w), y + int(0.60 * h)),
            (x + int(0.55 * w), y + int(0.60 * h)),
            (x + int(0.48 * w), y + int(0.78 * h)),
            (x + int(0.62 * w), y + int(0.52 * h)),
            (x + int(0.52 * w), y + int(0.52 * h)),
            (x + int(0.62 * w), y + int(0.40 * h))], (255, 230, 80))
    for i in range(8):
        rx = x + int((0.08 + i * 0.11) * w)
        c.line(rx, y + int(0.55 * h), rx - 6, y + int(0.68 * h),
               (170, 200, 235), 1)
    c.fill_rect(x, y + int(0.85 * h), w, h - int(0.85 * h), (40, 70, 110))


def _rocket(c, x, y, w, h):
    """Rocket launch: tower, rocket, smoke, flame."""
    c.fill_rect(x, y, w, h, (150, 190, 225))
    c.circle(x + int(0.80 * w), y + int(0.18 * h), 12, (255, 240, 180))
    for i in range(3):
        c.circle(x + int((0.15 + i * 0.12) * w), y + int(0.15 * h), 9,
                 (235, 240, 245))
    rx = x + int(0.42 * w)
    c.poly([(rx, y + int(0.12 * h)), (rx + 14, y + int(0.30 * h)),
            (rx + 14, y + int(0.62 * h)), (rx, y + int(0.62 * h))],
           (235, 235, 235))
    c.poly([(rx, y + int(0.12 * h)), (rx + 7, y + int(0.02 * h)),
            (rx + 14, y + int(0.12 * h))], (200, 40, 40))
    c.circle(rx + 7, y + int(0.38 * h), 4, (60, 120, 200))
    c.poly([(rx, y + int(0.62 * h)), (rx - 8, y + int(0.74 * h)),
            (rx, y + int(0.68 * h))], (200, 40, 40))
    c.poly([(rx + 14, y + int(0.62 * h)), (rx + 22, y + int(0.74 * h)),
            (rx + 14, y + int(0.68 * h))], (200, 40, 40))
    c.poly([(rx + 2, y + int(0.74 * h)), (rx + 7, y + int(0.92 * h)),
            (rx + 12, y + int(0.74 * h))], (255, 160, 40))
    c.fill_rect(x + int(0.15 * w), y + int(0.20 * h), 6, int(0.60 * h),
                (90, 90, 90))
    for i in range(3):
        c.fill_rect(x + int(0.15 * w) - 6, y + int((0.28 + i * 0.16) * h),
                    18, 4, (90, 90, 90))
    for i in range(5):
        c.circle(x + int((0.30 + i * 0.10) * w), y + int(0.88 * h), 10,
                 (225, 225, 225))
    c.fill_rect(x, y + int(0.92 * h), w, 4, (100, 100, 100))


def _tanker(c, x, y, w, h):
    """Oil tanker at sea with waves and smoke."""
    c.fill_rect(x, y, w, h, (170, 200, 225))
    c.circle(x + int(0.82 * w), y + int(0.16 * h), 10, (255, 240, 180))
    c.fill_rect(x, y + int(0.55 * h), w, h - int(0.55 * h), (40, 90, 140))
    for fy in (0.62, 0.74, 0.86):
        for k in range(5):
            fx = 0.05 + k * 0.20
            c.line(x + int(fx * w), y + int(fy * h),
                   x + int((fx + 0.10) * w), y + int(fy * h),
                   (150, 200, 240), 1)
    hx = x + int(0.10 * w)
    c.fill_rect(hx, y + int(0.42 * h), int(0.72 * w), int(0.16 * h),
                (120, 40, 30))
    c.fill_rect(hx + int(0.58 * w), y + int(0.28 * h), int(0.12 * w),
                int(0.14 * h), (230, 230, 230))
    for i in range(3):
        c.fill_rect(hx + int(0.60 * w) + i * 8, y + int(0.31 * h), 5, 5,
                    (60, 120, 200))
    c.fill_rect(hx + int(0.30 * w), y + int(0.34 * h), 8, int(0.08 * h),
                (60, 60, 60))
    c.circle(hx + int(0.32 * w), y + int(0.30 * h), 5, (180, 180, 180))
    c.circle(hx + int(0.36 * w), y + int(0.26 * h), 6, (200, 200, 200))


def _soccer(c, x, y, w, h):
    """Soccer: pitch, goal, ball with motion lines."""
    c.fill_rect(x, y, w, h, (60, 150, 70))
    for i in range(4):
        c.fill_rect(x, y + i * (h // 4), w, h // 8, (70, 165, 80))
    c.fill_rect(x + int(0.62 * w), y + int(0.15 * h), int(0.30 * w),
                int(0.45 * h), (255, 255, 255))
    c.rect(x + int(0.62 * w), y + int(0.15 * h), int(0.30 * w),
           int(0.45 * h), (255, 255, 255), 2)
    for i in range(3):
        c.vline(x + int((0.68 + i * 0.09) * w), y + int(0.15 * h),
                int(0.45 * h), (200, 200, 200), 1)
        c.hline(x + int(0.62 * w), y + int((0.25 + i * 0.11) * h),
                int(0.30 * w), (200, 200, 200), 1)
    bx, by = x + int(0.32 * w), y + int(0.55 * h)
    c.circle(bx, by, 13, (255, 255, 255))
    c.circle(bx, by, 13, (40, 40, 40), fill=False)
    c.circle(bx, by, 4, (40, 40, 40))
    for k in range(3):
        c.line(bx - 18 - k * 10, by - 6, bx - 10 - k * 10, by - 6,
               (255, 255, 255), 1)


def _mountain(c, x, y, w, h):
    """Snow mountain with sun, clouds and pines."""
    c.fill_rect(x, y, w, h, (140, 180, 220))
    c.circle(x + int(0.80 * w), y + int(0.16 * h), 11, (255, 240, 170))
    c.circle(x + int(0.20 * w), y + int(0.14 * h), 9, (240, 244, 248))
    c.circle(x + int(0.28 * w), y + int(0.12 * h), 7, (240, 244, 248))
    c.poly([(x + int(0.05 * w), y + h), (x + int(0.42 * w), y + int(0.18 * h)),
            (x + int(0.78 * w), y + h)], (90, 110, 140))
    c.poly([(x + int(0.34 * w), y + int(0.28 * h)),
            (x + int(0.42 * w), y + int(0.18 * h)),
            (x + int(0.50 * w), y + int(0.28 * h)),
            (x + int(0.46 * w), y + int(0.34 * h)),
            (x + int(0.38 * w), y + int(0.34 * h))], (245, 248, 250))
    c.poly([(x + int(0.55 * w), y + h), (x + int(0.82 * w), y + int(0.42 * h)),
            (x + w, y + h)], (70, 90, 120))
    for (fx, fy) in [(0.12, 0.78), (0.20, 0.82), (0.88, 0.80)]:
        px, py = x + int(fx * w), y + int(fy * h)
        c.poly([(px, py - 12), (px - 7, py + 4), (px + 7, py + 4)],
               (30, 90, 50))
        c.fill_rect(px - 1, py + 4, 3, 6, (90, 60, 40))


def _building(c, x, y, w, h):
    """City towers with windows, street and tree."""
    c.fill_rect(x, y, w, h, (180, 200, 225))
    c.fill_rect(x, y + int(0.70 * h), w, h - int(0.70 * h), (90, 90, 90))
    for (fx, fw, fh, col) in [(0.06, 0.20, 0.62, (70, 80, 110)),
                               (0.30, 0.26, 0.70, (50, 60, 90)),
                               (0.60, 0.18, 0.55, (80, 90, 120)),
                               (0.80, 0.16, 0.66, (60, 70, 100))]:
        bx = x + int(fx * w)
        by = y + int((0.70 - fh) * h)
        c.fill_rect(bx, by, int(fw * w), int(fh * h), col)
        for r in range(4):
            for col_i in range(3):
                wx = bx + 5 + col_i * (int(fw * w) // 3)
                wy = by + 6 + r * (int(fh * h) // 5)
                if (r + col_i) % 3:
                    c.fill_rect(wx, wy, 6, 7, (255, 220, 120))
    c.circle(x + int(0.50 * w), y + int(0.62 * h), 8, (40, 120, 60))
    c.fill_rect(x + int(0.50 * w) - 1, y + int(0.62 * h), 3, 10, (90, 60, 40))


def _diamond(c, x, y, w, h):
    """Cut gem with facets and sparkles."""
    c.fill_rect(x, y, w, h, (30, 30, 40))
    cx, cy = x + w // 2, y + int(0.48 * h)
    c.poly([(cx - 34, cy - 16), (cx + 34, cy - 16), (cx + 20, cy + 20),
            (cx - 20, cy + 20)], (150, 220, 250))
    c.poly([(cx - 34, cy - 16), (cx - 12, cy - 16), (cx, cy + 20),
            (cx - 20, cy + 20)], (110, 190, 230))
    c.poly([(cx + 12, cy - 16), (cx + 34, cy - 16), (cx + 20, cy + 20),
            (cx, cy + 20)], (190, 240, 255))
    c.line(cx - 12, cy - 16, cx, cy + 20, (230, 250, 255), 1)
    c.line(cx + 12, cy - 16, cx, cy + 20, (230, 250, 255), 1)
    for (fx, fy) in [(0.18, 0.20), (0.85, 0.25), (0.78, 0.80)]:
        px, py = x + int(fx * w), y + int(fy * h)
        c.line(px - 6, py, px + 6, py, (255, 255, 255), 1)
        c.line(px, py - 6, px, py + 6, (255, 255, 255), 1)


def _flame(c, x, y, w, h):
    """Factory fire: plant silhouette, chimneys, flame."""
    c.fill_rect(x, y, w, h, (96, 96, 112))
    c.fill_rect(x + int(0.08 * w), y + int(0.60 * h), int(0.84 * w),
                int(0.28 * h), (45, 45, 58))
    for (fx, fw) in [(0.15, 0.08), (0.30, 0.06), (0.70, 0.09)]:
        c.fill_rect(x + int(fx * w), y + int(0.30 * h), int(fw * w),
                    int(0.30 * h), (45, 45, 58))
        c.circle(x + int((fx + fw / 2) * w), y + int(0.26 * h), 7,
                 (170, 170, 170))
    fx, fy = x + int(0.50 * w), y + int(0.55 * h)
    c.poly([(fx, fy - 44), (fx - 18, fy), (fx - 6, fy - 15), (fx, fy + 2),
            (fx + 7, fy - 15), (fx + 18, fy)], (255, 120, 30))
    c.poly([(fx, fy - 22), (fx - 9, fy), (fx, fy + 2), (fx + 9, fy)],
           (255, 200, 60))


def _satellite(c, x, y, w, h):
    """Satellite over Earth curve."""
    c.fill_rect(x, y, w, h, (12, 16, 36))
    for i in range(14):
        c.fill_rect(x + (i * 11) % w, y + (i * 37) % h, 2, 2,
                    (220, 220, 220))
    c.circle(x + w // 2, y + h + 55, 70, (40, 90, 150))
    c.fill_rect(x + int(0.18 * w), y + int(0.30 * h), int(0.20 * w), 10,
                (60, 110, 200))
    c.fill_rect(x + int(0.62 * w), y + int(0.30 * h), int(0.20 * w), 10,
                (60, 110, 200))
    c.fill_rect(x + int(0.40 * w), y + int(0.26 * h), int(0.20 * w), 18,
                (200, 200, 210))
    c.line(x + int(0.50 * w), y + int(0.26 * h), x + int(0.50 * w),
           y + int(0.12 * h), (200, 200, 210), 2)
    c.circle(x + int(0.50 * w), y + int(0.10 * h), 4, (255, 220, 80))


def _plane(c, x, y, w, h):
    """Airliner in sky with contrail and clouds."""
    c.fill_rect(x, y, w, h, (150, 190, 230))
    for (fx, fy) in [(0.12, 0.20), (0.70, 0.12), (0.85, 0.70)]:
        c.circle(x + int(fx * w), y + int(fy * h), 10, (240, 244, 248))
        c.circle(x + int(fx * w) + 12, y + int(fy * h) + 2, 7,
                 (240, 244, 248))
    px, py = x + int(0.45 * w), y + int(0.45 * h)
    c.poly([(px - 46, py - 2), (px + 44, py - 10), (px + 54, py - 4),
            (px + 44, py + 6), (px - 46, py + 8)], (60, 70, 95))
    c.poly([(px - 6, py - 6), (px + 6, py - 30), (px + 14, py - 6)],
           (45, 55, 80))
    c.poly([(px - 34, py + 6), (px - 22, py + 24), (px - 12, py + 6)],
           (45, 55, 80))
    for i in range(4):
        c.fill_rect(px + 8 + i * 8, py - 6, 5, 4, (180, 200, 230))
    for k in range(5):
        c.line(px - 46 - k * 10, py + 2, px - 52 - k * 10, py + 2,
               (255, 255, 255), 1)


def _vote(c, x, y, w, h):
    """Ballot box with a ballot going in."""
    c.fill_rect(x, y, w, h, (200, 190, 170))
    c.fill_rect(x + int(0.20 * w), y + int(0.45 * h), int(0.60 * w),
                int(0.35 * h), (120, 40, 40))
    c.fill_rect(x + int(0.16 * w), y + int(0.38 * h), int(0.68 * w), 8,
                (90, 30, 30))
    c.fill_rect(x + int(0.42 * w), y + int(0.40 * h), int(0.16 * w), 4,
                (20, 20, 20))
    c.poly([(x + int(0.40 * w), y + int(0.40 * h)),
            (x + int(0.48 * w), y + int(0.16 * h)),
            (x + int(0.60 * w), y + int(0.20 * h)),
            (x + int(0.52 * w), y + int(0.40 * h))], (255, 255, 255))
    c.draw_text(x + int(0.34 * w), y + int(0.68 * h), "sans_bold_12", "VOTE",
                (255, 255, 255))


def _medal(c, x, y, w, h):
    """Gold medal on ribbon."""
    c.fill_rect(x, y, w, h, (40, 50, 90))
    c.poly([(x + int(0.35 * w), y), (x + int(0.48 * w), y + int(0.42 * h)),
            (x + int(0.38 * w), y + int(0.42 * h)),
            (x + int(0.25 * w), y)], (200, 40, 40))
    c.poly([(x + int(0.65 * w), y), (x + int(0.52 * w), y + int(0.42 * h)),
            (x + int(0.62 * w), y + int(0.42 * h)),
            (x + int(0.75 * w), y)], (200, 40, 40))
    cx, cy = x + w // 2, y + int(0.62 * h)
    c.circle(cx, cy, 20, (220, 170, 40))
    c.circle(cx, cy, 15, (240, 200, 80), fill=False)
    c.draw_text(cx - 5, cy + 5, "sans_bold_14", "1", (120, 80, 0))


def _solar(c, x, y, w, h):
    """Solar panels under sun."""
    c.fill_rect(x, y, w, h, (140, 190, 230))
    c.circle(x + int(0.80 * w), y + int(0.16 * h), 12, (255, 235, 150))
    c.fill_rect(x, y + int(0.68 * h), w, h - int(0.68 * h), (90, 140, 80))
    for i, fx in enumerate((0.10, 0.40, 0.70)):
        px = x + int(fx * w)
        py = y + int(0.42 * h) + (i % 2) * 8
        c.poly([(px, py), (px + 34, py - 8), (px + 40, py + 12),
                (px + 6, py + 20)], (30, 60, 140))
        c.line(px + 17, py - 4, px + 23, py + 16, (150, 180, 230), 1)
        c.line(px, py + 6, px + 37, py + 2, (150, 180, 230), 1)
        c.line(px + 17, py + 20, px + 20, py + 34, (60, 60, 60), 2)


def _forest(c, x, y, w, h):
    """Forest with sun and birds."""
    c.fill_rect(x, y, w, h, (150, 200, 230))
    c.circle(x + int(0.78 * w), y + int(0.16 * h), 11, (255, 240, 170))
    for (fx, fh) in [(0.08, 0.55), (0.22, 0.70), (0.38, 0.50), (0.55, 0.68),
                      (0.72, 0.52), (0.86, 0.62)]:
        px = x + int(fx * w)
        py = y + int((0.95 - fh) * h)
        c.poly([(px, py), (px - 12, py + int(fh * h)),
                (px + 12, py + int(fh * h))], (30, 110, 60))
        c.fill_rect(px - 2, y + int(0.95 * h) - 8, 4, 8, (90, 60, 40))
    c.fill_rect(x, y + int(0.92 * h), w, 4, (60, 110, 70))
    for (fx, fy) in [(0.30, 0.18), (0.45, 0.12)]:
        px, py = x + int(fx * w), y + int(fy * h)
        c.line(px - 6, py, px, py - 4, (40, 40, 40), 1)
        c.line(px, py - 4, px + 6, py, (40, 40, 40), 1)


def _ship(c, x, y, w, h):
    """Container ship at dusk."""
    c.fill_rect(x, y, w, h, (240, 180, 120))
    c.circle(x + int(0.82 * w), y + int(0.20 * h), 13, (255, 220, 120))
    c.fill_rect(x, y + int(0.62 * h), w, h - int(0.62 * h), (50, 90, 140))
    hx = x + int(0.08 * w)
    c.poly([(hx, y + int(0.52 * h)), (hx + int(0.84 * w), y + int(0.52 * h)),
            (hx + int(0.76 * w), y + int(0.62 * h)), (hx + 6, y + int(0.62 * h))],
           (40, 45, 55))
    for i, col in enumerate([(200, 60, 50), (60, 140, 80), (220, 180, 60),
                             (60, 110, 200)]):
        c.fill_rect(hx + 12 + i * 26, y + int(0.34 * h), 22, 16, col)
    c.fill_rect(hx + int(0.72 * w), y + int(0.30 * h), 14, 22,
                (230, 230, 230))


def _market(c, x, y, w, h):
    """Market stall: awning, crates, fruit."""
    c.fill_rect(x, y, w, h, (200, 215, 235))
    for i in range(5):
        col = (200, 50, 50) if i % 2 == 0 else (245, 245, 245)
        c.fill_rect(x + i * (w // 5), y, w // 5, int(0.18 * h), col)
    c.fill_rect(x, y + int(0.18 * h), w, 4, (120, 60, 40))
    for (fx, col) in [(0.12, (240, 120, 40)), (0.38, (220, 40, 40)),
                      (0.62, (140, 200, 60)), (0.84, (240, 200, 40))]:
        px = x + int(fx * w)
        py = y + int(0.62 * h)
        c.fill_rect(px - 16, py, 32, 18, (150, 100, 50))
        for k in range(3):
            c.circle(px - 8 + k * 8, py - 4, 6, col)
    c.fill_rect(x, y + int(0.80 * h), w, h - int(0.80 * h), (120, 90, 60))


def _lab(c, x, y, w, h):
    """Lab: flasks, microscope-ish bench."""
    c.fill_rect(x, y, w, h, (220, 235, 240))
    c.fill_rect(x, y + int(0.72 * h), w, h - int(0.72 * h), (120, 110, 100))
    # flask 1
    fx, fy = x + int(0.22 * w), y + int(0.30 * h)
    c.fill_rect(fx - 3, fy - 14, 6, 16, (60, 120, 160))
    c.poly([(fx - 3, fy + 2), (fx + 3, fy + 2), (fx + 14, fy + 30),
            (fx - 14, fy + 30)], (140, 200, 230))
    c.poly([(fx - 12, fy + 16), (fx + 12, fy + 16), (fx + 14, fy + 30),
            (fx - 14, fy + 30)], (60, 160, 90))
    # flask 2
    fx2 = x + int(0.62 * w)
    c.fill_rect(fx2 - 3, fy - 14, 6, 16, (60, 120, 160))
    c.poly([(fx2 - 3, fy + 2), (fx2 + 3, fy + 2), (fx2 + 12, fy + 26),
            (fx2 - 12, fy + 26)], (140, 200, 230))
    c.poly([(fx2 - 10, fy + 12), (fx2 + 10, fy + 12), (fx2 + 12, fy + 26),
            (fx2 - 12, fy + 26)], (200, 90, 90))
    # test tubes
    for i in range(3):
        tx = x + int((0.82 + i * 0.06) * w)
        c.fill_rect(tx, y + int(0.45 * h), 5, 22, (180, 220, 235))
        c.fill_rect(tx, y + int(0.58 * h), 5, 9, (90, 170, 110))


def _film(c, x, y, w, h):
    """Cinema: screen, seats, projector beam."""
    c.fill_rect(x, y, w, h, (30, 28, 40))
    c.fill_rect(x + int(0.18 * w), y + int(0.12 * h), int(0.64 * w),
                int(0.38 * h), (230, 230, 235))
    c.poly([(x + int(0.18 * w), y + int(0.12 * h)),
            (x + int(0.82 * w), y + int(0.12 * h)),
            (x + int(0.70 * w), y + int(0.50 * h)),
            (x + int(0.30 * w), y + int(0.50 * h))], (250, 250, 200))
    c.circle(x + int(0.50 * w), y + int(0.30 * h), 8, (200, 40, 40))
    for r in range(2):
        for i in range(5):
            c.fill_rect(x + int((0.14 + i * 0.16) * w),
                        y + int((0.62 + r * 0.16) * h), 18, 12,
                        (120, 40, 50))


def _trophy(c, x, y, w, h):
    """Trophy cup on a plinth."""
    c.fill_rect(x, y, w, h, (50, 60, 110))
    cx = x + w // 2
    c.poly([(cx - 20, y + int(0.15 * h)), (cx + 20, y + int(0.15 * h)),
            (cx + 14, y + int(0.42 * h)), (cx - 14, y + int(0.42 * h))],
           (230, 190, 60))
    c.poly([(cx - 30, y + int(0.15 * h)), (cx - 20, y + int(0.15 * h)),
            (cx - 20, y + int(0.32 * h)), (cx - 30, y + int(0.32 * h))],
           (230, 190, 60))
    c.poly([(cx + 20, y + int(0.15 * h)), (cx + 30, y + int(0.15 * h)),
            (cx + 30, y + int(0.32 * h)), (cx + 20, y + int(0.32 * h))],
           (230, 190, 60))
    c.fill_rect(cx - 4, y + int(0.42 * h), 8, 14, (200, 160, 40))
    c.fill_rect(cx - 22, y + int(0.56 * h), 44, 8, (120, 80, 40))
    c.fill_rect(cx - 28, y + int(0.64 * h), 56, 10, (90, 60, 30))
    for (fx, fy) in [(0.18, 0.22), (0.85, 0.30)]:
        px, py = x + int(fx * w), y + int(fy * h)
        c.line(px - 5, py, px + 5, py, (255, 255, 255), 1)
        c.line(px, py - 5, px, py + 5, (255, 255, 255), 1)


def _generic(c, x, y, w, h):
    """Fallback scene: sun, hills, road."""
    c.fill_rect(x, y, w, h, (170, 200, 230))
    c.circle(x + int(0.78 * w), y + int(0.18 * h), 11, (255, 240, 170))
    c.poly([(x, y + h), (x + int(0.30 * w), y + int(0.45 * h)),
            (x + int(0.65 * w), y + h)], (100, 160, 100))
    c.poly([(x + int(0.45 * w), y + h), (x + int(0.80 * w), y + int(0.55 * h)),
            (x + w, y + h)], (80, 140, 90))
    c.fill_rect(x, y + int(0.85 * h), w, 4, (120, 120, 120))


SCENES = {
    "chip": _chip, "sea": _sea, "chart": _chart, "court": _court,
    "summit": _summit, "storm": _storm, "rocket": _rocket,
    "tanker": _tanker, "soccer": _soccer, "mountain": _mountain,
    "building": _building, "diamond": _diamond, "flame": _flame,
    "satellite": _satellite, "plane": _plane, "vote": _vote,
    "medal": _medal, "solar": _solar, "forest": _forest, "ship": _ship,
    "market": _market, "lab": _lab, "film": _film, "trophy": _trophy,
    "generic": _generic,
}


def draw_scene(c, kind, x, y, w, h):
    fn = SCENES.get(kind, _generic)
    fn(c, x, y, w, h)


# ---------------------------------------------------------------- sections
def header(c, date_title, red_line, overview):
    c.fill_rect(0, 0, 1024, 6, NAVY)
    c.draw_text(16, 62, "serif_bold_54", date_title, INK)
    c.draw_text(16, 88, "serif_italic_16", red_line, RED)
    c.hline(16, 98, 992, INK, 2)
    c.draw_text_center(512, 118, "sans_bold_11", overview, INK)
    c.hline(16, 126, 992, LINE, 1)
    return 134


def headline_board(c, x, y, w, item, art_h=88, num=None):
    """item: dict with scene, banner, title, summary, place, cred, geotag,
    geotag_pos ('bl'|'br'|'tr')."""
    c.rect(x, y, w, art_h, INK, 1)
    draw_scene(c, item["scene"], x + 1, y + 1, w - 2, art_h - 2)
    # numbered circle (region colour) so pins on the map match stories
    bx = x + 1
    if num is not None:
        col = REGION_COLORS.get(item.get("region", ""), (100, 100, 100))
        c.circle(x + 11, y + 11, 9, (255, 255, 255))
        c.circle(x + 11, y + 11, 8, col)
        c.draw_text_center(x + 11, y + 14, "sans_bold_9", str(num),
                           (255, 255, 255))
        bx = x + 24
    # red banner across the top of the art
    bw = c.text_width("sans_bold_10", item["banner"]) + 14
    c.fill_rect(bx, y + 1, bw, 16, RED)
    c.draw_text(bx + 7, y + 13, "sans_bold_10", item["banner"], (255, 255, 255))
    # place name written inside the scene
    tag = item.get("geotag", "")
    if tag:
        tw = c.text_width("sans_bold_9", tag)
        pos = item.get("geotag_pos", "br")
        if pos == "br":
            tx, ty = x + w - tw - 8, y + art_h - 6
        elif pos == "bl":
            tx, ty = x + 8, y + art_h - 6
        else:
            tx, ty = x + w - tw - 8, y + 22
        c.fill_rect(tx - 4, ty - 10, tw + 8, 13, (255, 255, 255))
        c.draw_text(tx, ty, "sans_bold_9", tag, INK)
    ty = y + art_h + 8
    n = c.draw_wrapped(x, ty, "serif_bold_16", item["title"], w, 19, INK,
                       max_lines=2)
    ty += n * 19 + 2
    n2 = c.draw_wrapped(x, ty, "sans_11", item["summary"], w, 14, (40, 40, 40),
                        max_lines=2)
    ty += n2 * 14 + 4
    # place bar + credibility tag
    c.draw_text(x, ty + 10, "sans_bold_10", item["place"], INK)
    cw = c.text_width("sans_bold_9", item["cred"]) + 10
    c.rect(x + w - cw, ty, cw, 13, INK, 1)
    c.draw_text(x + w - cw + 5, ty + 10, "sans_bold_9", item["cred"], INK)
    return ty + 14


def secondary_cell(c, x, y, w, item, art_h=46, num=None):
    """item: scene, banner, title, summary, data (white box text or ''),
    cred."""
    c.rect(x, y, w, art_h, INK, 1)
    draw_scene(c, item["scene"], x + 1, y + 1, w - 2, art_h - 2)
    bx = x + 1
    if num is not None:
        col = REGION_COLORS.get(item.get("region", ""), (100, 100, 100))
        c.circle(x + 10, y + 10, 8, (255, 255, 255))
        c.circle(x + 10, y + 10, 7, col)
        c.draw_text_center(x + 10, y + 13, "sans_bold_8", str(num),
                           (255, 255, 255))
        bx = x + 21
    bw = c.text_width("sans_bold_9", item["banner"]) + 10
    c.fill_rect(bx, y + 1, bw, 13, RED)
    c.draw_text(bx + 5, y + 11, "sans_bold_9", item["banner"], (255, 255, 255))
    if item.get("data"):
        dw = c.text_width("sans_bold_10", item["data"]) + 10
        c.fill_rect(x + w - dw - 1, y + art_h - 14, dw, 13, (255, 255, 255))
        c.rect(x + w - dw - 1, y + art_h - 14, dw, 13, INK, 1)
        c.draw_text(x + w - dw + 4, y + art_h - 3, "sans_bold_10",
                    item["data"], INK)
    ty = y + art_h + 4
    n = c.draw_wrapped(x, ty, "sans_bold_11", item["title"], w, 13, INK,
                       max_lines=2)
    ty += n * 13 + 1
    n2 = c.draw_wrapped(x, ty, "sans_10", item["summary"], w, 12,
                        (50, 50, 50), max_lines=2)
    ty += n2 * 12 + 2
    c.draw_text(x, ty + 8, "sans_9", item["cred"], GRAY)
    return ty + 10


def numbers_strip(c, x, y, w, items):
    """items: list of (big, label). 6 across."""
    c.fill_rect(x, y, w, 36, NAVY)
    cw = w // len(items)
    for i, (big, label) in enumerate(items):
        cx = x + i * cw
        c.draw_text_center(cx + cw // 2, y + 18, "sans_bold_16", big,
                           (255, 255, 255))
        c.draw_text_center(cx + cw // 2, y + 31, "sans_9", label,
                           (200, 205, 220))
        if i:
            c.vline(cx, y + 5, 26, (90, 100, 140), 1)
    return y + 36


def region_bar(c, x, y, w, counts):
    """counts: dict region -> int. Draws a stacked colour bar + labels."""
    total = sum(counts.values()) or 1
    cx = x
    for r in REGION_ORDER:
        n = counts.get(r, 0)
        if n == 0:
            continue
        seg = max(8, int(w * n / total))
        c.fill_rect(cx, y, seg, 10, REGION_COLORS[r])
        cx += seg
    # labels under the bar
    lx = x
    for r in REGION_ORDER:
        n = counts.get(r, 0)
        if n == 0:
            continue
        label = "%s %d" % (r.upper(), n)
        lw = c.text_width("sans_bold_8", label)
        c.fill_rect(lx, y + 13, 7, 7, REGION_COLORS[r])
        c.draw_text(lx + 10, y + 21, "sans_bold_8", label, INK)
        lx += lw + 22
    return y + 24


def timeline_row(c, x, y, w, items):
    """items: list of (time, event). One row, each event single line."""
    c.draw_text(x, y + 10, "sans_bold_11", "UTC TIMELINE", INK)
    c.hline(x, y + 14, w, LINE, 1)
    cw = (w - 110) // len(items)
    for i, (t, ev) in enumerate(items):
        cx = x + 110 + i * cw
        c.draw_text(cx, y + 28, "sans_bold_10", t, RED)
        c.draw_text(cx, y + 40, "sans_9", ev, INK)
    return y + 44


def brief_list(c, x, y, w, items, cols=2, title="THE BRIEFS"):
    """items: list of (num, place, phrase). Two columns of numbered lines."""
    c.draw_text(x, y + 11, "sans_bold_11", title, INK)
    c.hline(x, y + 16, w, LINE, 1)
    col_w = w // cols
    rows = (len(items) + cols - 1) // cols
    for idx, item in enumerate(items):
        num, place, phrase = item[0], item[1], item[2]
        col = idx // rows
        row = idx % rows
        lx = x + col * col_w
        ly = y + 20 + row * 14
        c.draw_text(lx, ly + 10, "sans_bold_10", "%d." % num, RED)
        c.draw_text(lx + 20, ly + 10, "sans_10",
                    "%s — %s" % (place, phrase), INK)
    return y + 20 + rows * 14


def date_check(c, x, y, w, left_out, not_yet):
    c.draw_text(x, y + 11, "sans_bold_11", "DATE CHECK", INK)
    c.hline(x, y + 16, w, LINE, 1)
    lo = "LEFT OUT: " + " · ".join(left_out)
    n = c.draw_wrapped(x, y + 20, "sans_9", lo, w, 12, (60, 60, 60),
                       max_lines=2)
    ny = "NOT YET: " + " · ".join(not_yet)
    c.draw_wrapped(x, y + 20 + n * 12 + 2, "sans_9", ny, w, 12,
                   (60, 60, 60), max_lines=1)
    return y + 20 + n * 12 + 16


def footer(c, y):
    c.hline(16, y, 992, INK, 1)
    c.draw_text(16, y + 13, "sans_9",
                "HOW SURE:  CONFIRMED = 2+ outlets   ·   CLAIM = one side's account",
                INK)
    c.draw_text_right(1008, y + 13, "sans_9", "Original drawings", INK)
    c.draw_text(16, y + 26, "sans_9",
                "Sources: AP · Reuters · BBC · Bloomberg · CNBC · Al Jazeera · 24 November 2026",
                GRAY)
    c.draw_text_right(1008, y + 26, "sans_9", "24 November 2026", GRAY)
    return y + 30

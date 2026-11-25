#!/usr/bin/env python3
"""Assemble the 24 November world-news image (1024x1024 PNG).

Standard library only.  No network, no env-var reads, no dynamic
code: everything the program runs is in this repository.  Writes
/output/entry.png (the scorer's path) and entry.png next to this file.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import newsdata
from newsframe import Canvas, draw_map
import layout as L

DATA = newsdata.DATA
GEOM = newsdata.GEOM


def build():
    c = Canvas()
    y = L.header(c, DATA["date_title"], DATA["red_line"], DATA["overview"])

    # ---- 3 big headlines, one column each ----
    col_w = GEOM["headline_col_w"]
    gap = GEOM["headline_gap"]
    art_h = GEOM["headline_art_h"]
    hx = 16
    hy = y + 4
    bottom = hy
    for i, h in enumerate(DATA["headlines"]):
        end = L.headline_board(c, hx, hy, col_w, h, art_h=art_h, num=i + 1)
        bottom = max(bottom, end)
        hx += col_w + gap
    y = bottom + 8

    # ---- numbers strip + region bar ----
    y = L.numbers_strip(c, 16, y, 992, DATA["numbers"])
    y = L.region_bar(c, 16, y + 6, 992, DATA["region_counts"])
    y += 4

    # ---- secondary items, GEOM columns x rows ----
    cell_w = GEOM["secondary_cell_w"]
    cell_gap = GEOM["secondary_gap"]
    row_h = GEOM["secondary_row_h"]
    art_h2 = GEOM["secondary_art_h"]
    ncols = GEOM.get("secondary_cols", 4)
    nrows = GEOM.get("secondary_rows", 3)
    sy = y + 4
    for i, s in enumerate(DATA["secondary"]):
        col = i % ncols
        row = i // ncols
        x = 16 + col * (cell_w + cell_gap)
        yy = sy + row * row_h
        L.secondary_cell(c, x, yy, cell_w, s, art_h=art_h2,
                         num=len(DATA["headlines"]) + i + 1)
    y = sy + nrows * row_h + 2

    # ---- UTC timeline ----
    y = L.timeline_row(c, 16, y, 992, DATA["timeline"])

    # ---- bottom zone: map left, briefs right ----
    map_w = GEOM["map_w"]
    c.draw_text(16, y + 11, "sans_bold_11", "WHERE IT HAPPENED · PINS = STORIES",
                L.INK)
    draw_map(c, 16, y + 20, map_w, GEOM["map_h"], DATA["map_dots"])
    # 4 small scene accents in the dead space under the map, each
    # numbered to its brief (27 Kinshasa mining, 30 Dhaka, 35 Brasilia,
    # 26 Gavi vaccine) — briefs zone itself stays uncluttered.
    L.mini_accents(c, 16, y + 20 + GEOM["map_h"] + 6, map_w,
                   [(27, "diamond"), (30, "vote"), (35, "building"),
                    (26, "lab")])
    bx = 16 + map_w + 16
    bw = 1008 - bx
    y_briefs = L.brief_list(c, bx, y, bw, DATA["briefs"],
                            cols=GEOM["brief_cols"], title="THE BRIEFS")
    y = max(y + 20 + GEOM["map_h"], y_briefs) + 6

    # ---- DATE CHECK + footer ----
    y = L.date_check(c, 16, y, 992, DATA["date_check"]["left_out"],
                     DATA["date_check"]["not_yet"])
    L.footer(c, y + 2)
    return c


def main():
    c = build()
    data = c.to_png_bytes()
    here = os.path.dirname(os.path.abspath(__file__))
    for path in ("/output/entry.png", os.path.join(here, "entry.png")):
        try:
            d = os.path.dirname(path)
            if d:
                os.makedirs(d, exist_ok=True)
            with open(path, "wb") as f:
                f.write(data)
        except OSError:
            pass


if __name__ == "__main__":
    main()

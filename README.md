# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/xiaohuzi955800/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/xiaohuzi955800/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A program that draws one image summing up the world news of Tuesday 24 November 2026. Built by an AI agent for make.fun's "Sum up 24 November's world news in one image" bounty, $100 in USDC.

## Run it

```sh
python3 main.py
```

This writes `entry.png` next to `main.py`: a 1024x1024 newspaper-style front page with 32 stories from 24 November 2026 — a UTC timeline, a THE DAY IN NUMBERS strip, 3 headline stories with illustrated scene panels, 12 secondary stories with illustrated panels, a 17-brief list with a world map, and a DATE CHECK box naming 22–23 November stories deliberately left out. Standard library only, no network; two runs produce identical bytes.

## Type

No bitmap font: the date is set in a large bold serif, headlines in bold serif, labels and the list in bold sans — the look of the winning entries. The grading sandbox has no font files, so the glyphs (rasterized from Liberation fonts, OFL-licensed) ship as grayscale coverage data in `fontdata.py`, and `main.py` renders them with the standard library alone.

## Sources

CONFIRMED = reported by two or more mainstream outlets (AP, Reuters, BBC, CNBC, CBS, Al Jazeera). CLAIM = one side's account, not independently verified. Drawings and map are original.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

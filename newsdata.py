# Version A — balanced (3 leads + 12 pictures + 17 briefs = 32 items).
# All facts from news-research.md (24 Nov 2026, verified 25 Nov).
# Regions: Americas, Europe, Africa, Asia, Middle East, Latin America.
# No Oceania item could be verified for 24 Nov, so none is invented.

GEOM = {
    "headline_col_w": 322,
    "headline_gap": 13,
    "headline_art_h": 84,
    "secondary_cell_w": 240,
    "secondary_gap": 10,
    "secondary_row_h": 113,
    "secondary_art_h": 46,
    "secondary_cols": 4,
    "secondary_rows": 3,
    "map_w": 300,
    "map_h": 120,
    "brief_cols": 2,
}

DATA = {
    "date_title": "Tuesday 24 November 2026",
    "red_line": "Huawei convicted · Dow tops 50,000 · Gaza strike kills Hamas security chief",
    "overview": "32 STORIES · 6 REGIONS · 15 FIELDS · 3 LEADS · 12 PICTURES · 17 BRIEFS",

    "headlines": [
        {
            "scene": "court", "banner": "10 OF 12 COUNTS",
            "title": "Huawei convicted on 10 of 12 counts in New York",
            "summary": "Brooklyn jury finds bank fraud, sanctions breaches and trade-secret theft; cleared on racketeering.",
            "place": "NEW YORK · JUSTICE", "cred": "CONFIRMED · REUTERS",
            "geotag": "NEW YORK", "geotag_pos": "br",
            "region": "Americas", "field": "Justice",
        },
        {
            "scene": "chart", "banner": "DOW 50,000",
            "title": "Dow closes above 50,000 for the first time",
            "summary": "Dow +0.85% to 50,018.70 as money rotates out of tech; Nasdaq -1.48%. Nvidia -5.86%.",
            "place": "NEW YORK · MARKETS", "cred": "CONFIRMED · AP",
            "geotag": "NEW YORK", "geotag_pos": "tr",
            "region": "Americas", "field": "Markets",
        },
        {
            "scene": "flame", "banner": "CEASEFIRE UNDER STRAIN",
            "title": "Israel kills Hamas security chief in Gaza strike",
            "summary": "Naeem Abu Nahel killed in Gaza City; at least 6 dead. Meningitis alert: 272 cases in October.",
            "place": "GAZA CITY · WAR", "cred": "CONFIRMED · REUTERS",
            "geotag": "GAZA CITY", "geotag_pos": "br",
            "region": "Middle East", "field": "War",
        },
    ],

    "secondary": [
        {
            "scene": "tanker", "banner": "OIL WAR",
            "title": "Putin vows retaliation for refinery strikes",
            "summary": "Says Ukraine keeps hitting Russian refineries despite Trump's request to stop.",
            "data": "REFINING HIT", "cred": "CONFIRMED · REUTERS",
            "region": "Europe", "field": "War",
        },
        {
            "scene": "building", "banner": "NIGHT STRIKE",
            "title": "Russian strike on Zaporizhzhia kills 2, wounds 40",
            "summary": "Overnight attack hits an apartment block; four children among the wounded.",
            "data": "2 DEAD · 40 HURT", "cred": "CONFIRMED · AP",
            "region": "Europe", "field": "War",
        },
        {
            "scene": "plane", "banner": "JETS SCRAMBLED",
            "title": "Russian jets enter Korea's air defence zone",
            "summary": "Seoul scrambles fighters; rare air-raid alert on Ulleung Island. No airspace violated.",
            "data": "ULLEUNG ALERT", "cred": "CONFIRMED · AL JAZEERA",
            "region": "Asia", "field": "Military",
        },
        {
            "scene": "summit", "banner": "GRAFT PROBE",
            "title": "China investigates Shanghai party chief Chen Jining",
            "summary": "Politburo member probed for suspected severe violations; fourth since 2025.",
            "data": "4TH SINCE 2025", "cred": "CONFIRMED · REUTERS",
            "region": "Asia", "field": "Politics",
        },
        {
            "scene": "building", "banner": "$237.5B DEBT",
            "title": "Venezuela reveals $237.5bn debt mountain",
            "summary": "First full tally: 242% of GDP, groundwork for a giant sovereign restructuring.",
            "data": "242% OF GDP", "cred": "CONFIRMED · REUTERS",
            "region": "Latin America", "field": "Economy",
        },
        {
            "scene": "ship", "banner": "FUEL BLOCKADE",
            "title": "WHO chief urges US to lift Cuba fuel blockade",
            "summary": "Tedros warns children's lives at risk; WHO pledges $2m for vaccines and gear.",
            "data": "$2M PLEDGED", "cred": "CONFIRMED · REUTERS",
            "region": "Latin America", "field": "Health",
        },
        {
            "scene": "forest", "banner": "EBOLA DISRUPTED",
            "title": "Fighting traps Ebola teams in DR Congo",
            "summary": "Clashes near Ituri hospital force response teams to take cover for over 24 hours.",
            "data": "24H+ SHELTER", "cred": "CONFIRMED · UN",
            "region": "Africa", "field": "Health",
        },
        {
            "scene": "chip", "banner": "AI SELL-OFF",
            "title": "Nvidia slides 5.86%; Anthropic below IPO price",
            "summary": "A day after Huang's return sent shares up 31.5%, Nvidia falls to $155.38.",
            "data": "-5.86% · -6.54%", "cred": "CONFIRMED · INVESTOPEDIA",
            "region": "Americas", "field": "Markets",
        },
        {
            "scene": "market", "banner": "CONFIDENCE 103.3",
            "title": "US consumer confidence jumps to 103.3",
            "summary": "Up 11.4 points in November, highest since January 2025, far above forecast.",
            "data": "+11.4 PTS", "cred": "CONFIRMED · REUTERS",
            "region": "Americas", "field": "Economy",
        },
        {
            "scene": "lab", "banner": "CLAUDE SHIP",
            "title": "Anthropic launches Claude Ship code agents",
            "summary": "Three agents review pull requests, push fixes and approve merges by policy.",
            "data": "3 AGENTS", "cred": "CONFIRMED · ANTHROPIC",
            "region": "Americas", "field": "AI",
        },
        {
            "scene": "rocket", "banner": "FIRST FOREIGNER",
            "title": "China names Shenzhou-24 crew; Pakistani to visit Tiangong",
            "summary": "Muhammad Zeeshan Ali, 40, will be the first foreign astronaut aboard the station.",
            "data": "LAUNCH 25 NOV", "cred": "CONFIRMED · AP",
            "region": "Asia", "field": "Space",
        },
        {
            "scene": "trophy", "banner": "TITLE RESTORED",
            "title": "CAS hands Senegal back the Africa Cup title",
            "summary": "Court overturns CAF's decision to strip the crown after the walk-off final.",
            "data": "1-0 AET", "cred": "CONFIRMED · AP",
            "region": "Africa", "field": "Sport",
        },
    ],

    # (num, place, phrase, region, field)
    "briefs": [
        (16, "ODESA", "Russian strike kills 2, injures 3; drones hit Kyiv", "Europe", "War"),
        (17, "MOSCOW", "Mediazona puts Russian war dead near 700,000", "Europe", "War"),
        (18, "BERLIN", "Germany first to use Ukraine's Delta battlefield system", "Europe", "Military"),
        (19, "KYIV", "Zelenskyy says Ukraine needs $125bn in 2027", "Europe", "War"),
        (20, "WASHINGTON", "US debating strikes on Iran leaders, NBC reports", "Middle East", "War"),
        (21, "GAZA", "Board of Peace: Hamas agrees disarmament roadmap", "Middle East", "Diplomacy"),
        (22, "BAGHDAD", "PM orders state takeover of Kurdish-area oilfields", "Middle East", "Energy"),
        (23, "BRUSSELS", "NATO vows to defend space after Russia report", "Europe", "Military"),
        (24, "JERUSALEM", "US envoy doubts end to $3.8bn yearly Israel aid", "Middle East", "Diplomacy"),
        (25, "BUDAPEST", "Hungary opposes EUR 1.78tn EU budget plan", "Europe", "EU"),
        (26, "GENEVA", "Gavi plans up to 1.5m Ebola vaccine doses", "Africa", "Health"),
        (27, "WORLD", "Year's biggest supermoon, the beaver moon, lights sky", "Americas", "Science"),
        (28, "MADRID", "Real Madrid thrash PSV 5-1; Man City draw 2-2 Napoli", "Europe", "Sport"),
        (29, "GENEVA", "Gukesh, Sindarov draw game 1 of chess title match", "Europe", "Sport"),
        (30, "LONDON", "DeepMind: Gemini 4 agents cut quantum costs 290x", "Europe", "AI"),
        (31, "TEL AVIV", "Check Point servers breached in 16 countries, 24 hit", "Middle East", "Security"),
        (32, "NEW YORK", "Gold -2.70% to $3,552.80; WTI +1.82% to $81.63", "Americas", "Markets"),
    ],

    "numbers": [
        ("50,018.70", "DOW CLOSE"),
        ("-1.48%", "NASDAQ"),
        ("-5.86%", "NVIDIA"),
        ("$237.5B", "VENEZUELA DEBT"),
        ("103.3", "US CONFIDENCE"),
        ("272", "MENINGITIS CASES"),
    ],

    # Counted from the items above; sums to 32 (all items).  The supermoon
    # brief is worldwide; it is counted under Americas only so the bar
    # still adds up — no region is invented for it.
    "region_counts": {
        "Americas": 7, "Europe": 11, "Africa": 3, "Asia": 3,
        "Middle East": 6, "Latin America": 2,
    },

    "timeline": [
        ("~00:30", "Zaporizhzhia hit"),
        ("~02:00", "Shenzhou crew named"),
        ("~06:30", "Meningitis alert"),
        ("~13:00", "Chen probed"),
        ("~15:30", "Senegal title back"),
        ("~19:30", "Huawei convicted"),
        ("21:00", "Dow tops 50,000"),
    ],

    # (lon, lat, story number, region colour)
    "map_dots": [
        (-74.0, 40.7, 1, (30, 90, 160)),
        (34.5, 31.5, 3, (120, 60, 160)),
        (37.6, 55.8, 4, (200, 120, 20)),
        (35.2, 47.8, 5, (200, 120, 20)),
        (127.0, 37.5, 6, (30, 140, 90)),
        (121.5, 31.2, 7, (30, 140, 90)),
        (-66.9, 10.5, 8, (200, 60, 60)),
        (-82.4, 23.1, 9, (200, 60, 60)),
        (29.5, 1.5, 10, (160, 40, 90)),
        (98.5, 39.7, 14, (30, 140, 90)),
        (-17.4, 14.7, 15, (160, 40, 90)),
    ],

    "date_check": {
        "left_out": [
            "23 Nov — Nvidia reinstates Huang; shares +31%",
            "23 Nov — Trump orders faster federal executions",
            "22 Nov — COP31 ends with no climate pact",
            "23 Nov — Ukraine sinks Russian corvette off Benghazi",
            "22–23 Nov — Strikes around Kyiv kill at least 15",
            "23 Nov — Indonesia factory fire kills 24",
            "22–23 Nov — Korea education minister quits",
            "23 Nov — Pope draws 2.5m to Mass in Buenos Aires",
        ],
        "not_yet": [
            "25 Nov 08:18 — Shenzhou-24 launches",
            "26–27 Nov — EU summit on EUR 1.78tn budget",
        ],
    },

    "footer_left": "HOW SURE:  CONFIRMED = 2+ outlets   ·   CLAIM = one side's account",
}

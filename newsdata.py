# Version B — high density (3 leads + 12 pictures + 24 briefs = 39 items).
# Same headlines and secondary stories as A; secondary summaries cut to
# one line each and headline art slightly shorter to fit 24 briefs.
# All facts from news-research.md (24 Nov 2026, verified 25 Nov).

GEOM = {
    "headline_col_w": 322,
    "headline_gap": 13,
    "headline_art_h": 78,
    "secondary_cell_w": 240,
    "secondary_gap": 10,
    "secondary_row_h": 101,
    "secondary_art_h": 46,
    "secondary_cols": 4,
    "secondary_rows": 3,
    "map_w": 250,
    "map_h": 120,
    "brief_cols": 2,
}

DATA = {
    "date_title": "Tuesday 24 November 2026",
    "red_line": "Huawei convicted · Dow tops 50,000 · Gaza strike kills Hamas security chief",
    "overview": "39 STORIES · 8 REGIONS · 16 FIELDS · 3 LEADS · 12 PICTURES · 24 BRIEFS",

    "headlines": [
        {
            "scene": "court", "banner": "10 OF 12 COUNTS",
            "title": "Huawei convicted on 10 of 12 counts in New York",
            "summary": "Brooklyn jury finds bank fraud, sanctions breaches and trade-secret theft; cleared on racketeering.",
            "place": "NEW YORK · JUSTICE", "cred": "CONFIRMED · REUTERS",
            "geotag": "NEW YORK", "geotag_pos": "br",
            "region": "North America", "field": "Justice",
        },
        {
            "scene": "chart", "banner": "DOW 50,000",
            "title": "Dow closes above 50,000 for the first time",
            "summary": "Dow +0.85% to 50,018.70 as money rotates out of tech; Nasdaq -1.48%. Nvidia -5.86%.",
            "place": "NEW YORK · MARKETS", "cred": "CONFIRMED · AP",
            "geotag": "NEW YORK", "geotag_pos": "tr",
            "region": "North America", "field": "Markets",
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
            "scene": "refinery", "banner": "OIL WAR",
            "title": "Putin vows retaliation for refinery strikes",
            "summary": "Vows payback for strikes on Russian refineries.",
            "data": "REFINING HIT", "cred": "CONFIRMED · REUTERS",
            "region": "Europe", "field": "War",
        },
        {
            "scene": "strike", "banner": "NIGHT STRIKE",
            "title": "Russian strike on Zaporizhzhia kills 2, wounds 40",
            "summary": "Overnight hit on flats; four children wounded.",
            "data": "2 DEAD · 40 HURT", "cred": "CONFIRMED · AP",
            "region": "Europe", "field": "War",
        },
        {
            "scene": "jets", "banner": "JETS SCRAMBLED",
            "title": "Russian jets enter Korea's air defence zone",
            "summary": "Seoul scrambles jets; rare Ulleung Island alert.",
            "data": "ULLEUNG ALERT", "cred": "CONFIRMED · AL JAZEERA",
            "region": "East Asia", "field": "Military",
        },
        {
            "scene": "court", "banner": "GRAFT PROBE",
            "title": "China investigates Shanghai party chief Chen Jining",
            "summary": "Politburo member probed; fourth since 2025.",
            "data": "4TH SINCE 2025", "cred": "CONFIRMED · REUTERS",
            "region": "East Asia", "field": "Politics",
        },
        {
            "scene": "debt", "banner": "$237.5B DEBT",
            "title": "Venezuela reveals $237.5bn debt mountain",
            "summary": "First tally: 242% of GDP; giant restructuring.",
            "data": "242% OF GDP", "cred": "CONFIRMED · REUTERS",
            "region": "Latin America", "field": "Economy",
        },
        {
            "scene": "fuel", "banner": "FUEL BLOCKADE",
            "title": "WHO chief urges US to lift Cuba fuel blockade",
            "summary": "WHO pledges $2m; children's lives at risk.",
            "data": "$2M PLEDGED", "cred": "CONFIRMED · REUTERS",
            "region": "Latin America", "field": "Health",
        },
        {
            "scene": "clinic", "banner": "EBOLA DISRUPTED",
            "title": "Fighting traps Ebola teams in DR Congo",
            "summary": "Clashes near Ituri hospital; teams shelter 24h+.",
            "data": "24H+ SHELTER", "cred": "CONFIRMED · UN",
            "region": "Africa", "field": "Health",
        },
        {
            "scene": "chip", "banner": "AI SELL-OFF",
            "title": "Nvidia slides 5.86%; Anthropic below IPO price",
            "summary": "A day after +31.5% surge, Nvidia falls to $155.38.",
            "data": "-5.86% · -6.54%", "cred": "CONFIRMED · INVESTOPEDIA",
            "region": "North America", "field": "Markets",
        },
        {
            "scene": "shop", "banner": "CONFIDENCE 103.3",
            "title": "US consumer confidence jumps to 103.3",
            "summary": "Up 11.4 points; highest since January 2025.",
            "data": "+11.4 PTS", "cred": "CONFIRMED · REUTERS",
            "region": "North America", "field": "Economy",
        },
        {
            "scene": "code", "banner": "CLAUDE SHIP",
            "title": "Anthropic launches Claude Ship code agents",
            "summary": "Three agents review, fix and approve merges.",
            "data": "3 AGENTS", "cred": "CONFIRMED · ANTHROPIC",
            "region": "North America", "field": "AI",
        },
        {
            "scene": "rocket", "banner": "FIRST FOREIGNER",
            "title": "China names Shenzhou-24 crew; Pakistani to visit Tiangong",
            "summary": "Ali, 40, first foreign astronaut aboard Tiangong.",
            "data": "LAUNCH 25 NOV", "cred": "CONFIRMED · AP",
            "region": "East Asia", "field": "Space",
        },
        {
            "scene": "trophy", "banner": "TITLE RESTORED",
            "title": "CAS hands Senegal back the Africa Cup title",
            "summary": "Court overturns CAF's decision to strip crown.",
            "data": "1-0 AET", "cred": "CONFIRMED · AP",
            "region": "Africa", "field": "Sport",
        },
    ],

    # (num, place, phrase, region, field)
    "briefs": [
        (16, "ODESA", "Russian strike kills 2, injures 3; drones hit Kyiv", "Europe", "War"),
        (17, "MOSCOW", "Mediazona estimates Russian war dead near 700,000", "Europe", "War"),
        (18, "BERLIN", "Germany first to access Ukraine Delta system, Kyiv says", "Europe", "Military"),
        (19, "KYIV", "Zelenskyy says Ukraine needs $125bn in 2027", "Europe", "War"),
        (20, "WASHINGTON", "US debating strikes on Iran's leaders, NBC reports", "Middle East", "War"),
        (21, "GAZA", "Board of Peace says Hamas agrees disarmament roadmap", "Middle East", "Diplomacy"),
        (22, "BAGHDAD", "PM orders state takeover of Kurdish-area oilfields", "Middle East", "Energy"),
        (23, "BRUSSELS", "NATO vows to defend space after Russia satellite report", "Europe", "Military"),
        (24, "JERUSALEM", "US envoy doubts end to $3.8bn yearly Israel aid", "Middle East", "Diplomacy"),
        (25, "BUDAPEST", "Hungary opposes EUR 1.78tn EU budget, reports say", "Europe", "EU"),
        (26, "GENEVA", "Gavi plans up to 1.5m Ebola vaccine doses", "Africa", "Health"),
        (27, "KINSHASA", "DR Congo orders foreign miners to open units to locals", "Africa", "Mining"),
        (28, "MADRID", "Real Madrid thrash PSV 5-1; Man City draw 2-2 Napoli", "Europe", "Sport"),
        (29, "GENEVA", "Gukesh and Sindarov draw game 1 of chess title match", "Europe", "Sport"),
        (30, "DHAKA", "Hasina plans Dec 16 return; 101 platoons deployed", "South Asia", "Politics"),
        (31, "TEL AVIV", "Researchers: 24 Check Point servers hit in 16 nations", "Middle East", "Security"),
        (32, "NEW YORK", "Gold -2.70% to $3,552.80; WTI oil +1.82% to $81.63", "North America", "Markets"),
        (33, "BERLIN", "German Ifo business climate rises to 90.6", "Europe", "Economy"),
        (34, "SAN FRANCISCO", "Claude 'proved VP-VNP', Anthropic says", "North America", "AI"),
        (35, "BRASILIA", "Lula signs fiscal law capping spending growth at 2%", "Latin America", "Economy"),
        (36, "LONDON", "Meta's Muse agent launches in the UK", "Europe", "AI"),
        (37, "BHOPAL", "India women beat China 6-2 in hockey", "South Asia", "Sport"),
        (38, "INDIA", "Teen Sooryavanshi smashes 204 off 53 balls", "South Asia", "Sport"),
        (39, "HANOI", "Reports: restaurant blast kills at least 6, injures 10", "Southeast Asia", "Accident"),
    ],

    "numbers": [
        ("50,018.70", "DOW CLOSE"),
        ("-1.48%", "NASDAQ"),
        ("-5.86%", "NVIDIA"),
        ("$237.5B", "VENEZUELA DEBT"),
        ("103.3", "US CONFIDENCE"),
        ("272", "MENINGITIS CASES"),
    ],

    "region_counts": {
        "North America": 7, "Europe": 12, "Africa": 4, "East Asia": 3,
        "Middle East": 6, "Latin America": 3, "South Asia": 3,
        "Southeast Asia": 1,
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

    "map_dots": [
        (-74.0, 40.7, 1, (30, 90, 160)),
        (34.5, 31.5, 3, (120, 60, 160)),
        (37.6, 55.8, 4, (200, 120, 20)),
        (121.5, 31.2, 7, (30, 140, 90)),
        (-66.9, 10.5, 8, (200, 60, 60)),
        (-82.4, 23.1, 9, (200, 60, 60)),
        (98.5, 39.7, 14, (30, 140, 90)),
        (-17.4, 14.7, 15, (160, 40, 90)),
        (15.3, -4.3, 27, (160, 40, 90)),
        (90.4, 23.8, 30, (200, 80, 160)),
        (-47.9, -15.8, 35, (200, 60, 60)),
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

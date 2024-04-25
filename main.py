#!/usr/bin/env python

import json
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://osu.ppy.sh/beatmaps/artists"
OUTPUT_FILE = Path("input/data/result.json")
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z"


response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

# with open("debug.html", "w") as f:
#     f.write(response.content.decode())

songs_count = 0
entries = soup.find_all("div", class_="artist__track-count")

for div in entries:
    count = div.text.strip().split()[0]
    count = int(count)
    songs_count += count

with OUTPUT_FILE.open("w") as f:
    result = {
        "songs_count": songs_count,
        "artists_count": len(entries),
        "last_update": datetime.now(timezone.utc).strftime(DATE_FORMAT),
    }
    json.dump(result, f)

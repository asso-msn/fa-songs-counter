#!/usr/bin/env python

import json
from datetime import datetime
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

total = 0

for div in soup.find_all("div", class_="artist__track-count"):
    count = div.text.strip().split()[0]
    count = int(count)
    total += count

with OUTPUT_FILE.open("w") as f:
    result = {
        "count": total,
        "last_update": datetime.now().strftime(DATE_FORMAT),
    }
    json.dump(result, f)

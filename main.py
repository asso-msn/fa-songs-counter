#!/usr/bin/env python

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://osu.ppy.sh/beatmaps/artists"
OUTPUT_FILE = Path("input/data/result.json")


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
    json.dump({"count": total}, f)

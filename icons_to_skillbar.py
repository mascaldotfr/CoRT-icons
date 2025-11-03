#!/usr/bin/env python3

import json
import os
import sys

from PIL import Image

baseicons = "./original_skills_icons"
icon_target = 48 # width of a wanted icon

if len(sys.argv) == 1:
    print("Usage: icon_to_skillbar CoRT/data/version/trainerdata.json")
    print("Icon skillbars will be generated in the 'icons' subdirectory ")
    print("of the given trainerdata.json.")
    sys.exit(1)

data = None
with open(sys.argv[1], "r") as jsonfile:
    data = json.load(jsonfile)

target_skillbars = os.path.dirname(sys.argv[1]) + f"/icons"
os.makedirs(target_skillbars, exist_ok=True)
for discipline in data["disciplines"]:
    skillbar = Image.new("RGBA", (icon_target * 11, icon_target))
    offset = 1

    if discipline.endswith("WM"):
        img = Image.open(f"{baseicons}/WM.png")
    else:
        img = Image.open(f"{baseicons}/{discipline}.png")
    img_resized = img.resize((icon_target - 1, icon_target),
                             resample=Image.LANCZOS)
    skillbar.paste(img_resized, (offset, 0), mask=img_resized.split()[3])

    for skill in data["disciplines"][discipline]["spells"]:
        offset += icon_target
        if skill["name"].startswith("undefined"):
            continue
        img = Image.open(f'{baseicons}/{skill["name"]}.png')
        img_resized = img.resize((icon_target - 1, icon_target),
                                 resample=Image.LANCZOS)
        skillbar.paste(img_resized, (offset, 0))

    destfile = f"{target_skillbars}/{discipline.replace(' ','')}.webp"
    skillbar.convert("RGB").save(destfile, quality=60)
    print("Created", destfile)

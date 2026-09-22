import json
from pathlib import Path

input_file = Path(__file__).parent / "Week_6_statistics.json"

with open(input_file, "r") as f:
    data = json.load(f)
    print(data)
    print(data["name"])
    print(data["statistics"]["height"])
    print(data["statistics"]["age"])
    for person in data["other data"]:
        print(f"{person['name']}: {person['height']} ft, {person['age']} years old")
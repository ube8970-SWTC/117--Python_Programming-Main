import json
from pathlib import Path

with open("Json_test.json", "r") as file:
    data = json.load(file)

for person in data:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

output_path = Path(__file__).parent / "output_test.txt"
with open(output_path, "w") as file:
    for person in data:
        file.write(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}\n")

from pathlib import Path

input_path = Path(__file__).parent / "input_test.txt"

with open(input_path, "r") as file:
    lines = file.readlines()

print("Lines read from input_test.txt:")
for line in lines:
    print(line.strip())

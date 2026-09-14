import sys
from pathlib import Path

folder = Path(sys.argv[1])
base_name = input("Enter base name: ")
counter = 1

raw = input("Enter extensions (comma separated): ")

is_allowed = raw.split(",")
cleaned = [ext.strip() for ext in is_allowed]


for item in folder.iterdir():
    if not item.is_file():
        continue

    if item.suffix.lower() in cleaned:
        new_name = (f"{base_name}_{counter:03d}{item.suffix}")
        file_name = folder / new_name

        try:
            item.rename(file_name)
        except FileExistsError:
            print(f"Skipped {file_name}: already Exists. ") 
        counter +=1
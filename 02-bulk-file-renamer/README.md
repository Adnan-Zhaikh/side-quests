# 02 - Bulk File Renamer

Renames files in a folder to a base name + sequential number, filtered by user-chosen extensions.

## Usage
python renamer.py <folder_path>
(prompts for base name and allowed extensions at runtime)

## What I learned
- f-string number formatting: {counter:03d} for zero-padded numbers
- input() for runtime user prompts
- str.split(",") to turn one string into a list
- List comprehension: [x.strip() for x in list] to clean whitespace from every item
- Filtering with `in` against a list
- try/except FileExistsError for rename collisions

## Notes
- Extensions are entered comma-separated at runtime, e.g. ".jpg, .png"
- Files with extensions not in the list are left untouched
- Counter is global across the whole folder, not per-extension
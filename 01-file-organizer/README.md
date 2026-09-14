# 01 - File Extension Organizer

Sorts files in a folder into subfolders by extension (Images, Documents, etc.)

## Usage
python organizer.py <folder_path>

## What I learned
- pathlib: Path, iterdir(), suffix, name, mkdir(exist_ok=True)
- sys.argv for command-line input
- dict.get() with fallback for unmapped extensions
- try/except for handling FileExistsError on collisions

## Notes
- Unmatched extensions go into an "Others" folder
- Files with no extension are treated as empty string suffix → also go to "Others"
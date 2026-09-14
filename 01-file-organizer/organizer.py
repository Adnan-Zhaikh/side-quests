import sys
from pathlib import Path

folder = Path(sys.argv[1])
extension_map = { 
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"], 
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"], 
    "Videos": [".mp4", ".mkv", ".avi", ".mov"], 
    "Audio": [".mp3", ".wav", ".flac", ".aac"], 
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],  
    }

for item in folder.iterdir():
    if not item.is_file():
        continue
    
    exten = item.suffix.lower()
    category = extension_map.get(exten, "Others")

    sub = folder / category
    sub.mkdir(exist_ok=True)
    try:
        item.rename(sub / item.name)
    except FileExistsError:
        print(f"Skipped {item.name}: already exists in {category}")
    
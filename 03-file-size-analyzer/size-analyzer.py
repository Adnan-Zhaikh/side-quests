from pathlib import Path
import sys

def byteConvert(b):
    if b >= 1024**3:
        return(f"{b / 1024**3:.2f} GB")
    elif b >= 1024**2:
        return(f"{b / 1024**2:.2f} MB")
    elif b >= 1024:
        return(f"{b / 1024:.2f} KB")
    else:
        return(f"{b} bytes")

folder = Path(sys.argv[1])

for item in folder.iterdir():
    if not item.is_file():
        continue

    size = byteConvert(item.stat().st_size)

    print(f"{item.stem:<20} {size}")
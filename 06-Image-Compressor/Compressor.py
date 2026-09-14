from pathlib import Path
from PIL import Image
import sys


img = Image.open(sys.argv[1])

quality = 95

target = int(input("Enter the Compression size: "))

target_bytes = target * 1024

def byteConvert(b):
    if b >= 1024**3:
        return(f"{b / 1024**3:.2f} GB")
    elif b >= 1024**2:
        return(f"{b / 1024**2:.2f} MB")
    elif b >= 1024:
        return(f"{b / 1024:.2f} KB")
    else:
        return(f"{b} bytes")

while quality > 10:
    img.save("Compressed.jpg", quality=quality)
    size = Path("Compressed.jpg").stat().st_size
    s = byteConvert(size)
    if size < target_bytes:
        print(f"Your File is Compressed to: {s}")
        break
    quality -= 10
else:
    print("Could not reach target size. Closest attempt saved.")



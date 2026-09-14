import sys
from PIL import Image


img = Image.open(sys.argv[1])
og_wid, og_height = img.size

desired_wid = int(input("Enter a Width to change: "))

new_height = desired_wid * ( og_height / og_wid)

resized = img.resize((desired_wid, int(new_height)))

resized.save("outp.jpg")
out = Image.open("outp.jpg").size

print(f"The Image Size after Compression is: {out}")

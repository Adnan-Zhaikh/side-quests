# 05 - Image Converter

Converts images between formats (jpg/png/webp), handling transparency correctly.

## Usage (GUI)
python converter_gui.py

## What I learned
- Pillow infers output format from the file extension you .save() to
- RGBA vs RGB: JPEG can't store an alpha (transparency) channel — errors with "cannot write mode RGBA as JPEG"
- Image.new("RGB", size, "white") to create a blank background
- img.split() to unpack RGBA into separate R, G, B, A channel images
- .paste(img, (0,0), mask) — pastes using alpha as a mask so only transparent areas get filled
- Only JPEG needs the white-background flatten — PNG/WebP support alpha natively
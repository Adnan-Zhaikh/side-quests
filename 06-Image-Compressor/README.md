# 06 - Image Compressor

Compresses an image toward a target file size by stepping JPEG quality down until it fits (or gives up gracefully).

## Usage (CLI)
python compressor.py <image_path>
(prompts for target size in KB)

## Usage (GUI)
python compressor_gui.py

## What I learned
- .save(path, quality=N) — JPEG quality param (0-100), lossy compression
- while loop — used when the number of attempts isn't known in advance (unlike for)
- Unit mismatch bug: comparing a KB target against a byte-based size — had to convert to matching units
- Reused byteConvert() from quest 3 for human-readable output
- while/else: the else block runs only if the loop finishes WITHOUT hitting break — used to detect "target never reached" instead of failing silently
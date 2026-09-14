# 04 - Image Resizer

Resizes an image to a given width, preserving aspect ratio. CLI version built by hand; GUI version (tkinter) built with AI help since I chose not to learn tkinter right now.

## Usage (CLI)
python resizer.py <image_path>
(prompts for desired width)

## Usage (GUI)
python resizer_gui.py

## What I learned
- PIL.Image: .open(), .size (tuple), .resize(), .save()
- Tuple unpacking: og_width, og_height = img.size
- Aspect ratio math: new_height = new_width * (og_height / og_width)
- int() conversion — .resize() needs whole pixels, not floats
- GUI logic (resize math) reused from CLI, just wrapped in tkinter buttons/dialogs
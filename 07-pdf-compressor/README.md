# 07 - PDF Compressor

Shrinks a PDF toward a target size by recompressing every embedded image inside it.

## Usage (GUI)
python pdf_compressor_gui.py
(pick target size + unit: KB / MB / GB)

## What I learned
- pypdf's PdfReader vs PdfWriter — you never edit the original in place, you build a new PdfWriter from it and save that
- page.images returns real Pillow Image objects — same tools from quest 6 apply directly
- img.replace(image, quality=N) swaps a recompressed image back into the page
- Must loop over writer.pages (not reader.pages) when calling .replace() — .replace() only works on the writer's copy
- Nested loop: outer loop over every page, inner loop over that page's images
- Diminishing returns: an already-compressed PDF (previously shrunk 43MB -> 712KB) won't shrink much further — image quality isn't the only thing taking up space in a PDF
- Reused the while-loop quality-stepping pattern from quest 6, now with a KB/MB/GB unit dropdown instead of KB only
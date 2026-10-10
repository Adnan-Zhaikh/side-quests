# Side Quests

A growing collection of small, useful Python scripts. Each one is a "quest": one real problem, solved in one script, and one new set of concepts learned along the way.

**7 quests done so far, and more on the way.**

## Why this repo exists

I wanted to learn Python by building things I'd actually use, not by following tutorials. Every script here started as a small annoyance (messy download folders, huge image files, PDFs too big to email) and ended as a tool I can run. The repo is also a record of how my Python is improving, one script at a time.

## The quests

| # | Script | What it does | What I learned |
| --- | --- | --- | --- |
| 1 | **File organizer** | Sorts files into folders by extension | `pathlib`, `sys.argv`, dictionaries with `.get()` fallbacks, `mkdir(exist_ok=True)`, handling `FileExistsError` |
| 2 | **Bulk renamer** | Renames many files at once with numbered names | zero-padded counters, `input()`, parsing comma-separated input with `.split()` and `.strip()`, handling rename collisions |
| 3 | **File size analyzer** | Shows file sizes in readable units | `Path.stat().st_size`, converting bytes to KB/MB/GB with powers of 1024, `return` vs `print` |
| 4 | **Image resizer** | Resizes an image and keeps its aspect ratio | Pillow basics (`open`, `resize`, `save`), tuple unpacking, aspect-ratio math |
| 5 | **Image converter** | Converts between image formats, handling transparency | alpha channels (RGBA), flattening transparency onto a white background when saving as JPEG |
| 6 | **Image compressor** | Compresses an image to hit a target file size | JPEG `quality`, `while` loops for unknown retries, `while`/`else` for unreachable targets, debugging unit mismatches |
| 7 | **PDF compressor** | Shrinks a PDF by recompressing its images | `pypdf`, recompressing images inside pages, nested loops, and reading a real error message (iterating `reader.pages` vs `writer.pages`) |

Quests 4 to 7 also have a small desktop GUI wrapper so they're easier to use than the command line.

## Try the web version

Quests 3 to 7 became a browser app that runs entirely on your device: **[ShrunkPy](https://adnan-zhaikh.github.io/ShrunkPy/)**. The organizer and renamer aren't included there, because a web page can't move or rename files on your computer.

## Run a script

Requirements: Python 3.

```bash
git clone https://github.com/Adnan-Zhaikh/side-quests.git
cd side-quests
pip install Pillow pypdf
```

<!-- Add one real example command per script, for example:
python file_organizer.py ~/Downloads -->

Run each script from the terminal. The image and PDF scripts need `Pillow` and `pypdf`; the others use only the standard library.

## How I built these

I wrote the command-line versions myself, step by step, working out each concept before moving on. The tkinter GUI wrappers and the ShrunkPy web app were built with AI help, since my goal was to learn Python fundamentals, not GUI programming. I'm keeping that line clear on purpose: I only push code I understand.

## Roadmap

New quests get added whenever I run into a problem worth scripting. Ideas so far:

- [ ] Duplicate file finder
- [ ] ZIP utility
- [ ] CSV to JSON converter
- [ ] Eventually, a universal file utility CLI that combines the quests

## Author

**Adnan** — [@Adnan-Zhaikh](https://github.com/Adnan-Zhaikh)

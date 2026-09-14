# 03 - File Size Analyzer

Lists every file in a folder with its size in human-readable KB/MB/GB.

## Usage
python analyzer.py <folder_path>

## What I learned
- Path.stat().st_size for raw byte count
- Byte → KB/MB/GB conversion using powers of 1024
- Why if/elif chains must check largest unit first (or smaller thresholds "steal" the match)
- return vs print inside a function — print shows output, return actually hands the value back to the caller
- f-string number formatting: {value:.2f} for 2 decimal places

## Notes
- Columns aren't aligned (works fine for now since filenames were similar length; could add f"{name:<20}" later for general use)
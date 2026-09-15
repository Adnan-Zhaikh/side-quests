import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from pypdf import PdfReader, PdfWriter

selected_path = None

UNIT_MULTIPLIERS = {"KB": 1024, "MB": 1024**2, "GB": 1024**3}


def byteConvert(b):
    if b >= 1024**3:
        return f"{b / 1024**3:.2f} GB"
    elif b >= 1024**2:
        return f"{b / 1024**2:.2f} MB"
    elif b >= 1024:
        return f"{b / 1024:.2f} KB"
    else:
        return f"{b} bytes"


def pick_file():
    global selected_path
    selected_path = filedialog.askopenfilename(
        title="Select a PDF",
        filetypes=[("PDF files", "*.pdf")]
    )
    if selected_path:
        file_label.config(text=selected_path.split("/")[-1])
        original_size = Path(selected_path).stat().st_size
        original_label.config(text=f"Original size: {byteConvert(original_size)}")


def compress_pdf():
    if not selected_path:
        messagebox.showerror("No file", "Pick a PDF first.")
        return

    try:
        target_value = float(target_entry.get())
    except ValueError:
        messagebox.showerror("Invalid target", "Enter a number for the target size.")
        return

    unit = unit_var.get()
    target_bytes = target_value * UNIT_MULTIPLIERS[unit]

    save_path = filedialog.asksaveasfilename(
        title="Save compressed PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")]
    )
    if not save_path:
        return

    try:
        reader = PdfReader(selected_path)
        original_size = Path(selected_path).stat().st_size

        quality = 95
        final_size = None
        image_count = 0

        while quality > 10:
            writer = PdfWriter()
            writer.append(reader)

            image_count = 0
            for page in writer.pages:
                for img in page.images:
                    img.replace(img.image, quality=quality)
                    image_count += 1

            writer.write(save_path)
            size = Path(save_path).stat().st_size

            if size < target_bytes:
                final_size = size
                break
            quality -= 10
        else:
            final_size = Path(save_path).stat().st_size

        if final_size < target_bytes:
            messagebox.showinfo(
                "Done",
                f"Compressed {image_count} image(s) across {len(reader.pages)} page(s)\n"
                f"{byteConvert(original_size)} -> {byteConvert(final_size)} (quality={quality})"
            )
        else:
            messagebox.showwarning(
                "Target not reached",
                f"Could not reach {target_value} {unit}.\n"
                f"Closest: {byteConvert(final_size)} (quality={quality})"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Could not process this PDF:\n{e}")


root = tk.Tk()
root.title("PDF Compressor")
root.geometry("340x280")

tk.Button(root, text="Choose PDF", command=pick_file).pack(pady=10)
file_label = tk.Label(root, text="No file selected")
file_label.pack()
original_label = tk.Label(root, text="")
original_label.pack()

tk.Label(root, text="Target size:").pack(pady=(15, 0))

target_frame = tk.Frame(root)
target_frame.pack()
target_entry = tk.Entry(target_frame, width=10)
target_entry.insert(0, "500")
target_entry.pack(side=tk.LEFT, padx=(0, 6))

unit_var = tk.StringVar(value="KB")
tk.OptionMenu(target_frame, unit_var, "KB", "MB", "GB").pack(side=tk.LEFT)

tk.Button(root, text="Compress & Save", command=compress_pdf).pack(pady=15)

root.mainloop()
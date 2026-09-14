import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image

selected_path = None


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
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")]
    )
    if selected_path:
        file_label.config(text=selected_path.split("/")[-1])


def compress_image():
    if not selected_path:
        messagebox.showerror("No file", "Pick an image first.")
        return

    try:
        target_kb = int(target_entry.get())
    except ValueError:
        messagebox.showerror("Invalid target", "Enter a whole number of KB.")
        return

    target_bytes = target_kb * 1024

    save_path = filedialog.asksaveasfilename(
        title="Save compressed image as",
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg")]
    )
    if not save_path:
        return

    img = Image.open(selected_path).convert("RGB")
    quality = 95
    final_size = None

    while quality > 10:
        img.save(save_path, quality=quality)
        size = Path(save_path).stat().st_size
        if size < target_bytes:
            final_size = size
            break
        quality -= 10
    else:
        final_size = Path(save_path).stat().st_size

    if final_size == size and size < target_bytes:
        messagebox.showinfo("Done", f"Compressed to {byteConvert(final_size)} (quality={quality})")
    else:
        messagebox.showwarning(
            "Target not reached",
            f"Could not reach {target_kb} KB.\nClosest: {byteConvert(final_size)} (quality={quality})"
        )


root = tk.Tk()
root.title("Image Compressor")
root.geometry("320x220")

tk.Button(root, text="Choose Image", command=pick_file).pack(pady=10)
file_label = tk.Label(root, text="No file selected")
file_label.pack()

tk.Label(root, text="Target size (KB):").pack(pady=(10, 0))
target_entry = tk.Entry(root)
target_entry.pack()

tk.Button(root, text="Compress & Save", command=compress_image).pack(pady=15)

root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

selected_path = None


def pick_file():
    global selected_path
    selected_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    if selected_path:
        file_label.config(text=selected_path.split("/")[-1])


def convert_image():
    if not selected_path:
        messagebox.showerror("No file", "Pick an image first.")
        return

    target_format = format_var.get().lower()

    img = Image.open(selected_path)

    save_path = filedialog.asksaveasfilename(
        title="Save converted image as",
        defaultextension=f".{target_format}",
        filetypes=[(target_format.upper(), f"*.{target_format}")]
    )
    if not save_path:
        return

    if img.mode == "RGBA" and target_format == "jpg":
        bg = Image.new("RGB", img.size, "white")
        r, g, b, a = img.split()
        bg.paste(img, (0, 0), a)
        bg.save(save_path)
    else:
        img.save(save_path)

    messagebox.showinfo("Done", f"Saved: {save_path}")


root = tk.Tk()
root.title("Image Converter")
root.geometry("320x200")

tk.Button(root, text="Choose Image", command=pick_file).pack(pady=10)
file_label = tk.Label(root, text="No file selected")
file_label.pack()

tk.Label(root, text="Convert to:").pack(pady=(10, 0))
format_var = tk.StringVar(value="jpg")
tk.OptionMenu(root, format_var, "jpg", "png", "webp").pack()

tk.Button(root, text="Convert & Save", command=convert_image).pack(pady=15)

root.mainloop()
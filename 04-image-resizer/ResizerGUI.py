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


def resize_image():
    if not selected_path:
        messagebox.showerror("No file", "Pick an image first.")
        return

    try:
        desired_width = int(width_entry.get())
    except ValueError:
        messagebox.showerror("Invalid width", "Width must be a whole number.")
        return

    img = Image.open(selected_path)
    og_width, og_height = img.size
    new_height = int(desired_width * (og_height / og_width))

    resized = img.resize((desired_width, new_height))

    save_path = filedialog.asksaveasfilename(
        title="Save resized image as",
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
    )
    if not save_path:
        return

    resized.save(save_path)
    messagebox.showinfo("Done", f"Saved: {desired_width}x{new_height}\n{save_path}")


root = tk.Tk()
root.title("Image Resizer")
root.geometry("320x180")

tk.Button(root, text="Choose Image", command=pick_file).pack(pady=10)
file_label = tk.Label(root, text="No file selected")
file_label.pack()

tk.Label(root, text="Desired width (px):").pack(pady=(10, 0))
width_entry = tk.Entry(root)
width_entry.pack()

tk.Button(root, text="Resize & Save", command=resize_image).pack(pady=15)

root.mainloop()
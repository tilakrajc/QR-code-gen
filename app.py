import qrcode
import tkinter as tk

# Create a window
window = tk.Tk()
window.title("QRCode Generator")
window.geometry("200x100")

# Create a label
label = tk.Label(window, text="Enter text to generate QRCode")
label.grid(column=0, row=0)

# Create a text box
text_box = tk.Entry(window, width=20)
text_box.grid(column=0, row=1)

# Create a button
button = tk.Button(window, text="Generate QRCode")
button.grid(column=0, row=2)

# Create a label
label = tk.Label(window, text="QRCode will be saved as qrcode.png")
label.grid(column=0, row=3)

# Create a function to generate qrcode

def generate_qr(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Create a function to get text from text box and generate qrcode
def get_text():
    text = text_box.get()
    filename = "qrcode.png"
    generate_qr(text, filename)
    print(f"QRCode generated successfully and saved as {filename}.")
    text_box.delete(0, tk.END)

# Add button click event
button.config(command=get_text)

# Run the window
window.mainloop()
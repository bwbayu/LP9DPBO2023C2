from tkinter import Tk, Label, Button, Frame
from PIL import ImageTk, Image

def open_next_page():
    root.withdraw()  # Hide the current window
    # Add code to open the next page here

root = Tk()
root.title("Praktikum DPBO Python")

# Create a label "Halo, selamat datang"
label = Label(root, text="Halo, selamat datang", font=("Helvetica", 16))
label.pack(pady=20)

# Create a frame for the image
frameImage = Frame(root, padx=10, pady=10)
frameImage.pack()

# Load and display the image
image = Image.open("code/asset/images/wendy.jpg")
image = image.resize((300, 300), Image.LANCZOS)
image = ImageTk.PhotoImage(image)

image_label = Label(frameImage, image=image)
image_label.grid(row=0, column=0)

# Create a frame for the button
opts = Frame(root, padx=10, pady=10)
opts.pack()

# Create a button to navigate to the next page
next_button = Button(opts, text="Halaman Selanjutnya", command=open_next_page)
next_button.grid(row=0, column=0)

root.mainloop()

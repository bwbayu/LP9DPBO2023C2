from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
# DATA 1
Apartemen1 = Apartemen("Wendy", 3, 3, "321 Maple Avenue, Town")
Apartemen1.add_fasilitas("Kolam Renang")
Apartemen1.add_fasilitas("Gym")
Apartemen1.add_fasilitas("Garasi")
hunians.append(Apartemen1)
# DATA 2
Apartemen2 = Apartemen("Haerin", 10, 100, "123 Maple Avenue, City")
Apartemen2.add_fasilitas("Kolam Renang")
Apartemen2.add_fasilitas("Taman")
Apartemen2.add_fasilitas("Cafe")
Apartemen2.add_fasilitas("Garasi")
hunians.append(Apartemen2)
# DATA 3
hunians.append(Rumah("Seulgi", 4, 3, "123 Main Street, City", 2500000000))
# DATA 4
hunians.append(Indekos("Hanni", "Minji", 1, 1, "789 Elm Street, City", 1500000))
# DATA 5
hunians.append(Rumah("Yunjin", 2, 4, "456 Oak Avenue, Town", 3500000000))
# DATA 6
hunians.append(Indekos("Suho", "Sehun", 1, 3, "456 Pine Street, City", 1800000))

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan data pemilik
    i = 0
    Label(d_frame, text="Nama Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1

    # menampilkan data alamat
    Label(d_frame, text="Alamat: " + hunians[index].get_alamat(), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1

    # jika jenis indekos maka menampilkan data penghuni
    if(hunians[index].get_jenis() == "Indekos"):
        Label(d_frame, text="Nama Penghuni: " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=i, column=0, sticky="w")
        i += 1
        Label(d_frame, text="Harga per bulan: " + str(hunians[index].get_hargaPerBulan()), anchor="w").grid(row=i, column=0, sticky="w")
    elif(hunians[index].get_jenis() == "Rumah"):
        Label(d_frame, text="Harga Rumah: " + str(hunians[index].get_harga()), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1

    # menampilkan data dokumen
    Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1
    # menampilkan jumlah penghuni
    Label(d_frame, text="Jumlah Penghuni: " + str(hunians[index].get_jml_penghuni()), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1

    # menampilkan jumlah kamar
    Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=i, column=0, sticky="w")
    i += 1

    # jika jenisnya apartemen maka akan menampilkan data fasilitas
    if(hunians[index].get_jenis() == "Apartemen"):
        if len(hunians[index].get_fasilitas()) > 0:
            fasilitas_str = ", ".join(hunians[index].get_fasilitas())
        else:
            fasilitas_str = "-"
        Label(d_frame, text="Fasilitas: " + fasilitas_str, anchor="w").grid(row=i, column=0, sticky="w")
        i += 1

    # menampilkan data summary
    Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=i, column=0, sticky="w")
    
def dashboardPage():
    root.withdraw()  # Hide the main window
    dashboard = Tk()
    dashboard.title("Dashboard")
    # membuat frame untuk data residen
    frame = LabelFrame(dashboard, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    # buat frame untuk button
    opts = LabelFrame(dashboard, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    # membuat button add
    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=1)

    # membuat button exit
    b_exit = Button(opts, text="Exit", command=dashboard.quit)
    b_exit.grid(row=0, column=2)
    # Create a button to go back to the main page
    back_button = Button(opts, text="Back", command=lambda: back_to_main(dashboard))
    back_button.grid(row=0, column=0)

    # HEADER
    nomor = Label(frame, text="No", width=5, borderwidth=1, relief="solid")
    nomor.grid(row=0, column=0)
    jenis = Label(frame, text="Jenis", width=15, borderwidth=1, relief="solid")
    jenis.grid(row=0, column=1)
    nama = Label(frame, text="Nama", width=40, borderwidth=1, relief="solid")
    nama.grid(row=0, column=2)
    # menampilkan data dari list hunians
    for index, h in enumerate(hunians):
        # menampilkan nomor
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index+1, column=0)

        # menampilkan jenis hunians
        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index+1, column=1)

        # menampilkan data pemilik/penghuni
        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index+1, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index+1, column=2)

        # membuat button details
        b_detail = Button(frame, text="Details ", command=lambda index=index+1: details(index-1))
        b_detail.grid(row=index+1, column=3)
    dashboard.mainloop()

def back_to_main(home):
    home.destroy()  # Destroy the details page
    root.deiconify()  # Show the main window

# LANDING PAGE
root = Tk()
root.title("Praktikum DPBO Python")

# Create a label "Halo, selamat datang"
label = Label(root, text="Halo, Selamat Datang Wendy", font=("Helvetica", 16))
label.pack(pady=20)

# Create a frame for the image
frameImage = Frame(root, padx=10, pady=10)
frameImage.pack()

# Load and display the image
image = Image.open("code/asset/images/wendy.jpg")
image = image.resize((141, 176), Image.LANCZOS)
image = ImageTk.PhotoImage(image)

image_label = Label(frameImage, image=image)
image_label.grid(row=0, column=0)

# Create a frame for the button
opts = Frame(root, padx=10, pady=10)
opts.pack()

# Create a button to navigate to the next page
next_button = Button(opts, text="Home", command=dashboardPage)
next_button.grid(row=0, column=1)
# Create an exit button
exit_button = Button(opts, text="Exit", command=root.quit)
exit_button.grid(row=0, column=0)

root.mainloop()
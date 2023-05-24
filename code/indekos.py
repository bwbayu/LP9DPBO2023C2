from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, jml_penghuni, jml_kamar, alamat, hargaPerBulan):
        super().__init__("Indekos", jml_penghuni, jml_kamar, alamat)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.hargaPerBulan = hargaPerBulan

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_hargaPerBulan(self):
        return self.hargaPerBulan
from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, alamat, harga):
        super().__init__("Rumah", jml_penghuni, jml_kamar, alamat)
        self.nama_pemilik = nama_pemilik
        self.harga = harga

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_harga(self):
        return self.harga
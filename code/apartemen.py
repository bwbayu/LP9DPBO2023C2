from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, alamat):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, alamat)
        self.nama_pemilik = nama_pemilik
        self.fasilitas = []

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_fasilitas(self):
        return self.fasilitas

    def add_fasilitas(self, fasilitas):
        self.fasilitas.append(fasilitas)
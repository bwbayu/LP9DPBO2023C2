class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, alamat = ""):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.alamat = alamat

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_alamat(self):
        return self.alamat

    def get_dokumen(self):
        pass

    def get_summary(self):
        return f"Hunian {self.jenis} beralamat di {self.alamat}, ditempati oleh {self.jml_penghuni} orang dan memiliki {self.jml_kamar} kamar."
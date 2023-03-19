#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class PesawatTerbang:
    def __init__(self, hari, tanggal, maskapai, derpature, arrive, harga):
        self.hari = hari
        self.tanggal = tanggal
        self.maskapai = maskapai
        self.derpature = derpature
        self.arrive = arrive
        self.harga = harga

    def info(self):
        print(f"===========================\n           WAKTU           \n===========================")
        print(f"Hari : {self.hari}\nTanggal : {self.tanggal}\nMaskapai: {self.maskapai}")
        print(f"===========================\n       PEMBERANGKATAN       \n===========================")
        print(f"Derpature : {self.derpature}\nArrive : {self.arrive}\nHarga(Rp) : {self.harga}")
pesawatA = PesawatTerbang("Senin", "13 Feburari 2023", "Asia Cargo Airlines", "Jakarta (10.30)", "Majalengka (11.45)", "250.000,00")
pesawatA.info()
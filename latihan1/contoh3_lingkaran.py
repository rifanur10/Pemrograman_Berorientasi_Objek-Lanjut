#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class Lingkaran:

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
lingkaranA = Lingkaran(14)
print(f"Luas lingkaran: {lingkaranA.luas()}")
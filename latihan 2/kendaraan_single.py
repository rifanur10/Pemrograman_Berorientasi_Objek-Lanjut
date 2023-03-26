print("Rifa Nurfaizah\n210511025\nTI21A\n")

class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang berjalan.")

class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Sepeda motor ini sedang belok.")

motorA = SepedaMotor("Sepeda Motor", "Nmax", "Hitam", 155)
motorA.berkendara() # Output: Kendaraan ini sedang berjalan.
motorA.belok() # Output: Sepeda motor ini sedang belok.
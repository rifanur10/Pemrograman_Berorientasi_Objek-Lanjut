#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class KonversiSuhu :

    def __init__(self, kelvin):
        self.kelvin = kelvin

    def to_celcius(self):
        return self.kelvin - 273.15

    def to_reamur(self):
        return 4/5 * (self.kelvin - 273)

    def to_fahrenheit(self):
        return 9/5 * (self.kelvin - 273.15) + 32

suhu = KonversiSuhu(65)
celcius = suhu.to_celcius()
reamur = suhu.to_reamur()
fahrenheit = suhu.to_fahrenheit()

# Konversi suhu 65 derajat Kelvin ke Celcius
print(f"Konversi suhu {suhu.kelvin} derajat kelvin adalah {celcius} derajat celcius") # Output: -208.14999999999998

# Konversi suhu 65 derajat Kelvin ke Reamur
print(f"Konversi suhu {suhu.kelvin} derajat kelvin adalah {reamur} derajat reamur") # Output: -166.4

# Konversi suhu 65 derajat Kelvin ke Fahrenheit
print(f"Konversi suhu {suhu.kelvin} derajat kelvin adalah {fahrenheit} derajat fahrenheit") # Output: -342.66999999999996
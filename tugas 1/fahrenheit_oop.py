#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class KonversiSuhu :

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def to_celcius(self):
        return 5/9 * (self.fahrenheit - 32)

    def to_reamur(self):
        return 4/9 * (self.fahrenheit - 32)

    def to_kelvin(self):
        return 5/9 * (self.fahrenheit - 32)

suhu = KonversiSuhu(65)
celcius = suhu.to_celcius()
reamur = suhu.to_reamur()
kelvin = suhu.to_kelvin()

# Konversi suhu 65 derajat Fahrenheit ke Celcius
print(f"Konversi suhu {suhu.fahrenheit} derajat fahrenheit adalah {celcius} derajat celcius") # Output: 18.33333333333336

# Konversi suhu 65 derajat Fahrenheit ke Reamur
print(f"Konversi suhu {suhu.fahrenheit} derajat fahrenheit adalah {reamur} derajat reamur") # Output: 14.66666666666666

# Konversi suhu 65 derajat Fahrenheit ke Kelvin
print(f"Konversi suhu {suhu.fahrenheit} derajat fahrenheit adalah {kelvin} derajat kelvin") # Output: 18.33333333333336
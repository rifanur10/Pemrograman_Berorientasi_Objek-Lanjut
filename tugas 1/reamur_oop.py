#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class KonversiSuhu :

    def __init__(self, reamur):
        self.reamur = reamur

    def to_celcius(self):
        return (5/4) * self.reamur

    def to_fahrenheit(self):
        return (9/4) * self.reamur

    def to_kelvin(self):
        return (5/4) * self.reamur + 273.15

suhu = KonversiSuhu(65)
celcius = suhu.to_celcius()
fahrenheit = suhu.to_fahrenheit()
kelvin = suhu.to_kelvin()

# Konversi suhu 65 derajat Reamur ke Celcius
print(f"Konversi suhu {suhu.reamur} derajat reamur adalah {celcius} derajat celcius") # Output: 81.25

# Konversi suhu 65 derajat Reamur ke Fahrenheit
print(f"Konversi suhu {suhu.reamur} derajat reamur adalah {fahrenheit} derajat fahrenheit") # Output: 146.25

# Konversi suhu 65 derajat Reamur ke Kelvin
print(f"Konversi suhu {suhu.reamur} derajat reamur adalah {kelvin} derajat kelvin") # Output: 354.4
#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class Celcius:

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5

mycelcius = 70
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit)
#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class Kalkulator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y

# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(4, 5)) # Output: 9
print(Kalkulator.subtract(12, 7)) # Output: 5

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(4, 5)) # Output: 20
print(Kalkulator.divide(16, 4)) # Output: 4.0
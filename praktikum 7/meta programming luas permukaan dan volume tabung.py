#Nama   : Rifa NUrfaizah
#Kelas  : R1
#NIM    : 210511025

class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, jari, tinggi):
            return 4 * 22/7 * jari * (jari + tinggi)
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari, tinggi):
            return 22/7 * jari * jari * tinggi
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=TabungMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(40, 20)
C = A.volume(40, 20)
print('Luas Permukaan Tabung:',B)
print('Volume Tabung:',C)

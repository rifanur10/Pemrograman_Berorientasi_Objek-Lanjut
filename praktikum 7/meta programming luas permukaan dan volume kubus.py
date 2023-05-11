#Nama   : Rifa Nurfaizah
#Kelas  : R1
#NIM    : 210511025

class KubusMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, sisi):
            return 4 * sisi * sisi
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, sisi):
            return sisi * sisi * sisi
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=KubusMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(40)
C = A.volume(40)
print('Luas Permukaan Kubus:',B)
print('Volume Kubus:',C)
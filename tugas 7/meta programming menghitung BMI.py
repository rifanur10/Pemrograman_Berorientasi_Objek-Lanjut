#Nama   : Rifa Nurfaizah
#Kelas  : R1
#NIM    : 210511025

class MenghitungBMIMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def pria(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 10/100
        cls.pria = classmethod(pria)

        def wanita(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 15/100
        cls.wanita = classmethod(wanita)
class Ideal(metaclass=MenghitungBMIMeta):
    pass
A = Ideal()
B = A.pria(170)
C = A.wanita(150)
print('BMI Pria:',B)
print('BMI Wanita:',C)
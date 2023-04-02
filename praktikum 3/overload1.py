'''
Nama    : Rifa Nurfaizah
Kelas   : R1
NIM     : 210511025
'''

class belanja:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare+other.fare

sabuncuci = belanja(30)
skincare = belanja(200)
total = sabuncuci+skincare
print(f'\nHarga Total: {str(total)}k\n')
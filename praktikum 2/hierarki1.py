print('\nHierarchical Inheritance_Dokter\n\n')

class Dokter:
    def __init__(self, name, nip):
        self.name = name
        self.nip = nip

    def ket(self):
        print(f'{self.name} adalah Dokter Spesialis dengan NIP {self.nip}\n')
    
    def getName(self):
        return self.name 
    
    def getNip(self):
        return self.nip

class Jk(Dokter):
    def __init__(self, name, nip, jk):
        super().__init__(name, nip)
        self.jk = jk
    
    def detail(self):
        print(f'Nama: {self.name}\nNip: {self.nip}\nJk: {self.jk}\n')

    def getJk(self):
        return self.jk

class Spesialis(Jk):
    def __init__(self, name, nip, jk, spesialis):
        super().__init__(name, nip, jk)
        self.spesialis = spesialis

    def keterangan(self):
        print(f'Nama: {self.name}\nNip: {self.nip}\nJk: {self.jk}\nSpesialis: {self.spesialis}\n')

if __name__ == '__main__':
    dok1 = Spesialis('Sakri', 301202,'Laki-laki', 'Hati')
    dok1.keterangan()
    dok1.detail()
    dok1.ket()
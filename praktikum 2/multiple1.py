print('\nMultiple Inheritance_UN1TY\n')

class UN1TY:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Asal: {self.asal}")

class Dream:
    def __init__(self, posisi, line):
        self.posisi = posisi
        self.line = line
    def display_info(self):
        print(f"Posisi: {self.posisi}")
        print(f"Line: {self.line}")

class Ilichil:
    def __init__(self, posisi1, line1):
        self.posisi1 = posisi1
        self.line1 = line1
    def display_info(self):
        print(f"Posisi: {self.posisi1}")
        print(f"Line: {self.line1}")

class Universe(Dream, Ilichil):
    def __init__(self, nama, asal, posisi, line, posisi1, line1):
        UN1TY.__init__(self, nama, asal)
        Dream.__init__(self, posisi, line)
        Ilichil.__init__(self, posisi1, line1)
    def display1(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Asal: {self.asal}")
        print(f"Posisi: {self.posisi}")
        print(f"Line: {self.line}")
    def display1(self):
        print(f"Nama: {self.nama}")
        print(f"Asal: {self.asal}")
        print(f"Posisi: {self.posisi1}")
        print(f"Line: {self.line1}")

un1ty1 = Universe("Shandy","Bengkulu","Penyanyi", "2000",'Penyanyi','2000\n')
un1ty1.display1()       

un1ty2 = Universe("Fenly","Gorontalo","Penyanyi", "2001",'Penyanyi','2001\n')
un1ty2.display1()       
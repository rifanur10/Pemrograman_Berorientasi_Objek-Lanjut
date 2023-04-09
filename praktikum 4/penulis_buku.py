print('Rifa Nurfaizah\n210511025\nT121A(R1)\n')

class Penulis:
    def __init__(self,nama):
        self.nama = nama
        self.inventory = Inventory()
    
    def tampil(self):
        print(f'\nPenulis\t\t:  {self.nama}\n')

class Buku:
    def __init__(self,judul,publish,penerbit):
        self.judul = judul
        self.publish = publish
        self.penerbit = penerbit

    def get_judul(self):
        return self.judul

    def get_publish(self):
        return self.publish

    def get_penerbit(self):
        return self.penerbit

class Inventory:
    def __init__(self):
        self.books = []

    def add_buku(self,buku):
        self.books.append(buku)

    def daftar_buku(self):
        for buku in self.books:
            print(f'Judul\t\t: ',buku.judul)
            print(f'Terbit\t\t: ',buku.publish)
            print(f'Penerbit\t: ',buku.penerbit)

penulis1 = Penulis('Andrea Hirata')
laskarpelangi = Buku('Laskar Pelangi', 'Yogyakarta, 2005', 'Bentang Pustaka')
sangpemimpi = Buku('Sang Pemimpi', 'Yogyakarta, 2006', 'Bentang Pustaka')
edensor = Buku('Edensor', 'Yogyakarta, 2007', 'Bentang Pustaka')
maryamahkarpov = Buku('Maryamah Karpov', 'Yogyakarta, 2008', 'Bentang Pustaka\n')
penulis1.inventory.add_buku(laskarpelangi)
penulis1.inventory.add_buku(sangpemimpi)
penulis1.inventory.add_buku(edensor)
penulis1.inventory.add_buku(maryamahkarpov)
penulis1.inventory.books
penulis1.tampil()
penulis1.inventory.daftar_buku()
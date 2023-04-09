print('Rifa NUrfaizah\n210511025\nT121A(R1)\n')

class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t:  {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t:  {jurnal.date}')
           
jurnal1 = Jurnal('Sistem Informasi Geografis Objek Wisata Kabupaten Pemalang', 2016)
jurnal2 = Jurnal('Perancangan Sistem Informasi Terpadu Pemerintah Daerah Kabupaten Paser', 2009)
peneliti1 = peneliti('Hendra Marcos,Nataniel Dengen', [jurnal1, jurnal2])
jurnal3 = Jurnal('Sistem Informasi Manajemen dalam Rumah Sakit', 2007)
jurnal4 = Jurnal('Pengembangan Sistem Informasi Penjualan dan Pembelian Pada Toko PC Tablet', 2014)
peneliti2 = peneliti('Nuhyarsyah,Rizal Isnanto', [jurnal3, jurnal4])
peneliti1.daftar_jurnal()
peneliti2.daftar_jurnal()
 
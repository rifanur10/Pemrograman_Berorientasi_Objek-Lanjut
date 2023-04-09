print('Rifa Nurfaizah\n210511025\nT121A(R1)\n')

class List_drama:
    def __init__(self,tanggal):
        self.tanggal = tanggal
        self.list = List()
    
    def tampil(self):
        print('\t\t\tDrama List\t\t\t\n','\t','='*37,'\t')
        print(f'Date\t\t:  {self.tanggal}\n')

class Drama:
    def __init__(self,judul,status,genre,tayang,pemeran):
        self.judul = judul
        self.status = status
        self.genre = genre
        self.tayang = tayang
        self.pemeran = pemeran

    def get_judul(self):
        return self.judul
    def get_status(self):
        return self.status
    def get_genre(self):
        return self.genre
    def get_tayang(self):
        return self.tayang
    def get_pemeran(self):
        return self.pemeran

class List:
    def __init__(self):
        self.kDrama = []

    def add_drama(self,drama):
        self.kDrama.append(drama)

    def daftar_drama(self):
        for drama in self.kDrama:
            print(f'Judul\t\t: ',drama.judul)
            print(f'Status\t\t: ',drama.status)
            print(f'Genre\t\t: ',drama.genre)
            print(f'Tayang\t\t: ',drama.tayang)
            print(f'Pemeran\t\t: ',drama.pemeran,'\n')

listMaret = List_drama('April 2023')
drakor1 = Drama('Stealer: The Treasure Keeper', 'ON GOING', 'Action, Revenge Tragedy, Criminal', 'Jumat-Minggu Pukul 22.00', 'Joo Won, Lee Joo Woo, Jo Han Chul')
drakor2 = Drama('Call It Love', 'END', 'Action, Revenge Tragedy', 'Senin-Selasa Pukul 23.00', 'Kim Young Kwang, Lee Sung Kyung, Sung Joon, Ahn Hee Yeon')
drakor3 = Drama('Bora Deborah', 'ON GOING', 'Romance', 'Jumat Pukul 12.00', 'Yoo In Na, Yoon Hyun Min, Joo Sang Wook')
drakor4 = Drama('IOur Blooming Youth', 'END', 'Romance', 'Rabu-Kamis Pukul 10.30', 'park Hyung sik, Jeon So Nee')
listMaret.list.add_drama(drakor1)
listMaret.list.add_drama(drakor2)
listMaret.list.add_drama(drakor3)
listMaret.list.add_drama(drakor4)
listMaret.list.kDrama
listMaret.tampil()
listMaret.list.daftar_drama()
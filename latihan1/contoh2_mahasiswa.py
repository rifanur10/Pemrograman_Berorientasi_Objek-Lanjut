#Nama   : Rifa Nurfaizah
#NIM    : 210511025
#Kelas  : R1
#Matkul : Pemrogaman Berorientasi Objek 2 

class Mahasiswa:

    def __init__(self, nama, jeniskelamin, perguruantinggi, prodi, jenjang, nim, semesterawal, status):
        self.nama = nama
        self.jeniskelamin = jeniskelamin
        self.perguruantinggi = perguruantinggi
        self.prodi = prodi
        self.jenjang = jenjang
        self.nim = nim
        self.semesterawal = semesterawal
        self.status = status

    def info(self):
        print(f"Nama : {self.nama}\nJenis Kelamin : {self.jeniskelamin}\nPerguruan Tinggi : {self.perguruantinggi}\nProgam Studi : {self.prodi}\nJenjang : {self.jenjang}\nNomor Induk Mahasiswa : {self.nim}\nSemester Awal : {self.semesterawal}\nStatus Mahasiswa : {self.status}")
mahasiswaB = Mahasiswa("Rifa Nurfaizah", "Perempuan", "Universitas Muhammadiyah Cirebon", "Teknik Informatika", "S1", "210511025", "Ganjil 2021", "Belum Lulus")
mahasiswaB.info()
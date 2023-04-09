print('Rifa Nurfaizah\n210511025\nT121A(R1)\n')

class Song:
    def __init__(self, *song):
        self.song = song[0]

    def display(self):
        print(self.song)

class Album:
    def __init__(self, *idol_album):
        self.idol_album = idol_album[0]
        self.songs = []

    def add(self, lagu):
        self.songs.append(lagu)

    def remove(self, lagu):
        self.songs.remove(lagu)

    def display(self):
        print(f"="*50,'\n',self.idol_album)
        print("="*50)
        for lagu in self.songs:
            lagu.display()

if __name__ == "__main__":
    idol = Album("\t\t\tAlan Waker\t\t\t")
    album = Album("Album\t: Sped Up")
    song1 = Song(" Songs\t: All Falls Down")
    song2 = Song("\t  Darkside")
    song3 = Song("\t  Alone")
    song4 = Song("\t  The Spectre")
    song5 = Song("\t  Alone, Pt. II\n")
    album2 = Album("Album\t: World Of Walker")
    song1_album2 = Song(" Songs\t: Alone,Pt. II")
    song2_album2 = Song("\t  Out Of Love")
    song3_album2 = Song("\t  On My Way")
    song4_album2 = Song("\t  Man On The Moon\n")

    album.add(song1)
    album.add(song2)
    album.add(song3)
    album.add(song4)
    album.add(song5)
    album2.add(song1_album2)
    album2.add(song2_album2)
    album2.add(song3_album2)
    album2.add(song4_album2)

    idol.add(album)
    idol.add(album2)
    idol.display()

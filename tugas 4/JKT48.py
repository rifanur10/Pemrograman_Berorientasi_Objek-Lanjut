print('Rifa Nurfaizah\n210511025\nT121A(R1)\n')

class Jkt48:
    def __init__(self,member=None):
        if member is None:
            self.member = []
        else:
            self.member = member

    def add_member(self,jkt48t_member):
        self.member.append(jkt48_member)

    def daftar_member(self):
        print('\t\tDaftar Member\t\t')
        print('\t','='*27,'\t')
        for jkt48_member in self.member:
            print(f'Name\t\t: ',jkt48_member.name)
            print(f'Unit\t\t: ',jkt48_member.unit)

class Jkt48_member:
    def __init__(self,name,unit):
        self.name = name
        self.unit = unit

    def get_name(self):
        return self.name

    def get_unit(self):
        return self.unit
    
class Comeback:
    def __init__(self,comeback,title,song,Jkt48):
        self.comeback = comeback
        self.title = title
        self.song = song
        self.Jkt48 = Jkt48

    def tampil(self):
        print(f'Comeback\t: {self.comeback}')
        print(f'Album\t\t: {self.title}')
        print(f'Song\t\t: {self.song}\n')

member1 = Jkt48_member('Adzana Shaliha', 'Revival 2013\n')
member2 = Jkt48_member('Angelina Christy', 'Revival 2014\n')
member3 = Jkt48_member('Azizi Asadel', 'Waiting Stage\n')
member4 = Jkt48_member('Cornelia Vanisa', '-\n')
member5 = Jkt48_member('Febriola Sinambela', '-\n')
member6 = Jkt48_member('Flora Shafiq', '-\n')
member7 = Jkt48_member('Fiony Alveria', '-\n')
jkt48_2020 = Jkt48([member1, member2, member3, member4, member5, member6, member7])
jkt48_comeback = Comeback('JKT48 2020', 'Believe', 'Gingham Check',jkt48_2020)
jkt48_comeback.Jkt48.member
jkt48_comeback.tampil()
jkt48_comeback.Jkt48.daftar_member()
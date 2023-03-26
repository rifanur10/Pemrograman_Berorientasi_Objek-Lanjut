print('\nSingle Inheritance_BASO ACI\n\n')

class Menu:
    def __init__(self,menu,level):
        self.menu = menu
        self.level = level

    def info(self):
        print('Menu\t\t: ',self.menu)
        print('Level\t\t: ',self.level)

class Pesan(Menu):
    def __init__(self,menu,level,topping,tambahan):
        super().__init__(menu,level)
        self.topping = topping
        self.tambahan = tambahan
       
    def pesan(self):
        print('Topping\t\t: ',self.topping)
        print('Tambahan\t: ',self.tambahan)

pesan1 = Pesan("Baso Aci",2,"Cuangki lidah dan Batagor","Pilus cikur\n")
pesan1.info()
pesan1.pesan()


pesan2 = Pesan("Cilok","5","Balungan","-\n")
pesan2.info()
pesan2.pesan()
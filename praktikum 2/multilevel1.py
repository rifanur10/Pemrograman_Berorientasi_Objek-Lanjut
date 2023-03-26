print('\nMultilevel Inheritance_FAMILY\n')

class Family:
    def show(self):
        print("My Family...")

class Father(Family):
    name_father=""

    def show1(self):
        print(self.nama_father)

class Child(Father):
    name_child=""

    def show2(self):
        print("Father Name:",self.name_father)
        print("Child Name:",self.name_child)

o=Child()
o.name_father="Asep"
o.name_child="Faiz"
o.show()
o.show2()
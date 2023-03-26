print('\nHybrid Inheritance_JKT48\n\n')

# Hybrid Inheritance
class vehicle:
    
    def __init__(self,name,grup):
        self.name = name
        self.grup = grup
        
    def show_details(self):
        print(f'\nName : {self.name}')
        print(f'Grup : {self.grup}')
                
class bike(vehicle):
    
    # Inherit Properties and Override
    def __init__(self,name,grup,album):
        super().__init__(name,grup)
        self.album = album
    
    # Inherit Behavior and Override
    def show_details(self):
        super().show_details()
        print(f'Album : {self.album}\n')
    
    # Method of Derived Class
    def info(self):
        print(f'{self.name} {self.grup} mengeluarkan album terbarunya yaitu {self.album}')
        

class car(bike,vehicle):
    
    def info(self):
        print('\n\n\t\t\tNEWS!!!\t\t\t\n\n')

bajaj = car("Shani","AKB48","JOY KICK! TEARS")
bajaj.show_details()
bajaj.info()

idol1 = bike("Haruka","AKB48","TADAIMA RENAICHUU")
idol1.info()
idol1.show_details()
print('Rifa Nurfaizah\n210511025\nT121A(R1)\n')

class Menu:
    def __init__(self, dishes=None):
        if dishes is None:
            self.dishes = []
        else:
            self.dishes = dishes

    def add_dish(self, dish):
        self.dishes.append(dish)

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

dish1 = Dish("Baso Lava", 20000)
dish2 = Dish("Baso Rusuk Hotplate", 15000)
menu = Menu([dish1, dish2])
restaurant = Restaurant("Bakso Rusuk Jos", menu)
restaurant.menu.dishes # output: [dish1, dish2]
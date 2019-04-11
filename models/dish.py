from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.level_of_spicy import LevelOfSpicy


class Dish:

    def __init__(self, type_of_menu=TypeOfMenu.STANDARD_MENU, currency="", price=0, name="",
                 temperature=Temperature.NORMAL, weigh=0, level_of_spicy=LevelOfSpicy.NORMAL):
        self.type_of_menu = type_of_menu
        self.currency = currency
        self.price = price
        self.name = name
        self.temperature = temperature
        self.weigh = weigh
        self.level_of_spicy = level_of_spicy

    def __del__(self):
        pass

    def __str__(self):
        return "\ntype_of_menu = " + str(self.type_of_menu) + "\ncurrency = " + self.currency + "\nprice = " \
               + str(self.price) + "\nname = " + self.name + "\ntemperature = " + str(self.temperature) + "\nweigh = " \
               + str(self.weigh) + "\nlevel_of_spicy = " + str(self.level_of_spicy)

    def __repr__(self):
        return "name = " + self.name

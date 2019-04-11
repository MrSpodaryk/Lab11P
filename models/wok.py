from models.dish import Dish
from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.level_of_spicy import LevelOfSpicy
from enums.type_of_meat import TypeOfMeat
from enums.type_of_noodles import TypeOfNoodles
from enums.type_of_sauce import TypeOfSauce


class Wok(Dish):

    def __init__(self, type_of_menu=TypeOfMenu.STANDARD_MENU, currency="", price=0, name="",
                 temperature=Temperature.NORMAL, weigh=0, level_of_spicy=LevelOfSpicy.NORMAL,
                 type_of_noodles=TypeOfNoodles.SOBA, type_of_meat=TypeOfMeat.BEEF,
                 type_of_sauce=TypeOfSauce.SOUR_SWEET):
        Dish.__init__(self, type_of_menu, currency, price, name,
                      temperature, weigh, level_of_spicy)

        self.type_of_noodles = type_of_noodles
        self.type_of_meat = type_of_meat
        self.type_of_sauce = type_of_sauce

    def __del__(self):
        pass

    def __str__(self):
        return str(Dish.__str__(self)) + "\ntype_of_noodles = " + str(self.type_of_noodles) + "\ntype_of_meat = "\
               + str(self.type_of_meat) + "\ntype_of_sauce = " + str(self.type_of_sauce)

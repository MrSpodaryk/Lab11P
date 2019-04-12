from models.dish import Dish
from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.level_of_spicy import LevelOfSpicy


class Sushi(Dish):
    def __init__(self, type_of_menu=TypeOfMenu.STANDARD_MENU, currency="", price=0, name="",
                 temperature=Temperature.NORMAL, weigh=0, level_of_spicy=LevelOfSpicy.NORMAL, number_of_sushi=0):
        Dish.__init__(self, type_of_menu, currency, price, name,
                      temperature, weigh, level_of_spicy)

        self.number_of_sushi = number_of_sushi

    def __del__(self):
        pass

    def __str__(self):
        return str(Dish.__str__(self)) + "\nnumber_of_sushi = " + str(self.number_of_sushi)

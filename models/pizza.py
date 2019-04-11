from models.dish import Dish
from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.level_of_spicy import LevelOfSpicy
from enums.size import Size
from enums.style_of_dough import StyleOfDough


class Pizza(Dish):

    def __init__(self, type_of_menu=TypeOfMenu.STANDARD_MENU, currency="", price=0, name="",
                 temperature=Temperature.NORMAL, weigh=0, level_of_spicy=LevelOfSpicy.NORMAL,
                 size=Size.STANDARD, style_of_dough=StyleOfDough.AMERICAN):
        Dish.__init__(self, type_of_menu, currency, price, name,
                      temperature, weigh, level_of_spicy)

        self.size = size
        self.style_of_dough = style_of_dough

    def __del__(self):
        pass

    def __str__(self):
        return str(Dish.__str__(self)) + "\nsize = " + str(self.size) + "\nstyle_of_dough = " + str(self.style_of_dough)

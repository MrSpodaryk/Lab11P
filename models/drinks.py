from models.dish import Dish
from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.level_of_spicy import LevelOfSpicy


class Drinks(Dish):

    def __init__(self, type_of_menu=TypeOfMenu.STANDARD_MENU, currency="", price=0, name="",
                 temperature=Temperature.NORMAL, weigh=0, level_of_spicy=LevelOfSpicy.NORMAL,
                 capacity=0, presence_of_caffeine=False, presence_of_lactose=True):
        Dish.__init__(self, type_of_menu, currency, price, name,
                      temperature, weigh, level_of_spicy)

        self.capacity = capacity
        self.presence_of_caffeine = presence_of_caffeine
        self.presence_of_lactose = presence_of_lactose

    def __del__(self):
        pass

    def __str__(self):
        return str(Dish.__str__(self)) + "\ncapacity = " + str(self.capacity) + "\npresence_of_caffeine = "\
               + str(self.presence_of_caffeine) + "\npresence_of_lactose = " + str(self.presence_of_lactose)

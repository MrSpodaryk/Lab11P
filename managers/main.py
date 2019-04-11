from models.drinks import Drinks
from models.dish import Dish
from models.pizza import Pizza
from models.sushi import Sushi
from models.wok import Wok
from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.type_of_meat import TypeOfMeat
from enums.style_of_dough import StyleOfDough
from enums.size import Size
from enums.level_of_spicy import LevelOfSpicy
from enums.type_of_sauce import TypeOfSauce
from enums.type_of_noodles import TypeOfNoodles
from managers.dish_manager import DishManager

dishes = [
    Dish(TypeOfMenu.CHILD_MENU, "$", 25, "Puree", Temperature.NORMAL, 200, LevelOfSpicy.NOT_SPICY),
    Drinks(TypeOfMenu.VEGETARIAN_MENU, "$", 15, "Milk", Temperature.COLD, 300, LevelOfSpicy.NOT_SPICY, 300, False,
           True),
    Pizza(TypeOfMenu.STANDARD_MENU, "$", 150, "Paperoni", Temperature.HOT, 500, LevelOfSpicy.NORMAL, Size.STANDARD,
          StyleOfDough.AMERICAN),
    Sushi(TypeOfMenu.STANDARD_MENU, "$", 55, "California", Temperature.COLD, 300, LevelOfSpicy.NOT_SPICY, 6),
    Wok(TypeOfMenu.STANDARD_MENU, "$", 35, "CCC", Temperature.HOT, 300, LevelOfSpicy.HIGH, TypeOfNoodles.SOBA,
        TypeOfMeat.BEEF, TypeOfSauce.SOUR_SWEET)
]

dish_manager = DishManager(*dishes)
for i in dishes:
    print()
    print(i)
print()

sorted_dishes_by_type = dish_manager.find_dish_by_type_of_menu(TypeOfMenu.STANDARD_MENU)
print("sorted_dishes_by_type :")
for i in sorted_dishes_by_type:
    print(i)
    print()

sorted_dishes_by_increase_price = DishManager.sort_dish_by_increase_price(dishes)
print("sorted_dishes_by_increase_price :")
print(sorted_dishes_by_increase_price)
print()

sorted_dishes_by_decrease_price = DishManager.sort_dish_by_decrease_price(dishes)
print("sorted_dishes_by_decrease_price :")
print(sorted_dishes_by_decrease_price)
print()

sorted_dishes_by_increase_weigh = DishManager.sort_dish_by_increase_weigh(dishes)
print("sorted_dishes_by_increase_weigh :")
print(sorted_dishes_by_increase_weigh)
print()

sorted_dishes_by_decrease_weigh = DishManager.sort_dish_by_decrease_weigh(dishes)
print("sorted_dishes_by_decrease_weigh :")
print(sorted_dishes_by_decrease_weigh)

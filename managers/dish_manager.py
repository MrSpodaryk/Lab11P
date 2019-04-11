class DishManager:

    def __init__(self, *args):
        self.dishes = args

    def find_dish_by_type_of_menu(self, type_of_menu):
        return list(filter(lambda dish: dish.type_of_menu == type_of_menu, self.dishes))

    @staticmethod
    def sort_dish_by_increase_price(dishes):
        return sorted(dishes, key=lambda dish: dish.price)

    @staticmethod
    def sort_dish_by_decrease_price(dishes):
        return sorted(dishes, key=lambda dish: dish.price, reverse=True)

    @staticmethod
    def sort_dish_by_increase_weigh(dishes):
        return sorted(dishes, key=lambda dish: dish.price)

    @staticmethod
    def sort_dish_by_decrease_weigh(dishes):
        return sorted(dishes, key=lambda dish: dish.price, reverse=True)

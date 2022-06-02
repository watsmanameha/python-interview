# Реализовать расчет цены товара со скидкой.
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
# в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).

class ItemDiscount:

    def __init__(self, item_name, price):
        self.__item_name = item_name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_item_name(self):
        return self.__item_name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, item_name, price, discount):
        super().__init__(item_name, price)
        self.discount = discount

    def __str__(self):
        return f'{self.get_item_name()} {self.get_price() * (100 - self.discount) / 100}'


discount_report = ItemDiscountReport('Утюг', 6000, 50)
print(discount_report)  # До скидки: Утюг 6000, После: Утюг 3000.0
discount_report.set_price(5000)
print(discount_report)  # До скидки: Утюг 5000, После: Утюг 2500.0

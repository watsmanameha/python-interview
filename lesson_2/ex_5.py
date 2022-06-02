# Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно.
# Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать вызов каждой из функции get_info.

class ItemDiscount:

    def __init__(self, item_name, price, discount):
        self.__item_name = item_name
        self.__price = price
        self.discount = discount

    def set_price(self, price):
        self.__price = price

    def get_item_name(self):
        return self.__item_name

    def get_price(self):
        return self.__price


class ItemDiscountReportFirst(ItemDiscount):

    def get_info(self):
        return self.get_item_name()


class ItemDiscountReportSecond(ItemDiscount):

    def get_info(self):
        return self.get_price() * (100 - self.discount) / 100


item_name_report = ItemDiscountReportFirst('Утюг', 6000, 50)
print(item_name_report.get_info())  # Утюг

item_price_report = ItemDiscountReportSecond('Утюг', 6000, 50)
print(item_price_report.get_info())  # 3000.0
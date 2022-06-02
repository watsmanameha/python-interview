# Реализовать возможность переустановки значения цены товара в родительском классе.
# Проверить, распечатать информацию о товаре.

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

    def get_parent_data(self):
        return {self.get_item_name()}, {self.get_price()}


discount_report = ItemDiscountReport('Утюг', 6000)
print(discount_report.get_parent_data())  # ({'Утюг'}, {6000})
discount_report.set_price(5000)
print(discount_report.get_parent_data())  # ({'Утюг'}, {5000})



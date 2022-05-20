# Создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену.
# Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
# отвечающую за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”).
# Создать экземпляры родительского класса и дочернего. Распечатать информацию о товаре.

class ItemDiscount:

    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return {self.item_name}, {self.price}


print(ItemDiscountReport('Утюг', 6000).get_parent_data())
# Вывод:
# Утюг 5640.0
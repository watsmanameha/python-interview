# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
# Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:

    def __init__(self, item_name, price):
        self.__item_name = item_name
        self.__price = price

    def get_item_name(self):
        return self.__item_name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return {self.get_item_name()}, {self.get_price()}


print(ItemDiscountReport('Утюг', 6000).get_parent_data())

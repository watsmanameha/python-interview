# Реализовать функцию print_directory_contents(path).
#
# Функция принимает имя директории и выводит ее содержимое,
# включая содержимое всех поддиректории (рекурсивно вызывая саму себя).
#
# Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile

import os


def print_directory_contents(path):
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isfile(f_path):
            print(f_path)
        else:
            print_directory_contents(f_path)



print_directory_contents('F:\\Projects\\python-interview')
# Написать программу, в которой реализовать две функции.
# В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
# Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
# Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
# Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.
import os
import random


def mk_file(f_n):
    if os.path.isfile(f'{f_n}.txt'):
        print('Файл с таким именем существует.')
        return False
    with open(f'{f_n}.txt', 'w') as f_out:
        text_list = [i*2 for i in 'abcdefghijklmnopqrstuvwxyz']
        num_list = [random.randint(0, 3) for i in range(5)]
        f_out.writelines(['{}{}\n'.format(text, num) for text, num in zip(text_list, num_list)])
        print(f'Файл создан.')


def file_output(f_n):
    with open(f_n, 'r', encoding='utf-8') as f:
        print(f'Содержимое файла - {f_n}:')
        for line in f:
            print(line)

mk_file('file')
file_output('file.txt')
# Создать два списка с различным количеством элементов.
# В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь.
# Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
# Если есть  значения, которым не хватило ключей, их необходимо отбросить.

import random

k = [random.randint(0, 5) for i in range(0, random.randint(2, 5))]
print(f'Ключи - {k}')
v = [random.randint(0, 5) for i in range(0, random.randint(2, 5))]
print(f'Значения - {v}')


if len(k) > len(v):
    for i in range(len(k) - len(v)):
        v.append(None)

dict = {key: value for key, value in zip(k, v)}

print(dict)

# Ключи - [2, 3, 0]
# Значения - [0, 4]
# {2: 0, 3: 4, 0: None}
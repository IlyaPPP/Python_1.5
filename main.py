# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

array = []

for i in range(100):
    array.append(randint(0, 100))

print(array)

x = int(input("Введите минимум: "))
y = int(input("Введите максимум: "))
print("Число |  индекс")

for i in range(100):
    if array[i] >= x and array[i] <= y:
        print(array[i],'   ->   ', i)

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

array = []


x = int(input("Введите первый элемент массива: "))
y = int(input("Введите разность прогрессии массива: "))
z = int(input("Введите количество элементов массива: "))

for i in range(1, z):
    if i == 1:
        array.append(x)
    array.append((i*y)+x)

print(array)

n = int(input("Введите n-ый член прогрессии: "))
find_element = x + (n-1) * y
if find_element <= array[-1]:
    print(find_element)
else:
    print("Такой n отсутствует в прогрессии")

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
set1 = set(int(input("Введите элемент множества: ")) for _ in range(n))

m = int(input("Введите количество элементов второго множества: "))
set2 = set(int(input("Введите элемент множества: ")) for _ in range(m))

intersection = set()

for element in set1:
    if element in set2:
        intersection.add(element)

min_element = min(intersection)  # Находим минимальный элемент пересечения

while min_element in intersection:
    print(min_element)
    intersection.remove(min_element)  # Удаляем текущий минимальный элемент

    # Находим новый минимальный элемент
    min_element = min(intersection) if intersection else None

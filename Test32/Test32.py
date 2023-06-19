# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума).

def find_indices(array, min_val, max_val):
    indices = []
    for i in range(len(array)):
        if array[i] >= min_val and array[i] <= max_val:
            indices.append(i)
    return indices


# Ввод данных пользователем
array = [int(x)
         for x in input("Введите элементы массива через пробел: ").split()]
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

result = find_indices(array, min_val, max_val)
print(result)

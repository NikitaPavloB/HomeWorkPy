# ; Задача 28: Вводится десятичное число. Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. Нельзя использовать функцию bin()

# ; *Пример:*
# ;     10
# ;     *Вывод:*
# ;     1010


def decimal_to_binary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


decimal_number = int(input("Введите десятичное число: "))

binary_number = decimal_to_binary(decimal_number)
print(f"Двоичное представление числа {decimal_number}: {binary_number}")

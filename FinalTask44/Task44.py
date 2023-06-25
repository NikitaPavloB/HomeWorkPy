# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#  Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем пустой DataFrame с нужными именами столбцов
one_hot_data = pd.DataFrame(columns=unique_values)

# Заполняем значениями 0
one_hot_data.loc[:, :] = 0

# Заменяем значения на 1 в соответствующих столбцах
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

# Выводим исходный DataFrame
print("Исходный DataFrame:")
print(data.head())

# Выводим преобразованный DataFrame в формате One-Hot
print("\nDataFrame в формате One-Hot:")
print(one_hot_data.head())

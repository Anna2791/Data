# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
#     Самостоятельно создайте DataFrame с данными
#     Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
#     Вычислите среднюю оценку по каждому предмету
#     Вычислите медианную оценку по каждому предмету
#     Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
#     можно также попробовать рассчитать IQR
#     Вычислите стандартное отклонение

import pandas as pd
import numpy as np

data = {
    'Ученик': ['Ученик1', 'Ученик2', 'Ученик3', 'Ученик4', 'Ученик5',
               'Ученик6', 'Ученик7', 'Ученик8', 'Ученик9', 'Ученик10'],
    'Математика': [85, 90, 78, 92, 88, 76, 95, 89, 84, 91],
    'Физика': [88, 85, 79, 91, 87, 82, 93, 86, 80, 90],
    'Химия': [90, 85, 88, 92, 87, 83, 91, 86, 84, 89],
    'Биология': [82, 88, 79, 90, 85, 81, 89, 84, 78, 87],
    'Литература': [89, 87, 85, 91, 86, 83, 90, 88, 84, 92]
}

df = pd.DataFrame(data)


print("Первые несколько строк DataFrame:")
print(df.head())

average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print("\nQ1 для математики:", Q1_math)
print("Q3 для математики:", Q3_math)


IQR_math = Q3_math - Q1_math
print("IQR для математики:", IQR_math)


std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
#  Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
#  Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз

import pandas as pd

df0 = pd.read_csv('Data_Salaries.csv')
df = pd.DataFrame(df0)

print(df.head())
print(df.info())
print(df.describe())

df_read = pd.read_csv('dz.csv')
df2 = pd.DataFrame(df_read)
salary_by_city = df2.groupby('City')['Salary'].mean()
print(salary_by_city)

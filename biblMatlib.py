# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
# # Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

# import matplotlib.pyplot as plt
# import numpy as np
#
# data = np.random.normal(0, 1, 1000)
#
# plt.hist(data, bins=30)
# plt.title('Гистограмма нормального распределения')
# plt.xlabel('Значение')
# plt.ylabel('Частота')
# plt.show()

# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
#
# import matplotlib.pyplot as plt
# import numpy as np
# random_x = np.random.rand(5)
# random_y = np.random.rand(5)
# plt.scatter(random_x,random_y)
# plt.show()



# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны


import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import numpy as np

# Запуск веб-драйвера
driver = webdriver.Firefox()

# Открытие сайта
driver.get("https://www.divan.ru/category/divany")

# Подождем некоторое время для полной загрузки страницы
time.sleep(5)

# Парсинг цен на диваны
prices = []
try:
    # Найти элементы, содержащие цены
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='price']")
    for price_element in price_elements:
        # Извлекаем текст цены и очищаем его от пробелов и символов валюты
        price_text = price_element.text.replace(' ', '').replace('руб.', '')
        try:
            price = int(price_text)
            prices.append(price)
        except ValueError:
            continue
finally:
    # Закрытие веб-драйвера
    driver.quit()

# Сохранение данных в CSV файл
with open('prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price'])
    for price in prices:
        writer.writerow([price])

# Обработка данных
if prices:
    average_price = np.mean(prices)
    print(f"Средняя цена на диваны: {average_price:.2f} руб.")

    # Построение гистограммы
    plt.hist(prices, bins=30, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена, руб.')
    plt.ylabel('Частота')
    plt.show()
else:
    print("Не удалось извлечь цены.")
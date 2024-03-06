import pandas as pd # Импортируем библиотеку Pandas.

city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723],
        'Население': [11.9, 4.9, 1.5, 1.4]} # Создаём словарь с нужной информацией о городах.

df = pd.DataFrame(city) # Превращаем словарь в DataFrame, используя стандартный метод библиотеки.

df # Выводим DataFrame на экран.
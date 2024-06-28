import requests, sqlite3, os
from tkinter import messagebox
import datetime

connect = sqlite3.connect('myweather.db')
cursor = connect.cursor()

cursor.execute('SELECT city FROM account ORDER BY rowid DESC LIMIT 1')
last_city = cursor.fetchone()

cursor.execute('SELECT country FROM account ORDER BY rowid DESC LIMIT 1')
last_country = cursor.fetchone()

connect.commit()
connect.close()


api_key = 'ac90bee491d306ada1c92f65cd9f3482'
first_city_name = f'{last_city[0]}'
lang = 'ua'

first_url = f'https://api.openweathermap.org/data/2.5/weather?q={first_city_name}&appid={api_key}&lang={lang}'

first_responce = requests.get(first_url)
print(first_responce)

if first_responce.status_code == 200:    
    first_data = first_responce.json()
    first_main_data = first_data['main']
    
    first_temperature = first_main_data['temp']
    first_celsiy = first_temperature - 273.15
    first_celsiy = round(first_celsiy)
    first_max = first_main_data['temp_max'] - 273.15
    first_max = round(first_max)
    first_min = first_main_data['temp_min'] - 273.15
    first_min = round(first_min)
    first_humidity = first_main_data['humidity']
    first_description = first_data['weather'][0]['description']
    print(first_description)
    first_wind = first_data['wind']['speed']

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={first_city_name}&appid={api_key}&lang={lang}'

    responce = requests.get(url)

    if responce.status_code == 200:
        data = responce.json()

        first_hour = round(data['list'][0]['main']['temp'] - 273.15)
        firstdescription = data['list'][0]['weather'][0]['description']

        second_hour = round(data['list'][1]['main']['temp'] - 273.15)
        seconddescription = data['list'][1]['weather'][0]['description']

        third_hour = round(data['list'][2]['main']['temp'] - 273.15)
        thirddescription = data['list'][2]['weather'][0]['description']

        fourth_hour = round(data['list'][3]['main']['temp'] - 273.15)
        fourthdescription = data['list'][3]['weather'][0]['description']

        fifth_hour = round(data['list'][4]['main']['temp'] - 273.15)
        fifthdescription = data['list'][4]['weather'][0]['description']

        print(fourthdescription)
        sixth_hour = round(data['list'][5]['main']['temp'] - 273.15)
        sixthdescription = data['list'][5]['weather'][0]['description']

        seventh_hour = round(data['list'][6]['main']['temp'] - 273.15)
        seventhdescription = data['list'][6]['weather'][0]['description']

        eighth_hour = round(data['list'][7]['main']['temp'] - 273.15)
        eighthdescription = data['list'][7]['weather'][0]['description']

        nineth_hour = round(data['list'][8]['main']['temp'] - 273.15)
        ninethdescription = data['list'][8]['weather'][0]['description']


if first_responce.status_code == 404:
    messagebox.showerror("Помилка!", "Назва міста не корректна, введіть вірні дані!")
if first_responce.status_code == 400:
    messagebox.showerror("Помилка!", "Ви не задали місто!")


# 
api_key = 'ac90bee491d306ada1c92f65cd9f3482'
kyiv_city_name = 'Київ'
lang = 'ua'

kyiv_url = f'https://api.openweathermap.org/data/2.5/weather?q={kyiv_city_name}&appid={api_key}&lang={lang}'

kyiv_responce = requests.get(kyiv_url)

if kyiv_responce.status_code == 200:    
    kyiv_data = kyiv_responce.json()
    kyiv_main_data = kyiv_data['main']

    kyiv_temperature = kyiv_main_data['temp']
    kyiv_celsiy = kyiv_temperature - 273.15
    kyiv_celsiy = round(kyiv_celsiy)
    kyiv_max = kyiv_main_data['temp_max'] - 273.15
    kyiv_max = round(kyiv_max)
    kyiv_min = kyiv_main_data['temp_min'] - 273.15
    kyiv_min = round(kyiv_min)
    kyiv_humidity = kyiv_main_data['humidity']
    kyiv_description = kyiv_data['weather'][0]['description']
    kyiv_wind = kyiv_data['wind']['speed']
    # kyiv_max_temp = kyiv_data['max_temp']
# 





api_key = 'ac90bee491d306ada1c92f65cd9f3482'
rome_city_name = 'Рим'
lang = 'ua'

rome_url = f'https://api.openweathermap.org/data/2.5/weather?q={rome_city_name}&appid={api_key}&lang={lang}'

rome_responce = requests.get(rome_url)

if rome_responce.status_code == 200:    
    rome_data = rome_responce.json()
    rome_main_data = rome_data['main']
    rome_temperature = rome_main_data['temp']
    rome_max = rome_main_data['temp_max'] -273.15
    rome_max = round(rome_max)
    rome_min = rome_main_data['temp_min'] - 273.15
    rome_min = round(rome_min)
    rome_celsiy = rome_temperature - 273.15
    rome_celsiy = round(rome_celsiy)
    rome_humidity = rome_main_data['humidity']
    rome_description = rome_data['weather'][0]['description']
    rome_wind = rome_data['wind']['speed']
# 



api_key = 'ac90bee491d306ada1c92f65cd9f3482'
london_city_name = 'Лондон'
lang = 'ua'

london_url = f'https://api.openweathermap.org/data/2.5/weather?q={london_city_name}&appid={api_key}&lang={lang}'

london_responce = requests.get(london_url)

if london_responce.status_code == 200:    
    london_data = london_responce.json()
    london_main_data = london_data['main']
    london_temperature = london_main_data['temp']
    london_max = london_main_data['temp_max'] -273.15
    london_max =round(london_max)
    london_min = london_main_data['temp_min']-273.15
    london_min =round(london_min)
    london_celsiy = london_temperature - 273.15
    london_celsiy = round(london_celsiy)
    london_humidity = london_main_data['humidity']
    london_description = london_data['weather'][0]['description']
    london_wind = london_data['wind']['speed']

api_key = 'ac90bee491d306ada1c92f65cd9f3482'
warsaw_city_name = 'Варшава'
lang = 'ua'

warsaw_url = f'https://api.openweathermap.org/data/2.5/weather?q={warsaw_city_name}&appid={api_key}&lang={lang}'

warsaw_responce = requests.get(warsaw_url)

if warsaw_responce.status_code == 200:    
    warsaw_data = warsaw_responce.json()
    warsaw_main_data = warsaw_data['main']
    warsaw_temperature = warsaw_main_data['temp']
    warsaw_max = warsaw_main_data['temp_max'] - 273.15
    warsaw_max = round(warsaw_max)
    warsaw_min = warsaw_main_data['temp_min'] - 273.15
    warsaw_min = round(warsaw_min)
    warsaw_celsiy = warsaw_temperature - 273.15
    warsaw_celsiy = round(warsaw_celsiy)
    warsaw_humidity = warsaw_main_data['humidity']
    warsaw_description = warsaw_data['weather'][0]['description']
    warsaw_wind = warsaw_data['wind']['speed']

api_key = 'ac90bee491d306ada1c92f65cd9f3482'
prague_city_name = 'Прага'
lang = 'ua'

prague_url = f'https://api.openweathermap.org/data/2.5/weather?q={prague_city_name}&appid={api_key}&lang={lang}'

prague_responce = requests.get(prague_url)

if prague_responce.status_code == 200:    
    prague_data = prague_responce.json()
    prague_main_data = prague_data['main']
    prague_temperature = prague_main_data['temp']
    prague_max = prague_main_data['temp_max'] - 273.15
    prague_max = round(prague_max)
    prague_min = prague_main_data['temp_min'] - 273.15
    prague_min = round(prague_min)
    prague_celsiy = prague_temperature - 273.15
    prague_celsiy = round(prague_celsiy)
    prague_humidity = prague_main_data['humidity']
    prague_description = prague_data['weather'][0]['description']
    prague_wind = prague_data['wind']['speed']

def refresh_in_widget():
    
    api_key = 'ac90bee491d306ada1c92f65cd9f3482'
    refresh_city_name = 'Київ'
    lang = 'ua'

    refresh_url = f'https://api.openweathermap.org/data/2.5/weather?q={refresh_city_name}&appid={api_key}&lang={lang}'

    refresh_responce = requests.get(refresh_url)

    if refresh_responce.status_code == 200:    
        refresh_data = refresh_responce.json()
        refresh_main_data = refresh_data['main']

        refresh_temperature = refresh_main_data['temp']
        refresh_celsiy = refresh_temperature - 273.15
        refresh_celsiy = round(refresh_celsiy)
        refresh_max = refresh_main_data['temp_max'] - 273.15
        refresh_max = round(refresh_max)
        refresh_min = refresh_main_data['temp_min'] - 273.15
        refresh_min = round(refresh_min)
        refresh_humidity = refresh_main_data['humidity']
        refresh_description = refresh_data['weather'][0]['description']
        refresh_wind = refresh_data['wind']['speed']
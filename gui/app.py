from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import customtkinter
import sqlite3
import os
from datetime import datetime
import api_file as api
import requests
#import pytz

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  #Themes: "blue" (standard), "green", "dark-blue"

# API
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color="#5DA7B1")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images2")

        # WINDOW CONFIG
        self.title("MyWeather")
        self.geometry("1200x800")
        self.iconbitmap(__file__ + r'/../icon.ico')
        self.resizable(0, 0)

        connect = sqlite3.connect('myweather.db')
        cursor = connect.cursor()

        cursor.execute('SELECT name FROM account ORDER BY rowid DESC LIMIT 1')
        name = cursor.fetchone()
        cursor.execute('SELECT last_name FROM account ORDER BY rowid DESC LIMIT 1')
        lasty_name = cursor.fetchone()
        connect.commit()
        connect.close()
        # Time    
        def getdate():

            global time

            now = datetime.now()

            day = now.strftime("%A")
            current_date_time = now.strftime("%d.%m.%Y")
            time = now.strftime("%H:%M")
            dataDate.configure(text=current_date_time)
            dataDay.configure(text=day)
            dataTime.configure(text=time)
            self.after(8000, getdate)

        def set_status():
            moon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"moon.png")), size=(180, 180))
            storm = customtkinter.CTkImage(Image.open(os.path.join(image_path, r'storm.png')), size=(180,180))

            sunny = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(180, 180))
            sun = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sun.png")), size=(180, 180))
            sunny1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny1.png")), size=(180, 180))
            sunrise = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunrise.png")), size=(180, 180))
            sunset = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunset.png")), size=(180, 180))
            
            snowy1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"snowy.png")), size=(171 ,159))
            snowy = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"snowy.png")), size=(171 ,159))
            snow = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"snow.png")), size=(171 ,159))

            rain = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain.png")), size=(180, 180))
            rain_cloud = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain_cloud.png")), size=(180, 180))
            rainy = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rainy.png")), size=(180, 180))


                #  __________________________________________________________________________________________________

            _moon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"moon.png")), size=(50, 50))
            _storm = customtkinter.CTkImage(Image.open(os.path.join(image_path, r'storm.png')), size=(50,50))
            _sunny = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(50, 50))
            _sun = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sun.png")), size=(50, 50))
            _sunny1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny1.png")), size=(50, 50))
            _sunrise = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunrise.png")), size=(50, 50))
            _sunset = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunset.png")), size=(50, 50))
            _snowy1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"snowy.png")), size=(50, 50))
            _snowy = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"snowy.png")), size=(50, 50))
            _snow = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"snow.png")), size=(50, 50))
            _rain = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain.png")), size=(50, 50))
            _rain_cloud = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain_cloud.png")), size=(50, 50))
            _rainy = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rainy.png")), size=(50, 50))

            
            if api.first_description == "сонце":
                weatherStatusFrame.configure(image=sunny)
            elif api.first_description == "хмарно" and time <= "20:00":
             weatherStatusFrame.configure(image=moon)
            elif api.first_description == "хмарно" and time >= "20:00":
                weatherStatusFrame.configure(image=moon)
            elif api.first_description == "сніг" and time >= "20:00":
                weatherStatusFrame.configure(image=snowy1)
            elif api.first_description == "дощ" and time >= "20:00":
                weatherStatusFrame.configure(image=snow)
            elif api.first_description == "сніг":
                weatherStatusFrame.configure(image=snowy)
            elif api.first_description == "дощ":
                weatherStatusFrame.configure(image=rain)
            elif api.first_description == "захід сонця":
                weatherStatusFrame.configure(image=sunset)
            elif api.first_description == "схід сонця":
                weatherStatusFrame.configure(image=sunrise)
            elif api.first_description == "шторм":
                weatherStatusFrame.configure(image=storm)

            # 1
            if api.firstdescription == "сонце" and time <= "20:00" :
                inposicon.configure(image=_sun)
                print(api.firstdescription)
            if api.firstdescription == "сонце" and time >= "20:00" :
                inposicon.configure(image=_moon)
            if api.firstdescription == "легкий дощ" and time >='20:00':
                inposicon.configure(image=_rain_cloud)
            if api.firstdescription == "легкий дощ" and time <= '20:00':
                inposicon.configure(image=_rain)
            if api.firstdescription == 'помірний дощ' and time <= '20:00':
                inposicon.configure(image = _rain)
            if api.firstdescription == "помірний дощ" and time >='20:00':
                inposicon.configure(image=_rain_cloud)
            if api.firstdescription == 'хмарно' and time >= '20:00':
                inposicon.configure(image = _snow)
            if api.firstdescription == 'хмарно' and time <= '20:00':
                inposicon.configure(image = _sunny)
            if api.firstdescription == 'рвані хмари' and time <= '20:00':
                inposicon.configure(image = _sunny1)
            if api.firstdescription == 'рвані хмари' and time >= '20:00':
                inposicon.configure(Image =_moon)
            if api.firstdescription == 'чисте небо ' and time <= '20:00':
                inposicon.configure(image =_sun)
            if api.firstdescription == 'чисте небо ' and time >= '20:00':
                inposicon.configure(image = _moon)
            if api.firstdescription == 'сніг ' and time <= '20:00':
                inposicon.configure(image = _snowy)
            if api.firstdescription == 'сніг ' and time >= '20:00': 
                inposicon.configure(image = _snowy1)  
            if api.firstdescription == 'легкий сніг ' and time <= '20:00':
                inposicon.configure(image = _snowy)  
            if api.firstdescription == 'легкий сніг ' and time >= '20:00':
                inposicon.configure(image = _snowy1)  
            #2 
            if api.seconddescription == "сонце" and time <= "20:00" : inposicon2.configure(image=_sun)
            if api.seconddescription == "сонце" and time >= "20:00" : inposicon2.configure(image=_moon)
            if api.seconddescription == "легкий дощ" and time >='20:00': inposicon2.configure(image=_rain_cloud)
            if api.seconddescription == "легкий дощ" and time <= '20:00': inposicon.configure(image=_rain)
            if api.seconddescription == 'помірний дощ' and time <= '20:00': inposicon2.configure(image = _rain)
            if api.seconddescription == "помірний дощ" and time >='20:00': inposicon2.configure(image=_rain_cloud)
            if api.seconddescription == 'хмарно' and time >= '20:00': inposicon.configure(image = _snow)
            if api.seconddescription == 'хмарно' and time <= '20:00': inposicon2.configure(image = _sunny)
            if api.seconddescription == 'рвані хмари' and time <= '20:00': inposicon.configure(image = _sunny1)
            if api.seconddescription == 'рвані хмари' and time >= '20:00': inposicon2.configure(Image =_moon)
            if api.seconddescription == 'чисте небо ' and time <= '20:00': inposicon.configure(image =_sun)
            if api.seconddescription == 'чисте небо ' and time >= '20:00':inposicon2.configure(image = _moon)
            if api.seconddescription == 'сніг ' and time <= '20:00': inposicon.configure(image = _snowy)
            if api.seconddescription == 'сніг ' and time >= '20:00': inposicon2.configure(image = _snowy1)  
            if api.seconddescription == 'легкий сніг ' and time <= '20:00':
                inposicon2.configure(image = _snowy)  
            if api.seconddescription == 'легкий сніг ' and time >= '20:00':
                inposicon2.configure(image = _snowy1) 
            # 3
            if api.thirddescription == "сонце" and time <= "20:00" :
                inposicon3.configure(image=_sun)
            if api.thirddescription == "сонце" and time >= "20:00" :
                inposicon3.configure(image=_moon)
            if api.thirddescription == "легкий дощ" and time >='20:00':
                inposicon3.configure(image=_rain_cloud)
            if api.thirddescription == "легкий дощ" and time <= '20:00':
                inposicon3.configure(image=_rain)
            if api.thirddescription == 'помірний дощ' and time <= '20:00':
                inposicon3.configure(image = _rain)
            if api.thirddescription == "помірний дощ" and time >='20:00':
                inposicon3.configure(image=_rain_cloud)
            if api.thirddescription == 'хмарно' and time >= '20:00':
                inposicon3.configure(image = _snow)
            if api.thirddescription == 'хмарно' and time <= '20:00':
                inposicon3.configure(image = _sunny)
            if api.thirddescription == 'рвані хмари' and time <= '20:00':
                inposicon3.configure(image = _sunny1)
            if api.thirddescription == 'рвані хмари' and time >= '20:00':
                inposicon3.configure(Image =_moon)
            if api.thirddescription == 'чисте небо ' and time <= '20:00':
                inposicon3.configure(image =_sun)
            if api.thirddescription == 'чисте небо ' and time >= '20:00':
                inposicon3.configure(image = _moon)
            if api.thirddescription == 'сніг ' and time <= '20:00':
                inposicon3.configure(image = _snowy)
            if api.thirddescription == 'сніг ' and time >= '20:00': 
                inposicon3.configure(image = _snowy1)  
            if api.thirddescription == 'легкий сніг ' and time <= '20:00':
                inposicon3.configure(image = _snowy)  
            if api.thirddescription == 'легкий сніг ' and time >= '20:00':
                inposicon3.configure(image = _snowy1) 
            # 4
            if api.fourthdescription == "сонце" and time <= "20:00" :
                inposicon4.configure(image=_sun)
            if api.fourthdescription == "сонце" and time >= "20:00" :
                inposicon4.configure(image=_moon)
            if api.fourthdescription == "легкий дощ" and time >='20:00':
                inposicon4.configure(image=_rain_cloud)
            if api.fourthdescription == "легкий дощ" and time <= '20:00':
                inposicon4.configure(image=_rain)
            if api.fourthdescription == 'помірний дощ' and time <= '20:00':
                inposicon4.configure(image = _rain)
            if api.fourthdescription == "помірний дощ" and time >='20:00':
                inposicon4.configure(image=_rain_cloud)
            if api.fourthdescription == 'хмарно' and time >= '20:00':
                inposicon.configure(image = _snow)
            if api.fourthdescription == 'хмарно' and time <= '20:00':
                inposicon4.configure(image = _sunny)
            if api.fourthdescription == 'рвані хмари' and time <= '20:00':
                inposicon4.configure(image = _sunny1)
            if api.fourthdescription == 'рвані хмари' and time >= '20:00':
                inposicon4.configure(Image =_moon)
            if api.fourthdescription == 'чисте небо ' and time <= '20:00':
                inposicon4.configure(image =_sun)
            if api.fourthdescription == 'чисте небо ' and time >= '20:00':
                inposicon4.configure(image = _moon)
            if api.fourthdescription == 'сніг ' and time <= '20:00':
                inposicon.configure(image = _snowy)
            if api.fourthdescription == 'сніг ' and time >= '20:00': 
                inposicon4.configure(image = _snowy1)  
            if api.fourthdescription == 'легкий сніг ' and time <= '20:00':
                inposicon4.configure(image = _snowy)  
            if api.fourthdescription == 'легкий сніг ' and time >= '20:00':
                inposicon4.configure(image = _snowy1)
            # 5



            if api.fifthdescription == "сонце" and time <= "20:00" :
                inposicon5.configure(image=_sun)
            if api.fifthdescription == "сонце" and time >= "20:00" :
                inposicon5.configure(image=_moon)
            if api.fifthdescription == "легкий дощ" and time >='20:00':
                inposicon5.configure(image=_rain_cloud)
            if api.fifthdescription == "легкий дощ" and time <= '20:00':
                inposicon5.configure(image=_rain)
            if api.fifthdescription == 'помірний дощ' and time <= '20:00':
                inposicon5.configure(image = _rain)
            if api.fifthdescription == "помірний дощ" and time >='20:00':
                inposicon5.configure(image=_rain_cloud)
            if api.fifthdescription == 'хмарно' and time >= '20:00':
                inposicon5.configure(image = _snow)
            if api.fifthdescription == 'хмарно' and time <= '20:00':
                inposicon5.configure(image = _sunny)
            if api.fifthdescription == 'рвані хмари' and time <= '20:00':
                inposicon5.configure(image = _sunny1)
            if api.fifthdescription == 'рвані хмари' and time >= '20:00':
                inposicon5.configure(Image =_moon)
            if api.fifthdescription == 'чисте небо ' and time <= '20:00':
                inposicon5.configure(image =_sun)
            if api.fifthdescription == 'чисте небо ' and time >= '20:00':
                inposicon.configure(image = _moon)
            if api.fifthdescription == 'сніг ' and time <= '20:00':
                inposicon.configure(image = _snowy)
            if api.fifthdescription == 'сніг ' and time >= '20:00': 
                inposicon5.configure(image = _snowy1)  
            if api.fifthdescription == 'легкий сніг ' and time <= '20:00':
                inposicon5.configure(image = _snowy)  
            if api.fifthdescription == 'легкий сніг ' and time >= '20:00':
                inposicon5.configure(image = _snowy1) 
            # 6
            if api.sixthdescription == "сонце" and time <= "20:00" :
                inposicon6.configure(image=_sun)
            if api.sixthdescription == "сонце" and time >= "20:00" :
                inposicon6.configure(image=_moon)
            if api.sixthdescription == "легкий дощ" and time >='20:00':
                inposicon6.configure(image=_rain_cloud)
            if api.sixthdescription == "легкий дощ" and time <= '20:00':
                inposicon6.configure(image=_rain)
            if api.sixthdescription == 'помірний дощ' and time <= '20:00':
                inposicon6.configure(image = _rain)
            if api.sixthdescription == "помірний дощ" and time >='20:00':
                inposicon6.configure(image=_rain_cloud)
            if api.sixthdescription == 'хмарно' and time >= '20:00':
                inposicon6.configure(image = _snow)
            if api.sixthdescription == 'хмарно' and time <= '20:00':
                inposicon6.configure(image = _sunny)
            if api.sixthdescription == 'рвані хмари' and time <= '20:00':
                inposicon6.configure(image = _sunny1)
            if api.sixthdescription == 'рвані хмари' and time >= '20:00':
                inposicon6.configure(Image =_moon)
            if api.sixthdescription == 'чисте небо ' and time <= '20:00':
                inposicon6.configure(image =_sun)
            if api.sixthdescription == 'чисте небо ' and time >= '20:00':
                inposicon6.configure(image = _moon)
            if api.sixthdescription == 'сніг ' and time <= '20:00':
                inposicon6.configure(image = _snowy)
            if api.sixthdescription == 'сніг ' and time >= '20:00': 
                inposicon6.configure(image = _snowy1)  
            if api.sixthdescription == 'легкий сніг ' and time <= '20:00':
                inposicon6.configure(image = _snowy)  
            if api.sixthdescription == 'легкий сніг ' and time >= '20:00':
                inposicon6.configure(image = _snowy1)
            # 7
            if api.seventhdescription == "сонце" and time <= "20:00" :
                inposicon7.configure(image=_sun)
            if api.seventhdescription == "сонце" and time >= "20:00" :
                inposicon7.configure(image=_moon)
            if api.seventhdescription == "легкий дощ" and time >='20:00':
                inposicon7.configure(image=_rain_cloud)
            if api.seventhdescription == "легкий дощ" and time <= '20:00':
                inposicon7.configure(image=_rain)
            if api.seventhdescription == 'помірний дощ' and time <= '20:00':
                inposicon7.configure(image = _rain)
            if api.seventhdescription == "помірний дощ" and time >='20:00':
                inposicon7.configure(image=_rain_cloud)
            if api.seventhdescription == 'хмарно' and time >= '20:00':
                inposicon7.configure(image = _snow)
            if api.seventhdescription == 'хмарно' and time <= '20:00':
                inposicon7.configure(image = _sunny)
            if api.seventhdescription == 'рвані хмари' and time <= '20:00':
                inposicon7.configure(image = _sunny1)
            if api.seventhdescription == 'рвані хмари' and time >= '20:00':
                inposicon7.configure(Image =_moon)
            if api.seventhdescription == 'чисте небо ' and time <= '20:00':
                inposicon7.configure(image =_sun)
            if api.seventhdescription == 'чисте небо ' and time >= '20:00':
                inposicon7.configure(image = _moon)
            if api.seventhdescription == 'сніг ' and time <= '20:00':
                inposicon7.configure(image = _snowy)
            if api.seventhdescription == 'сніг ' and time >= '20:00': 
                inposicon7.configure(image = _snowy1)  
            if api.seventhdescription == 'легкий сніг ' and time <= '20:00':
                inposicon7.configure(image = _snowy)  
            if api.seventhdescription == 'легкий сніг ' and time >= '20:00':
                inposicon7.configure(image = _snowy1) 
            # 8
            if api.eighthdescription == "сонце" and time <= "20:00" :
                inposicon8.configure(image=_sun)
            if api.eighthdescription == "сонце" and time >= "20:00" :
                inposicon8.configure(image=_moon)
            if api.eighthdescription == "легкий дощ" and time >='20:00':
                inposicon8.configure(image=_rain_cloud)
            if api.eighthdescription == "легкий дощ" and time <= '20:00':
                inposicon8.configure(image=_rain)
            if api.eighthdescription == 'помірний дощ' and time <= '20:00':
                inposicon8.configure(image = _rain)
            if api.eighthdescription == "помірний дощ" and time >='20:00':
                inposicon8.configure(image=_rain_cloud)
            if api.eighthdescription == 'хмарно' and time >= '20:00':
                inposicon8.configure(image = _snow)
            if api.eighthdescription == 'хмарно' and time <= '20:00':
                inposicon8.configure(image = _sunny)
            if api.eighthdescription == 'рвані хмари' and time <= '20:00':
                inposicon8.configure(image = _sunny1)
            if api.eighthdescription == 'рвані хмари' and time >= '20:00':
                inposicon8.configure(Image =_moon)
            if api.eighthdescription == 'чисте небо ' and time <= '20:00':
                inposicon8.configure(image =_sun)
            if api.eighthdescription == 'чисте небо ' and time >= '20:00':
                inposicon8.configure(image = _moon)
            if api.eighthdescription == 'сніг ' and time <= '20:00':
                inposicon8.configure(image = _snowy)
            if api.eighthdescription == 'сніг ' and time >= '20:00': 
                inposicon8.configure(image = _snowy1)  
            if api.eighthdescription == 'легкий сніг ' and time <= '20:00':
                inposicon8.configure(image = _snowy)  
            if api.eighthdescription == 'легкий сніг ' and time >= '20:00':
                inposicon8.configure(image = _snowy1) 
            # 9
            if api.ninethdescription == "сонце" and time <= "20:00" :
                inposicon9.configure(image=_sun)
            if api.ninethdescription == "сонце" and time >= "20:00" :
                inposicon9.configure(image=_moon)
            if api.ninethdescription == "легкий дощ" and time >='20:00':
                inposicon9.configure(image=_rain_cloud)
            if api.ninethdescription == "легкий дощ" and time <= '20:00':
                inposicon9.configure(image=_rain)
            if api.ninethdescription == 'помірний дощ' and time <= '20:00':
                inposicon9.configure(image = _rain)
            if api.ninethdescription == "помірний дощ" and time >='20:00':
                inposicon9.configure(image=_rain_cloud)
            if api.ninethdescription == 'хмарно' and time >= '20:00':
                inposicon9.configure(image = _snow)
            if api.ninethdescription == 'хмарно' and time <= '20:00':
                inposicon9.configure(image = _sunny)
            if api.ninethdescription == 'рвані хмари' and time <= '20:00':
                inposicon9.configure(image = _sunny1)
            if api.ninethdescription == 'рвані хмари' and time >= '20:00':
                inposicon9.configure(Image =_moon)
            if api.ninethdescription == 'чисте небо ' and time <= '20:00':
                inposicon9.configure(image =_sun)
            if api.ninethdescription == 'чисте небо ' and time >= '20:00':
                inposicon9.configure(image = _moon)
            if api.ninethdescription == 'сніг ' and time <= '20:00':
                inposicon9.configure(image = _snowy)
            if api.ninethdescription == 'сніг ' and time >= '20:00': 
                inposicon9.configure(image = _snowy1)  
            if api.ninethdescription == 'легкий сніг ' and time <= '20:00':
                inposicon9.configure(image = _snowy)  
            if api.ninethdescription == 'легкий сніг ' and time >= '20:00':
                inposicon9.configure(image = _snowy1)  
            

            
            

            

            self.after(8000, set_status)

        def search():

            global user_query

            user_query = searchInput.get().replace(" ", "")
            
            api_key = 'ac90bee491d306ada1c92f65cd9f3482'
            _city_name = f'{user_query}'.lower().capitalize()
            lang = 'ua'

            _url = f'https://api.openweathermap.org/data/2.5/weather?q={_city_name}&appid={api_key}&lang={lang}'

            _responce = requests.get(_url)

            if _responce.status_code == 200:    
                _data = _responce.json()
                _main_data = _data['main']
                _temperature = _main_data['temp']
                _max = _main_data['temp_max']  - 273.15
                _max = round(_max)
                _min = _main_data['temp_min']  - 273.15
                _min = round(_min)
                _celsiy = _temperature - 273.15
                _celsiy = round(_celsiy)
                _humidity = _main_data['humidity']
                _description = _data['weather'][0]['description']
                _wind = _data['wind']['speed']

                self.cityName.configure(text=user_query)
                self.degreesLabel.configure(text=f'{_celsiy}°')
                self.weatherShortDesc.configure(text=f'{_description}')
                self.downarrowimg.configure(text=f'{_min}°')
                self.uparrowimg.configure(text=f'{_max}°')
            else:
                messagebox.showerror("MyWeather", "Не правильно введені данні.")

        
        weatherScroll = customtkinter.CTkScrollableFrame(self, width=275, height=800, fg_color="#096C82", corner_radius=0, scrollbar_button_color="#C5DFE3", scrollbar_button_hover_color="#B5CCCF", scrollbar_fg_color="#085769")
        weatherScroll.pack(anchor=tk.NW)

        kiev_tz = 'Europe/Kiev'
        varshava_tz = 'Europe/Warsaw'
        rim_tz = 'Europe/Rome'
        praga_tz = 'Europe/Prague'
        
        cities = {
            'Kiev': kiev_tz,
            'Varshava': varshava_tz,
            'Rim': rim_tz,
            'Praga': praga_tz,
        }
        

        self.weatherStat = customtkinter.CTkButton(weatherScroll, width=275, height=90, fg_color="#4599A4", border_width=2, corner_radius=20, border_color="white", text="", hover=False, command = self.pochtidevyatkayoU)
        self.weatherStat.pack(pady=15, padx=10)

        weatherStatDegrees = customtkinter.CTkLabel(self.weatherStat, text='11' + '°', text_color="white", font=('Roboto Slab Thin',80))

        maxDegree = customtkinter.CTkLabel(self.weatherStat, text=f'Максимальна' + f'{api.first_max}' + '°', text_color="#FFFFFF", font=('Roboto Slab Bold',40))
        
        minDegree = customtkinter.CTkLabel(self.weatherStat, text=f'Мінімальна' + f'{api.first_min}' + '°', text_color="#FFFFFF", font=('Roboto Slab Bold',40))
        
        self.potochna = customtkinter.CTkLabel(self.weatherStat, text='Поточна Позиція', fg_color='transparent', text_color="white", font=('Roboto Slab Bold',16))
        self.potochna.place(x=8,y=8)

        self.weatherStatName = customtkinter.CTkLabel(self.weatherStat, text=api.first_city_name.lower().capitalize(),fg_color='transparent', text_color="white", font=('Roboto Slab Bold', 12))
        self.weatherStatName.place(x=14,y=33)

        self.weatherStatDegrees = customtkinter.CTkLabel(self.weatherStat, text=f'{api.first_celsiy}' + '°', text_color="white", font=('Roboto Slab Bold',40))
        self.weatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        self.weatherStatDesc = customtkinter.CTkLabel(self.weatherStat, text=f"{api.first_description}", text_color="#FFFFFF", font=('Roboto Slab Bold',13))
        self.weatherStatDesc.place(x=7, y=55)

        self.weatherStatminmax = customtkinter.CTkLabel(self.weatherStat, text=f'макс.:{api.first_max}°, мін.:{api.first_min}',fg_color="#096C82", font=('Roboto Slab Bold',12), text_color='white')
        self.weatherStatminmax.place(x=146,y=58)

        self.kiivWeatherStat = customtkinter.CTkButton(weatherScroll, width=275, height=90, fg_color="#096C82", corner_radius=20, border_width=2, border_color="white", hover=False, text="", command=self.kyiv)
        self.kiivWeatherStat.pack(pady=15, padx=10)

        self.kiivWeatherStatName = customtkinter.CTkLabel(self.kiivWeatherStat, text=api.kyiv_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        self.kiivWeatherStatName.place(relx=0.14, rely=0.23, anchor=tk.CENTER)

        self.kiivWeatherStatDegrees = customtkinter.CTkLabel(self.kiivWeatherStat, text=f"{api.kyiv_celsiy}" + "°", text_color="white", font=('Roboto Slab Bold',40))
        self.kiivWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        self.kiivWeatherStatDesc = customtkinter.CTkLabel(self.kiivWeatherStat, text=api.kyiv_description, text_color="white", font=('Roboto Slab Bold',13))
        self.kiivWeatherStatDesc.place(x=14, y=55)
        self.kiivWeatherStatminmax = customtkinter.CTkLabel(self.kiivWeatherStat, text=f'макс.:{api.kyiv_max}°, мін.:{api.kyiv_min}', fg_color="#096C82", font=('Roboto Slab Bold',12), text_color='white')
        self.kiivWeatherStatminmax.place(x=146,y=58)

        self.romeWeatherStat = customtkinter.CTkButton(weatherScroll,  width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white", hover=False, text="", command=self.rome)
        self.romeWeatherStat.pack(pady=15, padx=10)

        self.romeWeatherStatName = customtkinter.CTkLabel(self.romeWeatherStat, text=f"{api.rome_city_name}", fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        self.romeWeatherStatName.place(relx=0.14, rely=0.23, anchor=tk.CENTER)

        self.romeWeatherStatDegrees = customtkinter.CTkLabel(self.romeWeatherStat, text=f'{api.rome_celsiy}' + '°', text_color="white", font=('Roboto Slab Bold',40))
        self.romeWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        self.romeWeatherStatDesc = customtkinter.CTkLabel(self.romeWeatherStat, text=api.rome_description, text_color="white", font=('Roboto Slab Bold',13))
        self.romeWeatherStatDesc.place(x=14, y=55)
        self.romeWeatherStatminmax = customtkinter.CTkLabel(self.romeWeatherStat, text=f'макс.:{api.rome_max}°, мін.:{api.rome_min}',fg_color="#096C82", font=('Roboto Slab Bold',12), text_color='white').place(x=146,y=58)

        self.londonWeatherStat = customtkinter.CTkButton(weatherScroll, width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white", hover=False, text="", command=self.london)
        self.londonWeatherStat.pack(pady=15, padx=10)

        self.londonWeatherStatName = customtkinter.CTkLabel(self.londonWeatherStat, text=api.london_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        self.londonWeatherStatName.place(relx=0.19, rely=0.23, anchor=tk.CENTER)

        self.londonWeatherStatDegrees = customtkinter.CTkLabel(self.londonWeatherStat, text=f'{api.london_celsiy}' + "°", text_color="white", font=('Roboto Slab Bold',40))
        self.londonWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        self.londonWeatherStatDesc = customtkinter.CTkLabel(self.londonWeatherStat, text=api.london_description, text_color="white", font=('Roboto Slab Bold',13))
        self.londonWeatherStatDesc.place(x=14, y=55)
        self.londonWeatherStatminmax = customtkinter.CTkLabel(self.londonWeatherStat, text=f'макс.:{api.london_max}°, мін.:{api.london_min}',fg_color="#096C82", font=('Roboto Slab Bold',12), text_color='white').place(x=146,y=58)

        self.warsawWeatherStat = customtkinter.CTkButton(weatherScroll, width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white", hover=False, text="", command=self.warsaw)
        self.warsawWeatherStat.pack(pady=15, padx=10)

        self.warsawWeatherStatName = customtkinter.CTkLabel(self.warsawWeatherStat, text=api.warsaw_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        self.warsawWeatherStatName.place(relx=0.2, rely=0.23, anchor=tk.CENTER)

        self.warsawWeatherStatDegrees = customtkinter.CTkLabel(self.warsawWeatherStat, text=f'{api.warsaw_celsiy}' + "°", text_color="white", font=('Roboto Slab Bold',40))
        self.warsawWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        self.warsawWeatherStatDesc = customtkinter.CTkLabel(self.warsawWeatherStat, text=api.warsaw_description, text_color="white", font=('Roboto Slab Bold',13))
        self.warsawWeatherStatDesc.place(x=14, y=55)
        self.warsawWeatherStatminmax = customtkinter.CTkLabel(self.warsawWeatherStat, text=f'макс.:{api.warsaw_max}°, мін.:{api.warsaw_min}', font=('Roboto Slab Bold',12),fg_color="#096C82", text_color='white').place(x=146,y=58)

        
        self.pragueWeatherStat = customtkinter.CTkButton(weatherScroll, width=275, height=90, corner_radius=20, fg_color="#096C82", border_width=2, border_color="white", hover=False, text="", command=self.prague)
        self.pragueWeatherStat.pack(pady=15, padx=10)

        self.pragueWeatherStatName = customtkinter.CTkLabel(self.pragueWeatherStat, text=api.prague_city_name, fg_color="#096C82", text_color="white", font=('Roboto Slab Bold',20))
        self.pragueWeatherStatName.place(relx=0.17, rely=0.23, anchor=tk.CENTER)

        self.pragueWeatherStatDegrees = customtkinter.CTkLabel(self.pragueWeatherStat, text=f'{api.prague_celsiy}' + "°", text_color="white", font=('Roboto Slab Bold',40))
        self.pragueWeatherStatDegrees.place(relx=0.85, rely=0.4, anchor=tk.CENTER)

        self.pragueWeatherStatDesc = customtkinter.CTkLabel(self.pragueWeatherStat, text=api.prague_description, text_color="white", font=('Roboto Slab Bold',13))
        self.pragueWeatherStatDesc.place(x=14, y=55)
        self.pragueWeatherStatminmax = customtkinter.CTkLabel(self.pragueWeatherStat, text=f'макс.:{api.prague_max}°, мін.:{api.prague_min}', font=('Roboto Slab Bold',12),fg_color="#096C82", text_color='white').place(x=146,y=58)

        accounticon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(35,35))

        accountButton = customtkinter.CTkButton(self, width=40, height=40, fg_color="#5DA7B1", text="", hover_color="#5AA0AA", image=accounticon, command = self.opencabinet) #5DA7B1
        accountButton.place(relx=0.28, rely=0.05, anchor=tk.CENTER)

        accountUserName = customtkinter.CTkLabel(self, text=f"{name[0]} " + f"{lasty_name[0]}", text_color="white", font=('Roboto Slab Bold', 15), wraplength=180)
        accountUserName.place(relx=0.38, rely=0.05, anchor=tk.CENTER)

        
        searchframe = customtkinter.CTkFrame(self,width=300, height=40,corner_radius=100,border_width=3, border_color="#91DCE6" , fg_color="#096C82")
        searchframe.place(relx=0.86, rely=0.05, anchor=tk.CENTER)

        searchInput = customtkinter.CTkEntry(searchframe, width=230, height=30, fg_color='transparent', text_color="white", font=('Roboto Slab Bold',18), placeholder_text="Пошук міста...", placeholder_text_color="#91DCE6", border_width=0)
        searchInput.place(x=49,y=5)


        #weatherStatusIcon = ImageTk.PhotoImage(Image.open("/images/sunny.png"))

        weatherStatusIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(171, 171))

        searchIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"search.png")), size=(20, 20))

        searchButton = customtkinter.CTkButton(searchframe, width=40, height=20, corner_radius=100, text="", fg_color="#096C82", hover_color="#096C82", image=searchIcon, command=search)
        searchButton.place(x=9,y=6)

        potochnaMain = customtkinter.CTkLabel(self, text="Поточна позиція", font=('Roboto Slab Bold', 35), text_color="white")
        potochnaMain.place(x=544,y=97)

        weatherStatusFrame = customtkinter.CTkLabel(self, fg_color="#5DA7B1", width=171, height=159, image=weatherStatusIcon, text="")
        weatherStatusFrame.place(x=450,y=220, anchor = tk.CENTER)

        self.degreesLabel = customtkinter.CTkLabel(self, text=f'{api.first_celsiy}' + '°', fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Medium',80))
        self.degreesLabel.place(x=697,y=230, anchor = tk.CENTER)

        self.cityName = customtkinter.CTkLabel(self, text=f'{api.first_city_name.lower().capitalize()}', fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',22))
        self.cityName.place(x=689,y=162, anchor=tk.CENTER)

        self.weatherShortDesc = customtkinter.CTkLabel(self, text=api.first_description, fg_color="#5DA7B1", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        self.weatherShortDesc.place(x=638,y=284)

        downarrowimgico = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow1.png")), size=(25, 25))
        uparrowimgico = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow2.png")), size=(25, 25))
        
        self.downarrowimg = customtkinter.CTkLabel(self, text=f'{api.first_min}' + '°', text_color="white",image=downarrowimgico, compound='left', font=('Roboto Slab Bold',30))
        self.downarrowimg.place(x=623,y=350)

        self.uparrowimg = customtkinter.CTkLabel(self, text=f"{api.first_max}" + '°', text_color="white",image=uparrowimgico, compound='left', font=('Roboto Slab Bold',30))
        self.uparrowimg.place(x=688,y=350)

        dataDay = customtkinter.CTkLabel(self, text="day", fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',29))
        dataDay.place(relx=0.83, rely=0.18, anchor=tk.CENTER)

        dataDate = customtkinter.CTkLabel(self, text="date", fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',42))
        dataDate.place(relx=0.83, rely=0.25, anchor=tk.CENTER)

        dataTime = customtkinter.CTkLabel(self, text="time", fg_color="#5DA7B1", text_color="white", font=('Roboto Slab Bold',30))
        dataTime.place(relx=0.83, rely=0.32, anchor=tk.CENTER)

        left = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"left.png")), size=(8, 21))
        right = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"right.png")), size=(8, 21))

        leftSwitch = customtkinter.CTkButton(self, text=" ", width=30,image=left, height=30, corner_radius=10, fg_color="transparent")
        leftSwitch.place(x=292,y=524)

        rightSwitch = customtkinter.CTkButton(self, text=" ", width=30,image=right, height=30, corner_radius=10, fg_color="transparent")
        rightSwitch.place(x=1160,y=524)

        sunny = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(50, 50))
        rain = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain.png")), size=(50, 50))
        moon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"moon.png")), size=(50, 50))
        
        inlinePositionFrame = customtkinter.CTkFrame(self, width=818, height=240, corner_radius=20, fg_color="#5DA7B1", border_width=5, border_color="#E2F5F7")
        inlinePositionFrame.place(x=329,y=430)
                # ('Roboto Slab Bold',45)
        customtkinter.CTkLabel(inlinePositionFrame, text="Захід сонця о 16:05.  Очікується дощова погода приблизно о 19:00", text_color="white", font=("Roboto Slab Bold", 14)).pack(padx=10, pady=17) #23
        customtkinter.CTkFrame(inlinePositionFrame, width=818, height=3, fg_color="white").pack(pady=(0, 5)) #pady=(3, 10)

        inpos = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos.pack(side="left", padx=20, pady=26)

        inpostime = customtkinter.CTkLabel(inpos, text="Зараз", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime.pack()

        inposicon = customtkinter.CTkLabel(inpos, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon.pack()

        inposdeegres = customtkinter.CTkLabel(inpos, text=f"{api.first_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres.pack()

        inpos2 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos2.pack(side="left", padx=20, pady=10)

        inpostime2 = customtkinter.CTkLabel(inpos2, text="22:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime2.pack()

        inposicon2 = customtkinter.CTkLabel(inpos2, text="", image=moon, fg_color="transparent", width=50, height=50)
        inposicon2.pack()

        inposdeegres2 = customtkinter.CTkLabel(inpos2, text=f"{api.second_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres2.pack()

        inpos3 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos3.pack(side="left", padx=20, pady=10)

        inpostime3 = customtkinter.CTkLabel(inpos3, text="23:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime3.pack()

        inposicon3 = customtkinter.CTkLabel(inpos3, text="", image=moon, fg_color="transparent", width=50, height=50)
        inposicon3.pack()

        inposdeegres3 = customtkinter.CTkLabel(inpos3, text=f"{api.third_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres3.pack()

        inpos4 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos4.pack(side="left", padx=20, pady=10)

        inpostime4 = customtkinter.CTkLabel(inpos4, text="00:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime4.pack()

        inposicon4 = customtkinter.CTkLabel(inpos4, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon4.pack()

        inposdeegres4 = customtkinter.CTkLabel(inpos4, text=f"{api.fourth_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres4.pack()

        inpos5 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos5.pack(side="left", padx=20, pady=10)

        inpostime5 = customtkinter.CTkLabel(inpos5, text="01:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime5.pack()

        inposicon5 = customtkinter.CTkLabel(inpos5, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon5.pack()

        inposdeegres5 = customtkinter.CTkLabel(inpos5, text=f"{api.fifth_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres5.pack()

        inpos6 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos6.pack(side="left", padx=20, pady=10)

        inpostime6 = customtkinter.CTkLabel(inpos6, text="02:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime6.pack()

        inposicon6 = customtkinter.CTkLabel(inpos6, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon6.pack()

        inposdeegres6 = customtkinter.CTkLabel(inpos6, text=f"{api.sixth_hour} °", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres6.pack()

        inpos7 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos7.pack(side="left", padx=20, pady=10)

        inpostime7 = customtkinter.CTkLabel(inpos7, text="03:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime7.pack()

        inposicon7 = customtkinter.CTkLabel(inpos7, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon7.pack()

        inposdeegres7 = customtkinter.CTkLabel(inpos7, text=f"{api.seventh_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres7.pack()

        inpos8 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos8.pack(side="left", padx=20, pady=10)

        inpostime8 = customtkinter.CTkLabel(inpos8, text="04:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime8.pack()

        inposicon8 = customtkinter.CTkLabel(inpos8, text="", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon8.pack()

        inposdeegres8 = customtkinter.CTkLabel(inpos8, text=f"{api.eighth_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres8.pack()

        inpos9 = customtkinter.CTkFrame(inlinePositionFrame, width=55, height=149, fg_color="transparent")
        inpos9.pack(side="left", padx=0, pady=10)

        inpostime9 = customtkinter.CTkLabel(inpos9, text="05:00", text_color="white", font=customtkinter.CTkFont(weight="bold", size=20))
        inpostime9.pack()

        inposicon9 = customtkinter.CTkLabel(inpos9, text=" ", image=sunny, fg_color="transparent", width=50, height=50)
        inposicon9.pack()

        inposdeegres9 = customtkinter.CTkLabel(inpos9, text=f"{api.nineth_hour}°", text_color="white", font=customtkinter.CTkFont(weight="bold", size=23))
        inposdeegres9.pack()

        self.protocol("WM_DELETE_WINDOW", self.onclosing)
        getdate()
        set_status()

    def opencabinet(self):

        self.destroy()

        file_name = __file__ + '/../account.py'

        os.system(f"python {file_name}")

    def pochtidevyatkayoU(self):
        self.cityName.configure(text=f'{api.first_city_name.lower().capitalize()}')
        self.degreesLabel.configure(text=f'{api.first_celsiy}°')
        self.weatherShortDesc.configure(text=f'{api.first_description}')
        self.uparrowimg.configure(text=f'{api.first_max}')
        self.downarrowimg.configure(text=f'{api.first_min}')

        self.potochna.configure(fg_color = '#4599a4' )
        self.weatherStat.configure(fg_color = '#4599a4')
        self.weatherStatDegrees.configure(fg_color = '#4599a4')
        self.weatherStatDesc.configure(fg_color = '#4599a4')
        self.weatherStatName.configure(fg_color = '#4599a4')
        # self.weatherStatminmax.configure(fg_color = '#4599a4')

        self.kiivWeatherStat.configure(fg_color = '#096c82')
        self.kiivWeatherStatDegrees.configure(fg_color = '#096c82')
        self.kiivWeatherStatDesc.configure(fg_color = '#096c82')
        self.kiivWeatherStatName.configure(fg_color = '#096c82')
        # self.kiivWeatherStatminmax.configure(fg_color = '#096c82')

        self.londonWeatherStat.configure(fg_color = '#096c82')
        self.londonWeatherStatDegrees.configure(fg_color = '#096c82')
        self.londonWeatherStatDesc.configure(fg_color = '#096c82')
        self.londonWeatherStatName.configure(fg_color = '#096c82')
        # self.londonWeatherStatminmax.configure(fg_color = '#096c82')

        self.romeWeatherStat.configure(fg_color = '#096c82')
        self.romeWeatherStatDegrees.configure(fg_color = '#096c82')
        self.romeWeatherStatDesc.configure(fg_color = '#096c82')
        self.romeWeatherStatName.configure(fg_color = '#096c82')
        # self.romeWeatherStatminmax.configure(fg_color = '#096c82')

        self.warsawWeatherStat.configure(fg_color = '#096c82')
        self.warsawWeatherStatDegrees.configure(fg_color = '#096c82')
        self.warsawWeatherStatDesc.configure(fg_color = '#096c82')
        self.warsawWeatherStatName.configure(fg_color = '#096c82')
        # self.warsawWeatherStatminmax.configure(fg_color = '#096c82')

        self.pragueWeatherStat.configure(fg_color = '#096c82')
        self.pragueWeatherStatDegrees.configure(fg_color = '#096c82')
        self.pragueWeatherStatDesc.configure(fg_color = '#096c82')
        self.pragueWeatherStatName.configure(fg_color = '#096c82')
        # self.pragueWeatherStatminmax.configure(fg_color = '#096c82')

    def kyiv(self):
        self.cityName.configure(text=f'{api.kyiv_city_name.lower().capitalize()}')
        self.degreesLabel.configure(text=f'{api.kyiv_celsiy}°')
        self.weatherShortDesc.configure(text=f'{api.kyiv_description}')
        self.uparrowimg.configure(text=f'{api.kyiv_max}')
        self.downarrowimg.configure(text=f'{api.kyiv_min}')


        self.kiivWeatherStat.configure(fg_color = '#4599a4')
        self.kiivWeatherStatDegrees.configure(fg_color = '#4599a4')
        self.kiivWeatherStatDesc.configure(fg_color = '#4599a4')
        self.kiivWeatherStatName.configure(fg_color = '#4599a4')
        # self.kiivWeatherStatminmax.configure(fg_color = '#4599a4')

        self.potochna.configure(fg_color = '#096c82')
        self.weatherStat.configure(fg_color = '#096c82')
        self.weatherStatDegrees.configure(fg_color = '#096c82')
        self.weatherStatDesc.configure(fg_color = '#096c82')
        self.weatherStatName.configure(fg_color = '#096c82')
        # self.weatherStatminmax.configure(fg_color = '#096c82')


        self.londonWeatherStat.configure(fg_color = '#096c82')
        self.londonWeatherStatDegrees.configure(fg_color = '#096c82')
        self.londonWeatherStatDesc.configure(fg_color = '#096c82')
        self.londonWeatherStatName.configure(fg_color = '#096c82')
        # self.londonWeatherStatminmax.configure(fg_color = '#096c82')

        self.romeWeatherStat.configure(fg_color = '#096c82')
        self.romeWeatherStatDegrees.configure(fg_color = '#096c82')
        self.romeWeatherStatDesc.configure(fg_color = '#096c82')
        self.romeWeatherStatName.configure(fg_color = '#096c82')
        # self.romeWeatherStatminmax.configure(fg_color = '#096c82')


        self.warsawWeatherStat.configure(fg_color = '#096c82')
        self.warsawWeatherStatDegrees.configure(fg_color = '#096c82')
        self.warsawWeatherStatDesc.configure(fg_color = '#096c82')
        self.warsawWeatherStatName.configure(fg_color = '#096c82')
        # self.warsawWeatherStatminmax.configure(fg_color = '#096c82')

        self.pragueWeatherStat.configure(fg_color = '#096c82')
        self.pragueWeatherStatDegrees.configure(fg_color = '#096c82')
        self.pragueWeatherStatDesc.configure(fg_color = '#096c82')
        self.pragueWeatherStatName.configure(fg_color = '#096c82')
        # self.pragueWeatherStatminmax.configure(fg_color = '#096c82')
                                   
    def london(self):
        self.cityName.configure(text=f'{api.london_city_name.lower().capitalize()}')
        self.degreesLabel.configure(text=f'{api.london_celsiy}°')
        self.weatherShortDesc.configure(text=f'{api.london_description}')
        self.uparrowimg.configure(text=f'{api.london_max}')
        self.downarrowimg.configure(text=f'{api.london_min}')

        self.kiivWeatherStat.configure(fg_color = '#096c82')
        self.kiivWeatherStatDegrees.configure(fg_color = '#096c82')
        self.kiivWeatherStatDesc.configure(fg_color = '#096c82')
        self.kiivWeatherStatName.configure(fg_color = '#096c82')
        # self.kiivWeatherStatminmax.configure(fg_color = '#096c82')
        
        self.potochna.configure(fg_color = '#096c82')
        self.weatherStat.configure(fg_color = '#096c82')
        self.weatherStatDegrees.configure(fg_color = '#096c82')
        self.weatherStatDesc.configure(fg_color = '#096c82')
        self.weatherStatName.configure(fg_color = '#096c82')
        # self.weatherStatminmax.configure(fg_color = '#096c82')

        self.londonWeatherStat.configure(fg_color = '#4599a4')
        self.londonWeatherStatDegrees.configure(fg_color = '#4599a4')
        self.londonWeatherStatDesc.configure(fg_color = '#4599a4')
        self.londonWeatherStatName.configure(fg_color = '#4599a4')
        # self.londonWeatherStatminmax.configure(fg_color = '#4599a4')

        self.romeWeatherStat.configure(fg_color = '#096c82')
        self.romeWeatherStatDegrees.configure(fg_color = '#096c82')
        self.romeWeatherStatDesc.configure(fg_color = '#096c82')
        self.romeWeatherStatName.configure(fg_color = '#096c82')
        # self.romeWeatherStatminmax.configure(fg_color = '#096c82')

        self.warsawWeatherStat.configure(fg_color = '#096c82')
        self.warsawWeatherStatDegrees.configure(fg_color = '#096c82')
        self.warsawWeatherStatDesc.configure(fg_color = '#096c82')
        self.warsawWeatherStatName.configure(fg_color = '#096c82')
        # self.warsawWeatherStatminmax.configure(fg_color = '#096c82')

        self.pragueWeatherStat.configure(fg_color = '#096c82')
        self.pragueWeatherStatDegrees.configure(fg_color = '#096c82')
        self.pragueWeatherStatDesc.configure(fg_color = '#096c82')
        self.pragueWeatherStatName.configure(fg_color = '#096c82')
        # self.pragueWeatherStatminmax.configure(fg_color = '#096c82')

    def rome(self):
        self.cityName.configure(text=f'{api.rome_city_name.lower().capitalize()}')
        self.degreesLabel.configure(text=f'{api.rome_celsiy}°')
        self.weatherShortDesc.configure(text=f'{api.rome_description}')
        self.uparrowimg.configure(text=f'{api.rome_max}')
        self.downarrowimg.configure(text=f'{api.rome_min}')

        self.kiivWeatherStat.configure(fg_color = '#096c82')
        self.kiivWeatherStatDegrees.configure(fg_color = '#096c82')
        self.kiivWeatherStatDesc.configure(fg_color = '#096c82')
        self.kiivWeatherStatName.configure(fg_color = '#096c82')
        # self.kiivWeatherStatminmax.configure(fg_color = '#096c82')
        
        self.potochna.configure(fg_color = '#096c82')
        self.weatherStat.configure(fg_color = '#096c82')
        self.weatherStatDegrees.configure(fg_color = '#096c82')
        self.weatherStatDesc.configure(fg_color = '#096c82')
        self.weatherStatName.configure(fg_color = '#096c82')
        # self.weatherStatminmax.configure(fg_color = '#096c82')

        self.londonWeatherStat.configure(fg_color = '#096c82')
        self.londonWeatherStatDegrees.configure(fg_color = '#096c82')
        self.londonWeatherStatDesc.configure(fg_color = '#096c82')
        self.londonWeatherStatName.configure(fg_color = '#096c82')
        # self.londonWeatherStatminmax.configure(fg_color = '#096c82')

        self.romeWeatherStat.configure(fg_color = '#4599a4')
        self.romeWeatherStatDegrees.configure(fg_color = '#4599a4')
        self.romeWeatherStatDesc.configure(fg_color = '#4599a4')
        self.romeWeatherStatName.configure(fg_color = '#4599a4')
        # self.romeWeatherStatminmax.configure(fg_color = '#4599a4')

        self.warsawWeatherStat.configure(fg_color = '#096c82')
        self.warsawWeatherStatDegrees.configure(fg_color = '#096c82')
        self.warsawWeatherStatDesc.configure(fg_color = '#096c82')
        self.warsawWeatherStatName.configure(fg_color = '#096c82')
        # self.warsawWeatherStatminmax.configure(fg_color = '#096c82')

        self.pragueWeatherStat.configure(fg_color = '#096c82')
        self.pragueWeatherStatDegrees.configure(fg_color = '#096c82')
        self.pragueWeatherStatDesc.configure(fg_color = '#096c82')
        self.pragueWeatherStatName.configure(fg_color = '#096c82')
        # self.pragueWeatherStatminmax.configure(fg_color = '#096c82')

    def prague(self):
        self.cityName.configure(text=f'{api.prague_city_name.lower().capitalize()}')
        self.degreesLabel.configure(text=f'{api.prague_celsiy}°')
        self.weatherShortDesc.configure(text=f'{api.prague_description}')
        self.uparrowimg.configure(text=f'{api.prague_min}')
        self.downarrowimg.configure(text=f'{api.prague_max}')

        self.kiivWeatherStat.configure(fg_color = '#096c82')
        self.kiivWeatherStatDegrees.configure(fg_color = '#096c82')
        self.kiivWeatherStatDesc.configure(fg_color = '#096c82')
        self.kiivWeatherStatName.configure(fg_color = '#096c82')
        # self.kiivWeatherStatminmax.configure(fg_color = '#096c82')
        
        self.potochna.configure(fg_color = '#096c82')
        self.weatherStat.configure(fg_color = '#096c82')
        self.weatherStatDegrees.configure(fg_color = '#096c82')
        self.weatherStatDesc.configure(fg_color = '#096c82')
        self.weatherStatName.configure(fg_color = '#096c82')
        # self.weatherStatminmax.configure(fg_color = '#096c82')

        self.londonWeatherStat.configure(fg_color = '#096c82')
        self.londonWeatherStatDegrees.configure(fg_color = '#096c82')
        self.londonWeatherStatDesc.configure(fg_color = '#096c82')
        self.londonWeatherStatName.configure(fg_color = '#096c82')
        # self.londonWeatherStatminmax.configure(fg_color = '#096c82')


        self.romeWeatherStat.configure(fg_color = '#096c82')
        self.romeWeatherStatDegrees.configure(fg_color = '#096c82')
        self.romeWeatherStatDesc.configure(fg_color = '#096c82')
        self.romeWeatherStatName.configure(fg_color = '#096c82')
        # self.romeWeatherStatminmax.configure(fg_color = '#096c82')

        self.warsawWeatherStat.configure(fg_color = '#096c82')
        self.warsawWeatherStatDegrees.configure(fg_color = '#096c82')
        self.warsawWeatherStatDesc.configure(fg_color = '#096c82')
        self.warsawWeatherStatName.configure(fg_color = '#096c82')
        # self.warsawWeatherStatminmax.configure(fg_color = '#096c82')

        self.pragueWeatherStat.configure(fg_color = '#4599a4')
        self.pragueWeatherStatDegrees.configure(fg_color = '#4599a4')
        self.pragueWeatherStatDesc.configure(fg_color = '#4599a4')
        self.pragueWeatherStatName.configure(fg_color = '#4599a4')
        # self.pragueWeatherStatminmax.configure(fg_color = '#4599a4')

    def warsaw(self):
        self.cityName.configure(text=f'{api.warsaw_city_name.lower().capitalize()}')
        self.degreesLabel.configure(text=f'{api.warsaw_celsiy}°')
        self.weatherShortDesc.configure(text=f'{api.warsaw_description}')
        self.uparrowimg.configure(text=f'{api.warsaw_max}')
        self.downarrowimg.configure(text=f'{api.warsaw_min}')

        self.kiivWeatherStat.configure(fg_color = '#096c82')
        self.kiivWeatherStatDegrees.configure(fg_color = '#096c82')
        self.kiivWeatherStatDesc.configure(fg_color = '#096c82')
        self.kiivWeatherStatName.configure(fg_color = '#096c82')
        # self.kiivWeatherStatminmax.configure(fg_color = '#096c82')
        
        self.potochna.configure(fg_color = '#096c82')
        self.weatherStat.configure(fg_color = '#096c82')
        self.weatherStatDegrees.configure(fg_color = '#096c82')
        self.weatherStatDesc.configure(fg_color = '#096c82')
        self.weatherStatName.configure(fg_color = '#096c82')
        # self.weatherStatminmax.configure(fg_color = '#096c82')

        self.londonWeatherStat.configure(fg_color = '#096c82')
        self.londonWeatherStatDegrees.configure(fg_color = '#096c82')
        self.londonWeatherStatDesc.configure(fg_color = '#096c82')
        self.londonWeatherStatName.configure(fg_color = '#096c82')
        # self.londonWeatherStatminmax.configure(fg_color = '#096c82')

        self.romeWeatherStat.configure(fg_color = '#096c82')
        self.romeWeatherStatDegrees.configure(fg_color = '#096c82')
        self.romeWeatherStatDesc.configure(fg_color = '#096c82')
        self.romeWeatherStatName.configure(fg_color = '#096c82')
        # self.romeWeatherStatminmax.configure(fg_color = '#096c82')

        self.warsawWeatherStat.configure(fg_color = '#4599a4')
        self.warsawWeatherStatDegrees.configure(fg_color = '#4599a4')
        self.warsawWeatherStatDesc.configure(fg_color = '#4599a4')
        self.warsawWeatherStatName.configure(fg_color = '#4599a4')
        # self.warsawWeatherStatminmax.configure(fg_color = '#4599a4')

        self.pragueWeatherStat.configure(fg_color = '#096c82')
        self.pragueWeatherStatDegrees.configure(fg_color = '#096c82')
        self.pragueWeatherStatDesc.configure(fg_color = '#096c82')
        self.pragueWeatherStatName.configure(fg_color = '#096c82')
        # self.pragueWeatherStatminmax.configure(fg_color = '#096c82')

    def onclosing(self):
        self.destroy()

        file_name = r'F:\python\work_with_weather_app\gui\widget.py'

        os.system(f"python {file_name}")


app1 = App()
app1.mainloop()
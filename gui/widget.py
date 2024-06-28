import tkinter as tk
import customtkinter
import api_file as api
from PIL import ImageTk, Image
import requests
import os

class DragDropWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyWeather")
        self.geometry("347x350")
        self.iconbitmap(__file__ + r'/../icon.ico')
        self.resizable(0, 0)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images2")
        
        sunny = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"sunny.png")), size=(180, 180))
        rain = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"rain.png")), size=(180, 180))
        moon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"moon.png")), size=(180, 180))
        refreshicon = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"captcha.png")), size=(25, 25))

        downarrow = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow1.png")), size=(20, 20))
        uparrow = customtkinter.CTkImage(Image.open(os.path.join(image_path, r"arrow2.png")), size=(20, 20))

        mainFrame = customtkinter.CTkFrame(self, fg_color="#5DA7B1", width=350, height=350, border_width=5, border_color="#096C82", corner_radius=20) #corner_radius=20
        mainFrame.pack()

        weatherIconStatus = customtkinter.CTkLabel(mainFrame, image=sunny, fg_color="#5DA7B1", bg_color="#5DA7B1", width=120, height=120, corner_radius=0, text="")
        weatherIconStatus.place(x=17, y=18)

        self.downarrowval = customtkinter.CTkLabel(mainFrame, text=f'{api.first_min}' + '°', text_color="white", image=downarrow ,compound='left' ,font=customtkinter.CTkFont(weight="bold", size=22))
        self.downarrowval.place(x=130,y=250, anchor=tk.CENTER)

        self.uparrowval = customtkinter.CTkLabel(mainFrame, text=f"{api.first_max}" + '°', text_color="white", compound='left' ,image=uparrow,font=customtkinter.CTkFont(weight="bold", size=22))
        self.uparrowval.place(x=70,y=250, anchor=tk.CENTER)

        refreshButton = customtkinter.CTkButton(mainFrame, image=refreshicon, fg_color="#5DA7B1", width=25, height=25, text="", bg_color="#5DA7B1", hover_color="#338A95", corner_radius=20, command=self.inclick)
        refreshButton.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

        self.tempritureStatus = customtkinter.CTkLabel(mainFrame, text=f'{api.first_celsiy}' + '°', text_color="white", fg_color="#5DA7B1", corner_radius=0, font=customtkinter.CTkFont(weight="bold", size=60))
        self.tempritureStatus.place(relx=0.8, rely=0.7, anchor=tk.CENTER)

        cityName = customtkinter.CTkLabel(mainFrame, text=api.first_city_name, text_color="white", fg_color="#5DA7B1", corner_radius=0, font=customtkinter.CTkFont(weight="bold", size=50))
        cityName.place(relx=0.65, rely=0.88, anchor=tk.CENTER)

        cityDescription = customtkinter.CTkLabel(mainFrame, text=api.first_description, text_color='white', fg_color='#5DA7B1', corner_radius=0, font=customtkinter.CTkFont(weight="bold", size=26))
        cityDescription.place(x=37,y=192)
    def inclick(self):

        api_key = 'ac90bee491d306ada1c92f65cd9f3482'
        refresh_city_name = 'Дніпро'
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
        
        self.tempritureStatus.configure(text=f'{refresh_celsiy}°')
        self.uparrowval.configure(text=f'{refresh_max}°')
        self.downarrowval.configure(text=f'{refresh_min}°')
        
        




app = DragDropWindow()
app.mainloop()

import customtkinter, os, sqlite3
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

customtkinter.set_appearance_mode('dark')
# image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
registration = customtkinter.CTk()
registration.geometry(f'{460}x{645}')
registration.resizable(False, False)
registration.title('Registration Window')
registration.iconbitmap(__file__ + r'/../icon.ico')

mainframe = customtkinter.CTkFrame(master=registration, width=440, height=625, corner_radius=14,fg_color='#5ba3b3',border_width=5,border_color='#0c6b83')
mainframe.place(x=10,y=10)

registr_label = customtkinter.CTkLabel(master=mainframe, text='Реєстрація користувача',font=customtkinter.CTkFont(size=25, weight='bold'))
registr_label.place(x=60, y=40)

country_text = customtkinter.CTkLabel(master=mainframe, text= "Країна:", font=customtkinter.CTkFont(size=23, weight='bold'))
country_text.place(x=30, y=120)
country_entry = customtkinter.CTkEntry(mainframe, height=40, width=200, placeholder_text="", fg_color='#0c6b83', border_color='white', border_width=1, corner_radius=17)
country_entry.place(x=26, y=160)

city_text = customtkinter.CTkLabel(master=mainframe, text= "Місто:", font=customtkinter.CTkFont(size=23, weight='bold'))
city_text.place(x=30, y=220)
city_entry = customtkinter.CTkEntry(mainframe, height=40, width=200, placeholder_text="", fg_color='#0c6b83', border_color='white', border_width=1, corner_radius=17)
city_entry.place(x=26, y=260)

name_text = customtkinter.CTkLabel(master=mainframe, text= "Ім'я:", font=customtkinter.CTkFont(size=23, weight='bold'))
name_text.place(x=30, y=320)
name_entry = customtkinter.CTkEntry(mainframe, height=40, width=250, placeholder_text="", fg_color='#0c6b83', border_color='white', border_width=1, corner_radius=17)
name_entry.place(x=26, y=360)

last_name_text = customtkinter.CTkLabel(master=mainframe, text= "Прізвище:", font=customtkinter.CTkFont(size=23, weight='bold'))
last_name_text.place(x=30, y=420)
last_name_entry = customtkinter.CTkEntry(mainframe, height=40, width=250, placeholder_text="", fg_color='#0c6b83', border_color='white', border_width=1, corner_radius=17)
last_name_entry.place(x=26, y=460)

def getinputentry(): 
    connect = sqlite3.connect('myweather.db')
    cursor = connect.cursor()

    last_get  = last_name_entry.get().replace(" ", "")
    city_get =city_entry.get().replace(" ", "")
    country_get = country_entry.get().replace(" ", "")
    name_get = name_entry.get().strip()

    cursor.execute('CREATE TABLE IF NOT EXISTS account (name text, last_name text, country text, city text)')

    cursor.execute(f"INSERT INTO account VALUES ('{name_get}' , '{last_get}' , '{country_get}' , '{city_get}')")

    connect.commit()

    connect.close()

    registration.destroy()

    # python = r'C:\Users\Димон\AppData\Local\Programs\Python\Python312\python.exe'
    path_file = __file__+  r'/..\\account.py'
    
    # print(python, file_name)

    os.system(f'python {path_file}')
    



main_button_1 = customtkinter.CTkButton(master=mainframe, width=180, height=40, fg_color="#0c6b83", text="Зберегти", border_width=2, text_color=("gray10", "#DCE4EE"), corner_radius=20, command=getinputentry)
main_button_1.place(x=130,y=550)

registration.mainloop()




































# import tkinter as tk
# import customtkinter
# from tkinter import messagebox
# import os
# import sqlite3

# class DragDropWindow(customtkinter.CTk):
#     def __init__(self):
#         super().__init__(fg_color="white")
#         self.title("User Registration")
#         self.resizable(0, 0)

#         def login():

#             global countryname
#             global cityname

#             countryname = countryName.get()
#             cityname = cityName.get()
#             username = userName.get()
#             surname = surName.get()

#             #country = apii.getcountrydata()
#             #city = apii.getcitydata()

#             if countryname == "1" and cityname == "1":
#                 connect = sqlite3.connect('database.db')
#                 cursor = connect.cursor()

#                 cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT,
#                         surname TEXT,
#                         country TEXT,
#                         city TEXT
#                     )
#                 ''')


#                 cursor.execute('''
#                     INSERT INTO users (name, surname, country, city) 
#                     VALUES (?, ?, ?, ?)
#                 ''', (username, surname, countryname, cityname))

#                 connect.commit()
#                 connect.close()
#                 print("User succesfully authorizated!")
#                 os.system("python app.py")
#             else:
#                 messagebox.showerror("Помилка!", "Виникла помилка! Введіть правильні дані.")

#         mainFrame = customtkinter.CTkFrame(self, fg_color="#5DA7B1", width=560, height=645, border_width=5, border_color="#096C82", corner_radius=20)
#         mainFrame.pack()

#         mainHeader = customtkinter.CTkLabel(mainFrame, text="Реєстрація користувача", font=customtkinter.CTkFont(weight="bold", size=40, family="Roboto Slab"), text_color="white")
#         mainHeader.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

#         customtkinter.CTkLabel(mainFrame, text="Країна:", text_color="white", font=customtkinter.CTkFont(weight="bold", size=25)).place(relx=0.16, rely=0.17, anchor=tk.CENTER)

#         countryName = customtkinter.CTkEntry(mainFrame, width=225, height=46, corner_radius=20, fg_color="#096C82", border_width=3, border_color="#91DCE6", text_color="#91DCE6", font=customtkinter.CTkFont(size=20, weight="bold"))
#         countryName.place(relx=0.3, rely=0.25, anchor=tk.CENTER)

#         customtkinter.CTkLabel(mainFrame, text="Місто:", text_color="white", font=customtkinter.CTkFont(weight="bold", size=25)).place(relx=0.16, rely=0.33, anchor=tk.CENTER)

#         cityName = customtkinter.CTkEntry(mainFrame, width=225, height=46, corner_radius=20, fg_color="#096C82", border_width=3, border_color="#91DCE6", text_color="#91DCE6", font=customtkinter.CTkFont(size=20, weight="bold"))
#         cityName.place(relx=0.3, rely=0.42, anchor=tk.CENTER)

#         customtkinter.CTkLabel(mainFrame, text="Ім’я:", text_color="white", font=customtkinter.CTkFont(weight="bold", size=25)).place(relx=0.16, rely=0.5, anchor=tk.CENTER)

#         userName = customtkinter.CTkEntry(mainFrame, width=280, height=46, corner_radius=20, fg_color="#096C82", border_width=3, border_color="#91DCE6", text_color="#91DCE6", font=customtkinter.CTkFont(size=20, weight="bold"))
#         userName.place(relx=0.35, rely=0.59, anchor=tk.CENTER)

#         customtkinter.CTkLabel(mainFrame, text="Прізвище:", text_color="white", font=customtkinter.CTkFont(weight="bold", size=25)).place(relx=0.22, rely=0.67, anchor=tk.CENTER)

#         surName = customtkinter.CTkEntry(mainFrame, width=280, height=46, corner_radius=20, fg_color="#096C82", border_width=3, border_color="#91DCE6", text_color="#91DCE6", font=customtkinter.CTkFont(size=20, weight="bold"))
#         surName.place(relx=0.35, rely=0.75, anchor=tk.CENTER)

#         confirm = customtkinter.CTkButton(mainFrame, text="Зберегти", width=230, height=46, corner_radius=20, fg_color="#096C82", border_width=3, border_color="#91DCE6", text_color="#91DCE6", font=customtkinter.CTkFont(size=20, weight="bold"), hover_color="#085263", command=login)
#         confirm.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


# if __name__ == "__main__":
#     app = DragDropWindow()
    #@app.mainloop()

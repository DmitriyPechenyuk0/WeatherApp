import customtkinter
import os
import sqlite3

customtkinter.set_appearance_mode('dark')

account = customtkinter.CTk()
account.geometry(f'{460}x{645}')
account.resizable(0,0)
account.title('Authorization Window')

account.iconbitmap(__file__ + r'/../icon.ico')

connect = sqlite3.connect('myweather.db')
cursor = connect.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS registration (reg TEXT)')

cursor.execute('SELECT city FROM account ORDER BY rowid DESC LIMIT 1')
last_city = cursor.fetchone()

cursor.execute('SELECT country FROM account ORDER BY rowid DESC LIMIT 1')
last_country = cursor.fetchone()

cursor.execute('SELECT name FROM account ORDER BY rowid DESC LIMIT 1')
last_name = cursor.fetchone()

cursor.execute('SELECT last_name FROM account ORDER BY rowid DESC LIMIT 1')
last_last_name = cursor.fetchone()

print(last_city,last_country,last_last_name,last_name)

connect.commit()
connect.close()

mainframe = customtkinter.CTkFrame(master=account, width=440, height=625, corner_radius=14,fg_color='#5ba3b3',border_width=5,border_color='#0c6b83')
mainframe.place(x=10,y=10)

osobystiy_kabinet_label = customtkinter.CTkLabel(master=mainframe, text='Особистий кабінет',font=customtkinter.CTkFont(size=25, weight='bold'))
osobystiy_kabinet_label.place(x=60, y=40)

country_text = customtkinter.CTkLabel(master=mainframe, text= "Країна:", font=customtkinter.CTkFont(size=23, weight='bold'))
country_text.place(x=30, y=120)
country_select = customtkinter.CTkLabel(master=mainframe, text=f'{last_country[0]}', font=customtkinter.CTkFont(size=25, weight='bold',underline=True))
country_select.place(x=119,y=157)

city_text = customtkinter.CTkLabel(master=mainframe, text= "Місто:", font=customtkinter.CTkFont(size=23, weight='bold'))
city_text.place(x=30, y=220)
city_select = customtkinter.CTkLabel(master=mainframe, text=f"{last_city[0]}", font=customtkinter.CTkFont(size=25, weight='bold',underline=True))
city_select.place(x=119, y=256)

name_text = customtkinter.CTkLabel(master=mainframe, text= "Ім'я:", font=customtkinter.CTkFont(size=23, weight='bold'))
name_text.place(x=30, y=320)
name_select = customtkinter.CTkLabel(master=mainframe, text=f'{last_name[0]}', font=customtkinter.CTkFont(size=25, weight='bold',underline=True))
name_select.place(x=119, y=352)

last_name_text = customtkinter.CTkLabel(master=mainframe, text= "Прізвище:", font=customtkinter.CTkFont(size=23, weight='bold'))
last_name_text.place(x=30, y=420)
last_name_select = customtkinter.CTkLabel(master=mainframe, text=f"{last_last_name[0]}", font=customtkinter.CTkFont(size=25, weight='bold',underline=True))
last_name_select.place(x=119, y=455)

def nextfile():

    account.destroy()
    path_file = __file__+  r'/..\\app.py'
    os.system(f'python {path_file}')


main_button_1 = customtkinter.CTkButton(master=mainframe, width=180, height=40, fg_color="#0c6b83", text="Перейти до додатку", border_width=2, text_color=("gray10", "#DCE4EE"), corner_radius=20, command=nextfile)
main_button_1.place(x=130,y=550)

account.mainloop()



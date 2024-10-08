from tkinter import *
from tkinter import ttk
import requests

# Function to fetch and display weather data
def data_get():
    city = city_name.get()
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a9390f8429be0b95a8631940485add06")
    data = response.json()
    if response.status_code == 200:
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=f"{int(data['main']['temp'] - 273.15)}°C")
        per_label1.config(text=data["main"]["pressure"])
    else:
        w_label1.config(text="N/A")
        wd_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")


win = Tk()
win.title("OIBSIP Intern Weather App")
win.config(bg='blue')
win.geometry("500x570")

name_label = Label(win, text="OIBSIP Intern Weather App", font=('arial', 25, 'bold'), bg='blue', fg='white')
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_names = ["Karachi", "Lahore", "Quetta", "Peshawar", "Islamabad"]
com = ttk.Combobox(win, values=list_names, font=('arial', 15, 'bold'), textvariable=city_name)
com.place(x=150, y=150, height=50, width=200)
com.set("Select City")

w_label = Label(win, text="Weather Climate", font=('arial', 15, 'bold'), bg='blue', fg='white')
w_label.place(x=25, y=220, height=50, width=200)
w_label1 = Label(win, text="", font=('arial', 15, 'bold'), bg='blue', fg='white')
w_label1.place(x=250, y=220, height=50, width=200)

wd_label = Label(win, text="Description", font=('arial', 15, 'bold'), bg='blue', fg='white')
wd_label.place(x=25, y=290, height=50, width=200)
wd_label1 = Label(win, text="", font=('arial', 15, 'bold'), bg='blue', fg='white')
wd_label1.place(x=250, y=290, height=50, width=200)

temp_label = Label(win, text="Temperature", font=('arial', 15, 'bold'), bg='blue', fg='white')
temp_label.place(x=25, y=360, height=50, width=200)
temp_label1 = Label(win, text="", font=('arial', 15, 'bold'), bg='blue', fg='white')
temp_label1.place(x=250, y=360, height=50, width=200)

per_label = Label(win, text="Pressure", font=('arial', 15, 'bold'), bg='blue', fg='white')
per_label.place(x=25, y=430, height=50, width=200)
per_label1 = Label(win, text="", font=('arial', 15, 'bold'), bg='blue', fg='white')
per_label1.place(x=250, y=430, height=50, width=200)

done_button = Button(win, text="Find Weather", font=('arial', 15, 'bold'), command=data_get, bg='orange', activebackground='green')
done_button.place(x=150, y=500, height=50, width=200)


win.mainloop()
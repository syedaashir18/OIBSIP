from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("OIBSIP BMI CALCULATOR")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())
        m = h / 100
        bmi = round(w / m**2)
        label1.config(text=bmi)
        
        if bmi < 18.5:
            label2.config(text="UNDERWEIGHT")
            label3.config(text="You have lower weight than normal body")
        elif 18.5 <= bmi <= 24.9:
            label2.config(text="NORMAL")
            label3.config(text="You have a normal body")
        elif 25 <= bmi <= 29.9:
            label2.config(text="OVERWEIGHT")
            label3.config(text="You are overweight than normal body")
        else:
            label2.config(text="OBESE")
            label3.config(text="Health may be at risk")
    except ValueError:
        label1.config(text="Invalid Input")
        label2.config(text="")
        label3.config(text="")

image_icon = PhotoImage(file="C:/Users/ht/Downloads/icon.png")
root.iconphoto(False, image_icon)

top = PhotoImage(file="C:/Users/ht/Downloads/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

bottom_label = Label(root, width=72, height=18, bg="lightblue")
bottom_label.pack(side=BOTTOM)

box = PhotoImage(file="C:/Users/ht/Downloads/box.png")
box_image1 = Label(root, image=box)
box_image1.place(x=20, y=100)

box_image2 = Label(root, image=box)
box_image2.place(x=240, y=100)

scale = PhotoImage(file="C:/Users/ht/Downloads/scale.png")
scale_image = Label(root, image=scale, bg="lightblue")
scale_image.place(x=20, y=310)

current_value = tk.DoubleVar()

def get_current_value():
    return "{:.2f}".format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = Image.open("C:/Users/ht/Downloads/man.png")
    resized_image = img.resize((50, 10 + size))
    Photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=Photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = Photo2

style = ttk.Style()
style.configure("TScale", background="red")
slider = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

current_value2 = tk.DoubleVar()

def get_current_value2():
    return "{:.2f}".format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale", background="red")
slider2 = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

Height = StringVar()
Weight = StringVar()

height_entry = Entry(root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
height_entry.place(x=35, y=160)
Height.set(get_current_value())

Weight_entry = Entry(root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
Weight_entry.place(x=255, y=160)
Weight.set(get_current_value2())

secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)
label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=200, y=500)

root.mainloop()

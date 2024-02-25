from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=aa4e3d1855fbaf85658d06ce1c2e71a0").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win=Tk()

win.title("Weather APP")
win.config(bg="blue")
win.geometry("500x570")
name_label=Label(win,text="WEATHER APP",font=("Math Sans",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_state=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com=ttk.Combobox(win,text="Select Your City",values=list_state,font=("Math Sans",30,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="Weather climate",font=("Math Sans",20,"bold"))
w_label.place(x=25,y=260,width=210,height=50 )

w_label1=Label(win,text="",font=("Math Sans",20,"bold"))
w_label1.place(x=250,y=260,width=210,height=50 )

wb_label=Label(win,text="Weather Description",font=("Math Sans",15,"bold"))
wb_label.place(x=25,y=330,width=210,height=50)

wb_label1=Label(win,text="",font=("Math Sans",15,"bold"))
wb_label1.place(x=250,y=330,width=210,height=50)

temp_label=Label(win,text="Tempreture",font=("Math Sans",20,"bold"))
temp_label.place(x=25,y=400,width=210,height=50)

temp_label1=Label(win,text="",font=("Math Sans",20,"bold"))
temp_label1.place(x=250,y=400,width=210,height=50)


per_label=Label(win,text="Pressure",font=("Math Sans",20,"bold"))
per_label.place(x=25,y=460,width=210,height=50)

per_label1=Label(win,text="",font=("Math Sans",20,"bold"))
per_label1.place(x=250,y=460,width=210,height=50)

done_button=Button(win,text="Done",font=("Math Sans",30,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


win.mainloop()

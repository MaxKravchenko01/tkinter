from cmath import e
from this import d
import tkinter as Tk
import tkinter
import requests
import json
from tkinter import *


def api_index(request):
    id = e.get()
    balance = e.get()
    setbalance = f'https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={id}&balance={balance}'
    requests.get(setbalance)
    url = f'https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={id}'
    response = requests.request("GET",url)
    res = requests.get(url)
    json = res.json()
    for i in json:
        user_id = i['id']
        user_name = i['name']
        user_surname = i['surname']
        user_balance = i['balance']
        


window = tkinter.Tk()
window.title('window')
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.geometry('500x500')

button = tkinter.Button(
    text = "Buy me a Frenchman in World of Tanks",
    width = 25,
    height = 5,
    bg = "blue",
    fg = "red"

)

window.mainloop()
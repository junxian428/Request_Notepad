
import json
import tkinter
import tkinter.messagebox
from tkinter import *
import requests
import urllib
from tkinter import scrolledtext
from tkinter import filedialog
import webbrowser
from selenium import webdriver
import poplib
from email import parser
import io
import PIL
from PIL import Image, ImageDraw





global search
global SWITCH

top = tkinter.Tk()
top.state('zoomed')


browser_name = tkinter.Message(top,text="Lazy Browser")
browser_name.place(x=1200,y=200)

text_area = scrolledtext.ScrolledText(top,wrap=tkinter.WORD,width=80,height=200)
text_area.grid(column=0, pady=10, padx=10)
text_area.focus()
#message_area = scrolledtext.ScrolledText(top,wrap=tkinter.WORD,width=30,height=50)
#message_area.grid(column=0, pady=5, padx=5)
#message_area.place(x=450,y=10)
#message_area.focus()


E1 = Entry(top)
E1.place(x=1180,y=300)

def browser():
   search = E1.get()
   x = requests.get('https://'+ search)
   text_area.insert(tkinter.INSERT, x.text)
   # tkinter.Message(top, text= x.text).place(x=100,y=100)


   return


def export():
    text = text_area.get("1.0", "end-1c")
    with io.open("saved.txt", "w", encoding="utf-8") as f:
          f.write(text)
    f.close
    return



tkinter.Button(top,text="Exit",command=exit).place(x=1220,y=440)



tkinter.Button(top, text="Search", command=browser).place(x=1210,y=350)
tkinter.Button(top, text="Export as ", command=export).place(x=1210,y=380)


top.mainloop()




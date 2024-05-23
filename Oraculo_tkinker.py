from tkinter import *
import pandas as pd
from pandas.io.json._normalize import json_normalize
import PIL
from PIL import ImageTk
import random

#Pantalla
interface = Tk() 
interface.config(width=600, height=500)
interface.title("TarotAPP")
interface.configure(bg="black")

#para poder ver todo lo que dicen las columnas
pd.set_option('display.max_colwidth', None)

#cargo dataset
cardsImgs = pd.read_json(r'C:\Users\arace\OneDrive\Escritorio\Maestría\TA en IA\TP interfaces\tarot-images.json', orient='records')
cardsImgs = json_normalize(cardsImgs['cards'])
arcanos_mayores = cardsImgs[cardsImgs['arcana'] == 'Major Arcana']

#########################

#función
def tirar():
    global tirada
    tirada = arcanos_mayores.sample(1)

    img_path = f'C:/Users/arace/OneDrive/Escritorio/Maestría/TA en IA/TP interfaces/cards/{tirada["img"].values[0]}'
    img = PIL.Image.open(img_path)
    img = img.resize((200, 300))
    img = ImageTk.PhotoImage(img)

    # mostrar la imagen en un label
    img_label.config(image=img)
    img_label.image = img

    # mostrar el texto en un label
    texto_label.config(text=tirada['fortune_telling'].values[0])
    
def palabras():    
    texto_label.config(text=tirada['keywords'].values[0])

#Botón
boton_tirar = Button(text="Elija una carta", command=tirar)
boton_tirar.place(x=220, y=450)

#Botón
boton_palabras = Button(text="Keywords", command=palabras)
boton_palabras.place(x=320, y=450)

# Label para mostrar la imagen
img_label = Label(interface)
img_label.place(x=200, y=50)

# Label para mostrar el texto
texto_label = Label(interface, wraplength=300)
texto_label.place(x=150, y=370)

interface.mainloop()

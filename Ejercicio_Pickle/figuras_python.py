from tkinter import *
from tkinter import ttk
import tkinter as tk
import pickle
import threading
import time

import cuadrado,triangulo,rectangulo,poligono

c=cuadrado.Cuadrado()
p=poligono.Poligono()
t=triangulo.Triangulo()
r=rectangulo.Rectangulo()

root = tk.Tk()
root.title("Calculadora de Áreas")
root.config(width=490, height=300)

tk.Label(root, text="Calculadora de Áreas").place(x=180,y=10)

tk.Label(root, text="Base:").place(x=50,y=60)
txtBase = tk.Entry()
txtBase.place(x=100,y=60)

tk.Label(root, text="Altura:").place(x=50, y=100)
txtAltura=tk.Entry()
txtAltura.place(x=100,y=100)

tk.Label(root, text="Lados:").place(x=250, y=60)
comboLados = ttk.Combobox(root)
comboLados.place(x=300,y=60)
comboLados['values'] = ('5','6','7','8','9','10')
comboLados.current(0)

tk.Label(root, text="Resultado:").place(x=250, y=100)
txtResultado=tk.Entry()
txtResultado.place(x=320,y=100)

tk.Label(root, text="Figura:").place(x=160, y=150)
comboFigura = ttk.Combobox(root)
comboFigura.place(x=200,y=150)
comboFigura['values'] = ('Triangulo','Cuadrado','Rectangulo','Poligono')
comboFigura.current(0)

def Calcular():
    if comboFigura.get()=="Triangulo":
        t.setBase(float(txtBase.get()))
        t.setAltura(float(txtAltura.get()))
        t.calcularArea()
        txtResultado.insert(0,str(t.getArea()))
    elif comboFigura.get()=="Cuadrado":
        c.setBase((float(txtBase.get())))
        c.calcularArea()
        txtResultado.insert(0,str(c.getArea()))
    elif comboFigura.get()=="Rectangulo":
        r.setBase((float(txtBase.get())))
        r.setAltura((float(txtAltura.get())))
        r.calcularArea()
        txtResultado.insert(0,str(r.getArea()))
    elif comboFigura.get()=="Poligono":
        p.setBase((float(txtBase.get())))
        p.setLados(float(comboLados.get()))
        p.calcularArea()
        txtResultado.insert(0,str(p.getArea()))

def serializar():
    valores = {
        'txtBase': txtBase.get(),
        'txtAltura': txtAltura.get(),
        'comboLados': comboLados.get(),
        'txtResultado': txtResultado.get(),
        'comboFigura': comboFigura.get()
    }
    with open('valores.pkl', 'wb') as archivo:
        pickle.dump(valores, archivo)

def deserializar():
    try:
        with open('valores.pkl', 'rb') as archivo:
            valores = pickle.load(archivo)
            txtBase.insert(0, valores['txtBase'])
            txtAltura.insert(0, valores['txtAltura'])
            comboLados.set(valores['comboLados'])
            txtResultado.insert(0, valores['txtResultado'])
            comboFigura.set(valores['comboFigura'])
    except FileNotFoundError:
        pass
def Limpiar():
    txtAltura.delete(0,END)
    txtBase.delete(0,END)
    txtResultado.delete(0,END)

btnCalcular=tk.Button(root,text= "Calcular",command=Calcular)
btnCalcular.place(x=200,y=200)

btnLimpiar=tk.Button(root,text= "Limpiar",command=Limpiar)
btnLimpiar.place(x=280,y=200)

def ejecutar_cada_30_segundos():
    while True:
        serializar()
        time.sleep(30)


hilo = threading.Thread(target=ejecutar_cada_30_segundos)

# Iniciar el hilo
hilo.start()

while True:
    time.sleep(1)
    deserializar()
    root.mainloop()
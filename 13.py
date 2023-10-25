#Serie 101010101010
from guizero import App, Text, TextBox, PushButton
app= App(title="Serie binaria")
b:int=0
lista=[]

def calcular():
    global b
    cantidad= int(cantidad_n.value)
    for i in range(cantidad):
        
        if b == 0:
            lista.append(1)
            b=1
        else:
            lista.append(0)
            b=0
    app.info(title="Resultado",text=(f"La serie es: {lista}"))

texto= Text(app, text="Ingresa la cantidad de caracteres que tendra la serie")
cantidad_n= TextBox(app,width=30)
boton1 = PushButton(app, text="Calcular", command=calcular)

app.display()

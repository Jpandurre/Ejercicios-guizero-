#suma de todos los cuadrados de n números capturados del teclado
from guizero import App, Text, TextBox, PushButton
app= App(title="Suma de cuadrados")
lista_n=[]
suma:int= 0

def agregar():
    global suma
    numero= int(num.value)
    if numero<0:
        app.info(title="Error", text="Ingresa un número positivo")
    else:
        cuadrado= pow(numero,2)
        lista_n.append(cuadrado)
        suma += cuadrado
        num.clear()
        

def sumatoria():
    app.info(title="Sumatoria", text=(f"La sumatoria de los cuadrados es {suma}"))

texto= Text(app, text="Ingresa un número")
num= TextBox(app, width=30)
boton1 = PushButton(app, text="Siguiente", command=agregar)
boton2 = PushButton(app, text="Sumar", command=sumatoria)
app.display()

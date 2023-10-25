#obtenga la suma del cuadrado de los pares y el cubo de los impares
from guizero import App, Text, TextBox, PushButton
app= App(title="Suma de el cuadrado de los pares y el cubo de los impares")
lista_par=[]
lista_impar=[]
suma_p:int= 0
suma_i:int= 0

def agregar():
    global suma_p, suma_i
    numero= int(num.value)
    if numero<0:
        app.info(title="Error", text="Ingresa un número positivo")
    elif numero%2==0:
        cu= pow(numero,2)
        lista_par.append(cu)
        suma_p += cu
        num.clear()
    else:
        cubo= pow(numero,3)
        lista_impar.append(cubo)
        suma_i += cubo
        num.clear()
        

def sumatoria():
    app.info(title="Sumatoria", text=(f"La suma de los pares es:{suma_p} y la suma de los impares es: {suma_i}"))

texto= Text(app, text="Ingresa un número")
num= TextBox(app, width=30)
boton1 = PushButton(app, text="Siguiente", command=agregar)
boton2 = PushButton(app, text="Sumar", command=sumatoria)
app.display()

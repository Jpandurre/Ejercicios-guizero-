#suma de 5 números capturados, entre 5 y 10 inclusive
from guizero import App, Text, TextBox, PushButton
app= App(title="Suma de 5 números")
list_datos=[5,6,7,8,9,10]
lista_n=[]
suma:int=0

def siguiente():
    global suma, clicks_restantes
    numeros=int(num.value)
    if numeros in list_datos:
        lista_n.append(numeros)
        suma += numeros
        num.clear()
    else:
        app.info(title="Error", text="Ingresa un número dentro del rango")
        num.clear()
    if len(lista_n) == 5:
        button2.show()
        button1.hide()
          
def sumatoria():
    app.info("Resultado", (f"La suma de los 5 números es {suma}"))
           
Mensaje= Text(app,text="Ingresa un número en el rango de [5,10]")
num= TextBox(app,width=30)
button1= PushButton(app,text="Siguiente", command=siguiente)
button2= PushButton(app,text="Calcular", command=sumatoria)
button2.hide()
app.display()

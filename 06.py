#calcule el cuadrado de un número positivo leído desde el teclado
from guizero import App, Text, TextBox, PushButton
app= App(title="Calculadora de cuadrados")

def calcular():
    try:
        numero= int(num.value)
        if numero<0:
            app.info(title="Error", text="Ingresa un número positivo")
            num.clear()
        else:
            error.clear()
            app.info("Resultado", (f"El cuadrado es {pow(numero,2)}"))
    except:
        error.value= "Ingresa valores númericos"
        
texto= Text(app, text="Ingresa un número")
num = TextBox(app, width=30)
boton1 = PushButton(app, text="Siguiente", command=calcular)
error= Text(app, text="", color="red")
app.display()

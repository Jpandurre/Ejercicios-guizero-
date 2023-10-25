#Menú de una calculadora funcional que pueda sumar, restar, multiplicar y dividir seleccionando el tipo de operacion. Dar 2 números.
from guizero import App, Text, TextBox, PushButton
app= App(title="Calculadora")

def calcular ():
    numero1= int(num1.value)
    numero2= int(num2.value)
    match int(operacion.value):
        case 1:
            suma= numero1 + numero2
            app.info(title="Resultado", text=(f"El reusltado de la suma es {suma}"))
        case 2:
            resta= numero1 - numero2
            app.info(title="Resultado", text=(f"El reusltado de la suma es {resta}"))
        case 3:
            multiplicacion= numero1 * numero2
            app.info(title="Resultado", text=(f"El reusltado de la suma es {multiplicacion}"))
        case 4:
            division= numero1 / numero2
            app.info(title="Resultado", text=(f"El reusltado de la suma es {division}"))
        case _:
            app.info(title="Error", text="Ingresa un número valido")


mensaje= Text(app,text="Ingresa un número")
num1= TextBox(app,width=30)
mensaje2= Text(app,text="Ingresa un número")
num2= TextBox(app,width=30)
mensaje3= Text(app,text="Indique que operacion vas a realizar:")
mensaje3= Text(app,text= "1.-suma, 2.-resta, 3.- multiplicación y 4.-division")
operacion= TextBox(app,width=30)
boton= PushButton(app,text="Calcular", command=calcular)
app.display()

#Promedio de n números
from guizero import App, Text, TextBox, PushButton

app = App(title="Promedio n números")
lista = []
suma = 0

def n_numeros():
    global suma
    numeros = cal.value
    if not numeros.isnumeric(): #verifica si el valor ingresado es númerico.
        app.info("Error", "Error, Ingresa valores númericos")
        cal.clear()
    else:
        numeros = float(numeros)
        lista.append(numeros)
        suma += numeros
        cal.clear()
        if len(lista) >= 2:
            boton.show()


def prom():
    if not lista: 
        app.info("Error", "Debes ingresar al menos dos números")
    else:
        app.info("Promedio", f"El promedio de los números es: {suma / len(lista)}")

texto = Text(app, text="Ingresa los números a promediar")
cal = TextBox(app, width=30)
boton2 = PushButton(app, text="Siguiente número", command=n_numeros)
boton = PushButton(app, text="Calcular el promedio", command=prom)
boton.hide()

app.display()

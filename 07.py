#suma de todos los cuadrados de números pares entre 0 y 20 consecutivos
from guizero import App, Text, TextBox, PushButton
app= App(title="Calculadora de cuadrados (0,20)")
suma:int=0
def calcular():
    global suma
    app.info(title="resultado", text=(f"La suma de los cuadrados de los 20 números es: {suma}"))


texto= Text(app, text="Cuadrado de números pares de 0 a 20")
boton1 = PushButton(app, text="Calcular", command=calcular)
for i in range(0,21,2):
        cuadrado= pow(i,2)
        suma += cuadrado
app.display()

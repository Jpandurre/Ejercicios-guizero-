#Obtener la edad promedio de n personas preguntando su año de nacimiento y asumiendo que el año actual es 2023
from guizero import App, Text, TextBox, PushButton
app= App(title="Edad promedio")
lista= []
suma=0
año_act=2023

def n_personas():
    global suma, año_act
    a_nacimiento= int(a_nac.value)
    if a_nacimiento>año_act or a_nacimiento<0:
         app.info(title="Error",text= "Error, el año de nacimiento no puede ser mayor al año actual o 0")
         a_nac.clear()
    else:
         a_nacimiento= int(a_nacimiento)
         lista.append(a_nacimiento)
         edad= año_act-a_nacimiento
         suma += edad
         a_nac.clear()
    if len(lista) >= 2:
        boton.show()

def prom():
     app.info("Promedio", f"La edad promedio es : {suma / len(lista)}")
     
texto= Text(app, text="Ingresa los años de nacimiento")
a_nac = TextBox(app, width=30)
boton2 = PushButton(app, text="Siguiente", command=n_personas)
boton = PushButton(app, text="Calcular el promedio", command=prom)
boton.hide()

app.display()

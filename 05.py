#Se desea saber la cantidad de alumnos que pasaron una materia, son 25 y la calificación aprobatoria es 7
from guizero import App, Text, TextBox, PushButton
app= App(title="Calculadora de promedios")
lista= []
aprobaron= 0
reprobaron= 0

def n_calificaciones():
    global aprobaron, reprobaron
    calificacion= int(cal.value)
    if calificacion>10 or calificacion<0:
         app.info(title="Error",text= "Error. La calificacion se mide del 1 al 10")
         cal.clear()
    else:
         calificacion= int(calificacion)
         lista.append(list)
         if calificacion>=7:
              aprobaron= aprobaron + 1
              cal.clear()
         else:
              reprobaron= reprobaron + 1
              cal.clear()
    if len(lista)==25:
        boton.show()
        boton2.hide()

def resultado():
     app.info("Aprobados y reprobados", f"Aprobaron:{aprobaron} y reprobaron:{reprobaron}")
     
texto= Text(app, text="Ingresa las calificaciones")
cal = TextBox(app, width=30)
boton2 = PushButton(app, text="Siguiente", command=n_calificaciones)
boton = PushButton(app, text="Calcular", command=resultado)
boton.hide()

app.display()

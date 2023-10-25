#Determinar el día de la semana dado un número
from guizero import App, Text, TextBox, PushButton
app= App(title="¿Qué dia de la semana es?")

def dia_sem():
    dias= int(dia.value)
    if dias<=0:
        app.info(title="ERROR", text="Ingresa un número del 1-7")
    else:
        if dias==1:
            app.info(title="Día de la semana", text= "Hoy es Lunes")
            dia.clear()
        elif dias==2:
            app.info(title="Día de la semana", text= "Hoy es Martes")
            dia.clear()
        elif dias==3:
            app.info(title="Día de la semana", text= "Hoy es Miércoles")
            dia.clear()
        elif dias==4:
            app.info(title="Día de la semana", text= "Hoy es Jueves")
            dia.clear()
        elif dias==5:
            app.info(title="Día de la semana", text= "Hoy es Viernes")
            dia.clear()

mensaje= Text(app,text="Ingresa un número del 1-7 para calcular el día")
dia= TextBox(app,width=30)
boton= PushButton(app,text="Calcular", command=dia_sem)
app.display()

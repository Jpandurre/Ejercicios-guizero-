#Una empresa desea calcular el sueldo total de una persona bajo los siguientes rubros: 
#percepciones, sueldo base, 5% canasta básica, 3% prima antiguedad y deducciones.
#Si el salario base excede los $10,000 el ISR es del 30% y menos de ese el 20%.
#Indique de cuánto es el total de la nómina a pagar y cuántos son los impuestos que el patron debe de pagar al sat.
from guizero import App, Text, TextBox, PushButton
app= App(title="Sueldo total")
total_p:int=0 #Total a pagar
i_pagar:int=0 #Impuestos a pagar

def siguiente():
    global total_p, i_pagar
    salariox = int(salario.value)
    if salariox<0:
        app.info("Error", (f"Ingresa números positivos"))
    else:
        cb= salariox*.05 #cb=canasta basica
        pa= salariox*.03 #pa= prima de antiguedad
        if salariox>= 10000:
            isr=salariox*.70
            np= cb+pa+isr #nomina pagar
            isrp= salariox*.30 #isr del patron
            salario.clear()
        else:
            isr= salariox*.80
            np= cb+pa+isr 
            isrp= salariox*.20 
            salario.clear()
    total_p += np
    i_pagar += isrp

def nom_imp():
    app.info(title="Nomina e impuesto", text=(f"La nomina total es {total_p} y el impuesto a pagar es de: {i_pagar}"))

Mensaje= Text(app,text="Ingrese el salario de la persona")
salario= TextBox(app,width=30)
button1= PushButton(app,text="Siguiente", command=siguiente)
button2= PushButton(app,text="Calcular nomina e impuestos", command=nom_imp)
app.display()

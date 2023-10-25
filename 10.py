#Dado el año de nacimiento indique cuántos años va a cumplir una persona 
from guizero import App, Text, TextBox, PushButton
app= App(title="Años a cumplir")

def a_cumplir():
    if int(a_act.value)<int(a_nac.value):
        app.info("ERROR",text="El año actual no puede ser menor al año de nacimiento")
    else:
        a_cum:int= int(a_act.value) - int(a_nac.value)
        app.info("Resultado", text= (f"Vas a culplir {a_cum+1}"))
Mensaje= Text(app,text="Ingresa el año actual")
a_act= TextBox(app,width=30)
Mensaje2= Text(app,text="Ingresa el año de nacimiento")
a_nac= TextBox(app,width=30)
button= PushButton(app,text="Calcular", command=a_cumplir)
app.display()

#Promedio de 3 números
import pyttsx3 
from guizero import App, Text, PushButton, TextBox

engine= pyttsx3.init()
app=App("Aplicación ICI")
def promedio():
    try:
        valor_1= float(num1.value)
        valor_2= float(num2.value)
        valor_3=float(num3.value)
        promedio= (valor_1 + valor_2 + valor_3) / 3
        engine.say(f"el promedio es {promedio:.2f}")
        engine.runAndWait()
        app.info(title="promedio", text=(f"El promedio es {promedio:.2f}"))
        error.clear()
    except:
        error.value= "Ingresa valores númericos"
        engine.say("Ingresa valores númericos")
        engine.runAndWait()
  
text=Text(app,text="Ingresa un número")
num1=TextBox(app,width=30)
separador= Text(app, text="+")
num2=TextBox(app,width=30)
separador= Text(app, text="+")
num3=TextBox(app,width=30)
error= Text(app, text="", color="red")

button = PushButton(app,text="Promediar", command=promedio)
app.display()


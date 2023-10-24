#Resultado de la suma de 3 números
import pyttsx3 
from guizero import App, Text, PushButton, TextBox

engine= pyttsx3.init()
app=App("Aplicación ICI")
def suma():
    
    valor_1= int(num1.value)
    valor_2= int(num2.value)
    valor_3=int(num3.value)
    resultado= str(int(valor_1 + valor_2 + valor_3))
    engine.say(f"el resultado es {resultado}")
    engine.runAndWait()
    app.info(title="resultado", text=(f"El resultado es {resultado}"))
  
text=Text(app,text="Ingresa un número")
num1=TextBox(app,width=30)
separador= Text(app, text="+")
num2=TextBox(app,width=30)
separador= Text(app, text="+")
num3=TextBox(app,width=30)

button = PushButton(app,text="Suma", command=suma)



app.display()

#La tienda "Brankos" debe vender productos a n alumnos, ofrecen tortas, tacos, hotdogs y pizza. 
#Imprime los productos vendidos en total.
from guizero import App, Text, TextBox, PushButton
app= App(title="Brankos, ventas")
torta:int=0
tacos:int=0
hotdogs:int=0
pizza:int=0


def siguiente():
    global torta, tacos, hotdogs, pizza
    match int(producto.value):
        case 1:
            torta += 1
            producto.clear()
        case 2:
            tacos += 1
            producto.clear()
        case 3:
            hotdogs += 1
            producto.clear()
        case 4:
            pizza += 1
            producto.clear()
        case _:
            app.info(title="Error", text="Ingresa un número valido")
    
def calcular():
    app.info(title="Resultado", text=(f"se vendieron: torta:{torta}, tacos:{tacos}, hotdogs:{hotdogs}, pizza:{pizza}"))
    

mensaje= Text(app, text="Menu del dia:")
mensaje.text_size=25 
mensaje.text_color="red"
mensaje2= Text(app, text="1.-Torta, 2.-Tacos, 3.-Hotdog, 4.-Pizza")
mensaje2.text_color="blue"
mensaje3= Text(app, text="Ingresa el número del producto a ordenar")
producto= TextBox(app,width=25)
boton= PushButton(app,text="Siguiente", command=siguiente)
boton2= PushButton(app, text="Calcular", command=calcular)

app.display()

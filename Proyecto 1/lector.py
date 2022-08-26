from xml.dom import minidom
from Estructura import ListaEnlazada

class lector():
    #inicializa
    def __init__(self):
        pass
    def cargar(direccion):
            
        try:
            # contructor de lista enlazada para la informacion
            lista=ListaEnlazada()
            # se lee el archivo
            doc = minidom.parse(f"{direccion}")
            pacientes = doc.getElementsByTagName("paciente")
            n = 0
            for  datos in pacientes:
                periodos = datos.getElementsByTagName("periodos")[0]
                tamanio = datos.getElementsByTagName("m")[0]

                if int(tamanio.firstChild.data)<=10000 and int(tamanio.firstChild.data)%10 == 0 and int(periodos.firstChild.data)<=10000:
                    n = n+1
                    nombre = datos.getElementsByTagName("nombre")[0]
                    edad = datos.getElementsByTagName("edad")[0]
                    celdas_contagiadas = datos.getElementsByTagName("celda")
                    # Se crea cadena con todos los datos de las celdas contagiadas
                    contagiados= ""
                    i=0
                    for contagiada in celdas_contagiadas:
                        i+=1
                        if i==1:
                            contagiados= contagiados+ contagiada.getAttribute("f") +";"+  contagiada.getAttribute("c")
                        else:
                            contagiados= contagiados+";"+contagiada.getAttribute("f") +";"+ contagiada.getAttribute("c")
                    #Se crea cadena de toda la informacion 
                    cadena=f"{n},{nombre.firstChild.data},{edad.firstChild.data},{periodos.firstChild.data},{tamanio.firstChild.data},{contagiados}"
                    
                    try:
                        # se incerta informacion en la estructura de lista enlazada
                        lista.insertar(cadena)
                    except:
                        print(" error al cargar datos en lista")

            #  Se imprime la informacion de la estructura (solo para comprobacion)
            for d in lista.imprimir():
                print(str(d) )
        except:
            print("No se pudo leer el archivo, revisar que la direccion sea correcta")
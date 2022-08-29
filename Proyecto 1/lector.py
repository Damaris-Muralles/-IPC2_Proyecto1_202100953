from xml.dom import minidom
from Estructura import ListaEnlazada

class lector_archivo():
    #inicializa
    def __init__(self):
        self.lista =ListaEnlazada()
    def cargar(self, direccion):
            
        try:
            
            # se lee el archivo
            doc = minidom.parse(f"{direccion}")
            pacientes = doc.getElementsByTagName("paciente")
            n = 0
            for  datos in pacientes:
                periodos = datos.getElementsByTagName("periodos")[0]
                tamanio = datos.getElementsByTagName("m")[0]

                #if int(tamanio.firstChild.data)<=10000 and int(tamanio.firstChild.data)%10 == 0 and int(periodos.firstChild.data)<=10000:
                   
                nombre = datos.getElementsByTagName("nombre")[0]
                edad = datos.getElementsByTagName("edad")[0]
                celdas_contagiadas = datos.getElementsByTagName("celda")
                # Se crea cadena con todos los datos de las celdas contagiadas
                contagiados= ""
                for contagiada in celdas_contagiadas:
                    
                        contagiados= contagiados+ contagiada.getAttribute("f") +";"+  contagiada.getAttribute("c")+ ";"
                    
                #Se crea cadena de toda la informacion 
                cadena=f"{nombre.firstChild.data},{edad.firstChild.data},{periodos.firstChild.data},{tamanio.firstChild.data},{contagiados}"
                
                try:
                    # se incerta informacion en la estructura de lista enlazada
                    self.lista.insertar(cadena)
                except:
                    print(" error al cargar datos en lista")

            #  Se imprime la informacion de la estructura (solo para comprobacion)
            for d in self.lista.imprimir():
                print(str(d) )
        except:
            print("No se pudo leer el archivo, revisar que la direccion sea correcta")
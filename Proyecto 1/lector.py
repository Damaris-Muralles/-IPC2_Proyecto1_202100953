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
            print("VISTA DE PACIENTES EN EL DOCUMENTO:")
            for  datos in pacientes:
                periodos = datos.getElementsByTagName("periodos")[0]
                tamanio = datos.getElementsByTagName("m")[0]

                if int(tamanio.firstChild.data)<=10000 and int(tamanio.firstChild.data)%10 == 0 and int(periodos.firstChild.data)<=10000:
                    n=n+1
                    nombre = datos.getElementsByTagName("nombre")[0]
                    edad = datos.getElementsByTagName("edad")[0]
                    celdas_contagiadas = datos.getElementsByTagName("celda")
                    # Se crea cadena con todos los datos de las celdas contagiadas
                    contagiados= ""
                    for i in range(1,int(tamanio.firstChild.data)):
                        for j in range(1,int(tamanio.firstChild.data)):
                            for contagiada in celdas_contagiadas:
                                if contagiada.getAttribute("f")!="0" and contagiada.getAttribute("c")!="0":
                                    if int(contagiada.getAttribute("f"))== i and int(contagiada.getAttribute("c"))==j:
                                        contagiados= contagiados+ contagiada.getAttribute("f") +";"+  contagiada.getAttribute("c")+ ";"
                        
                    #Se crea cadena de toda la informacion 
                    cadena=f"{nombre.firstChild.data},{edad.firstChild.data},{periodos.firstChild.data},{tamanio.firstChild.data},{contagiados}"
                   
                    print(f"{n}. {nombre.firstChild.data}")
                    try:
                        # se incerta informacion en la estructura de lista enlazada
                        self.lista.insertar(cadena)
                    except:
                        print(" Error al cargar datos en lista")
                  
            #  Se imprime la informacion de la estructura (solo para comprobacion de funcionamiento)
            #for d in self.lista.imprimir():
             #   print(str(d))

        except:
            print("No se pudo leer el archivo, revisar que la direccion sea correcta")
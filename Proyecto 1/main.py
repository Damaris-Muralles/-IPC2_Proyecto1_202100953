import sys
from Estructura import ListaEnlazada
from lector import lector_archivo
from Estructura_grafica import ListaGrafica
import re
def menu():
    print("=============================== Menu ==============================")
    print("=  1. Cargar archivo                                              =")
    print("=  2. Simulacion de desarrollo de la enfermedad                   =")
    print("=  3. Generar archivo                                             =")
    print("=  4. salir                                                       =")
    print("===================================================================")
    
    opcion= int(input("Ingrese la opcion: "))

    # Condicionales para entrar a opciones
    if opcion == 1:
        print("========================= Cargar archivo ==========================")
        print("")
        direccion = input("Ingrese la direccion del archivo: ")
        print("") 
        archivo.cargar(direccion)
        print("")
        
        print(listapaciente.cabeza.siguiente[1])
        input("<<<<Presione una tecla para salir>>>>")
        print(" ")
        
    elif opcion == 2:
        print("========================= Elegir Paciente =========================")
        print("")
        nombre_paciente= input("Ingrese el nombre completo del paciente: ")
        print("PROCESANDO LOS DATOS....")
        datos_paciente_elegido(nombre_paciente)
        print("GRAFICANDO REJILLA INICIAL....")
        grafica.graficarLista(int(listapaciente[3]), (int(listapaciente[3])*int(listapaciente[3])))
        grafica.imprimir()
        menuperiodo=True
        while menuperiodo:
            opcion_grafica = menu_manejo()
            if opcion_grafica == 3:
                menuperiodo=False
        print("")
        input("<<<<Presione una tecla para salir>>>>")
        print(" ") 
    elif opcion == 3:
        print("pulso 3")
    else:
        return opcion

def datos_paciente_elegido(nombre_paciente):
    #Para buscar el dato entre la cadena
    listapaciente.borrar()
    grafica.borrar()
    dato_buscar = re.compile(nombre_paciente)
    f=-1
    contador=-1
    inicio=0
    #se usa la funcion de imprimir de la lista para buscar la coincidencia entre la cadena
    for d in archivo.lista.imprimir():
        f=f+1
        # mostrara un objeto con un atributo span( intervalo en el que se encuentra la conicidencia)
        coincidencia = dato_buscar.search(d)
        # solo entrara si se encuentra una coincidencia
        if coincidencia != None:
            # simulacion de la funcion split en listas
            print("dato de prueba")
            print(archivo.lista[f])
            informacion=str(archivo.lista[f])
            separador =re.compile(r",")
            separar= separador.finditer(informacion)
            
            for s in separar:
                contador += 1
                print("dato de prueba")
                print(f"----> {s}")
                # se agrega a una nueva lista con toda informacion del paciente elegido
                if contador==0:
                    listapaciente.insertar(informacion[0:s.start()])
                    inicio =  s.end()
                else:
                    listapaciente.insertar(informacion[inicio:s.start()])
                    inicio= s.end()

            print("datos de prueba")     
            for p in listapaciente.imprimir():
                print(str(p) ) 
            # se crea patron de celulas sanas y contagiadas
            fila=-1
            columna=-1
            patron=""
            datoanterior=0
            # se establece largo de la cadena por medio de los for
            for i in range(int(listapaciente[3])):
                print(f"i {i}")
                for j in range(int(listapaciente[3])):
                    print(f"j {j}")
                    # segun las condiciones entra a realizar el split de datos
                    if fila ==-1 and columna == -1:
                        contador1=-1
                        separador =re.compile(r";")
                        separar= separador.finditer(informacion)
                        for celda in separar:
                            contador1 += 1
                            print(f"contador {contador1}")
                            print(f"datoanterior {datoanterior}")
                            if (fila ==-1 or columna == -1) and datoanterior==contador1:
                                if contador1%2==0:
                                    fila=int(informacion[inicio:celda.start()])
                                    inicio =  celda.end()
                                    datoanterior= contador1+1
                                else:
                                    columna=int(informacion[inicio:celda.start()])
                                    inicio =  celda.end()
                                    datoanterior=contador1+1
                    print(f"fila {fila}")     
                    print(f"columna {columna}")           
                    # mientras las filas y columnas coicidan con las contagiadas se ingresara un 1 al patron
                    if (i+1)==fila and (j+1)== columna :
                        print("entrando a coincidencia")
                        patron = patron + "1"
                        fila=-1
                        columna =-1
                        print(patron)
                    elif (i+1)!= fila or (j+1)!=columna :
                        print("no coincidencia")
                        patron = patron + "0"
                        print(patron)
            print("datos de prueba")     
            for p in listapaciente.imprimir():
                print(str(p) ) 
            print("patron final")
            print(patron)
            guardarPatron(patron,int(listapaciente[3]) ,int(listapaciente[3]) )   

def guardarPatron(patron, filas, columnas):
    #recorremos la cadena del string guardandolo en la lista
        for i in range(0, filas):
            for j in range(0, columnas):
                estado = patron[(i*columnas)+j]
                row = str(i)
                col = str(j)
                #print("estado: "+estado+" fila: "+row+" columna: "+col)
                grafica.insertar(estado, row, col)

def menu_manejo():
    print("=============================== Menu ==============================")
    print("=  1. Ejecutar periodos paso a paso                               =")
    print("=  2. Ejecutar automaticamente                                    =")
    print("=  3. Salir                                                       =")
    print("===================================================================")
    
    opcion_manejo= int(input("Ingrese la opcion: "))
    if opcion_manejo == 1:
        print("1")
    elif opcion_manejo ==2:
        print("2")
    else:
        return opcion_manejo

def ejecucion_periodos():
    pass

if __name__ == '__main__':
    archivo=lector_archivo()
    grafica = ListaGrafica()
    listapaciente=ListaEnlazada()
    listgrafica=ListaEnlazada()
    #  Se inicia el menu
    while True:
        opcion = menu()
        if opcion == 4:
            sys.exit(0)
        
   # C:\Users\pedrto\Desktop\prueba.xml
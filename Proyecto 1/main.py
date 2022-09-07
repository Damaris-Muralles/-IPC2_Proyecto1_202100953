import sys
from time import sleep
from Estructura import ListaEnlazada
from lector import lector_archivo
from Estructura_grafica import ListaGrafica
from Constructor_Archivo import Archivo_salida
import re

def menu():
    #print("vista antes del menu")
    #for dp in listapaciente.imprimir():
     #   print(dp)
    print("=========================== Menu General ==========================")
    print("=  1. Cargar archivo                                              =")
    print("=  2. Simulacion del desarrollo de la enfermedad                  =")
    print("=  3. Generar archivo de salida                                   =")
    print("=  4. salir                                                       =")
    print("===================================================================")
     
    print("")
    opcion= int(input("Ingrese la opcion: "))
    print("")
    # Condicionales para entrar a opciones
    if opcion == 1:
        
        print("========================= Cargar archivo ==========================")
        print("")
        direccion = input("Ingrese la direccion del archivo: ")
        print("") 
        archivo.cargar(direccion)
        print("")
        print("===================================================================")
        print("")
        input("<<<<Presione Enter para salir>>>>")
        print(" ")
        
    elif opcion == 2:
        print("========================= Elegir Paciente =========================")
        print("")
        nombre_paciente= input("Ingrese el nombre completo del paciente: ")
        print("")
        print("PROCESANDO LOS DATOS....")
        res= datos_paciente_elegido(nombre_paciente)
        print("") 
        sleep(1)
        if res==True: 
         simulacion()
        else:
            print("No se encontro al paciente en el registro")
            print("")
            print("===================================================================")
            sleep(1)
        print("")
        
    elif opcion == 3:
        print("CONSTRUYENDO ARCHIVO....")
        print("")
        datos_paciente_elegido("Todos")
        for dpt in listapaciente.imprimir():
            #print(dpt)
            generararchivo.construir(dpt,int(listapaciente.contador))
    else:
        return opcion

def datos_paciente_elegido(nombre_paciente):
    #Para buscar el dato entre la cadena

    listapaciente.borrar()
    if nombre_paciente!="Todos":
        dato_buscar = re.compile(nombre_paciente)
    f=-1
    contador=-1
    #se usa la funcion de imprimir de la lista para buscar la coincidencia entre la cadena
    for d in archivo.lista.imprimir():
        inicio=0
        listgrafica.borrar()
        f=f+1
        # mostrara un objeto con un atributo span( intervalo en el que se encuentra la conicidencia)
        if nombre_paciente=="Todos":
            coincidencia = "t"
        else:
            coincidencia = dato_buscar.search(d)
        # solo entrara si se encuentra una coincidencia
        if coincidencia != None:
            # simulacion de la funcion split en listas
            
            #print("dato de prueba")
            #print("imprimiendo datos: ",f, " ",archivo.lista[f])
            informacion=str(archivo.lista[f])
            separador =re.compile(r",")
            separar= separador.finditer(informacion)
            
            for s in separar:
                contador += 1
                #print("dato de prueba")
                #print(f"----> {s}")
                # se agrega a una nueva lista con toda informacion del paciente elegido
                if contador==0:
                    listapaciente.insertar(informacion[0:s.start()])
                    inicio =  s.end()
                else:
                    listapaciente.insertar(informacion[inicio:s.start()])
                    inicio= s.end()

            #print("datos prueba")     
            #for p in listapaciente.imprimir():
            #    print(str(p) ) 
            # se crea patron de celulas sanas y contagiadas
            fila=-1
            columna=-1
            patron=""
            datoanterior=0
            # se establece largo de la cadena por medio de los for
            if  nombre_paciente=="Todos":
                m=int(listapaciente[3+(f*7)])
            else:
                m=int(listapaciente[3])
            for i in range(m):
                #print(f"i {i}")
                for j in range(m):
                    #print(f"j {j}")
                    # segun las condiciones entra a realizar el split de datos
                    if fila ==-1 and columna == -1:
                        contador1=-1
                        separador =re.compile(r";")
                        separar= separador.finditer(informacion)
                        for celda in separar:
                            contador1 += 1
                            #print(f"contador {contador1}")
                            #print(f"datoanterior {datoanterior}")
                            if (fila ==-1 or columna == -1) and datoanterior==contador1:
                                if contador1%2==0:
                                    fila=int(informacion[inicio:celda.start()])
                                    inicio =  celda.end()
                                    datoanterior= contador1+1
                                else:
                                    columna=int(informacion[inicio:celda.start()])
                                    inicio =  celda.end()
                                    datoanterior=contador1+1
                    #print(f"fila {fila}")     
                    #print(f"columna {columna}")           
                    # mientras las filas y columnas coicidan con las contagiadas se ingresara un 1 al patron
                    if (i+1)==fila and (j+1)== columna :
                        #print("entrando a coincidencia")
                        patron = patron + "1"
                        fila=-1
                        columna =-1
                    elif (i+1)!= fila or (j+1)!=columna :
                        #print("no coincidencia")
                        patron = patron + "0"
           
            listgrafica.insertar(patron)
            
            if nombre_paciente=="Todos":
                #print("tamaño: ", listapaciente[3+(f*7)])
                guardarPatron(patron,int(listapaciente[3+(f*7)]) ,int(listapaciente[3+(f*7)]))
                simulacion_para_el_archivo(f)
            else:
                guardarPatron(patron,int(listapaciente[3]) ,int(listapaciente[3]))
                print("")
                print("Datos del paciente seleccionado:")     
                for p in listapaciente.imprimir():
                    print(str(p)) 
                return True
    if coincidencia==None:
        return False       

def guardarPatron(patron, filas, columnas):
    grafica.borrar()
    #recorremos la cadena del string guardandolo en la lista
    
    for i in range(0, filas):
        for j in range(0, columnas):
            estado = patron[(i*columnas)+j]
            row = str(i)
            col = str(j)
            #print("estado: "+estado+" fila: "+row+" columna: "+col)
            grafica.insertar(estado, row, col)

def simulacion():
    try:
        print("======================== Interar patrones ========================")
        print("")
        patroninicial=listgrafica[0]
        print("Patron inicial")
        print("Numero de celulas sanas: ", patroninicial.count("0"))
        print("Numero de celulas contagiadas: ", patroninicial.count("1"))
        print("")
        grafica.graficarLista(int(listapaciente[3]), (int(listapaciente[3])*int(listapaciente[3])),0)
        print("")
        sleep(3)
        menuperiodo=True
        while menuperiodo:
            opcion_grafica = menu_manejo()
            if opcion_grafica == 3:
                menuperiodo=False
        print("")
    except:
        pass

def menu_manejo():
    # Nos aseguramos que el patron sea el inicial, esto por si se quiere repetir mas veces
    guardarPatron(listgrafica[0],int(listapaciente[3]) ,int(listapaciente[3])) 
    contador_periodos=0
    paso=True
    cp = 0
    while paso:
        print("")
        opciongrafica= int(input("1. Siguiente  2. Automatico  3. Salir ---> "))
        print("")
        print("==================================================================")
        if opciongrafica==1 :
            if contador_periodos<int(listapaciente[2]) :
                paso_siguiente=1
                contador_periodos+=1
                #print(contador_periodos)
                #print(cp)
                if cp == 0:
                    print("")
                    print(f"Graficando periodo: {contador_periodos}")
                    cp= ejecucion_periodos(contador_periodos,0,0)
                    if cp==1 and contador_periodos==1:
                        print("")
                        print("Se a determinado una coincidencia en los patrones")
                        print("")
                        listapaciente.insertar("Mortal")
                        listapaciente.insertar(f"{contador_periodos}")
                        listapaciente.insertar("0")
                        print("Enfermedad: ", listapaciente[4])
                        print("Periodo en que se repite el patron inical: ", listapaciente[5])
                        contador_periodos=int(listapaciente[2])
                    elif cp==1 and contador_periodos!=1:
                        print("")
                        print("Se a determinado una coincidencia en los patrones")
                        print("")
                        listapaciente.insertar("Grave")
                        listapaciente.insertar(f"{contador_periodos}")
                        listapaciente.insertar("0")
                        print("Enfermedad: ", listapaciente[4])
                        print("Periodo en que se repite el patron inical: ", listapaciente[5])
                        contador_periodos=int(listapaciente[2])
                    elif cp>0:
                        print("")
                        print("Se a determinado una coincidencia en los patrones")
                        print("")
                        if contador_periodos-cp == 1:
                            listapaciente.insertar("Mortal")
                        else:
                            listapaciente.insertar("Grave")
                        listapaciente.insertar(f"{cp}")
                        listapaciente.insertar(f"{contador_periodos-cp}")
                        contador_periodos=int(listapaciente[2])
                        print("Enfermedad: ", listapaciente[4])
                        print(f"Patron del periodo {listapaciente[5]} se repite en {listapaciente[6]} periodos")
                #print(int(listapaciente[2]))        
                if cp == 0 and contador_periodos==int(listapaciente[2]):
                        print("")
                        print("No se observo coincidencia en los patrones")
                        listapaciente.insertar("Leve")
                        listapaciente.insertar("0")
                        listapaciente.insertar("0")  
                        print("") 
                        print("Enfermedad: ", listapaciente[4])
            else:
                print("")
                print("Se ha llegado al limite de periodos propuestos\no se encontro coincidencia")
        elif opciongrafica==2:
            #prueba
            #print("Desde donde comienza automaticamente: ", contador_periodos)
            if contador_periodos<int(listapaciente[2]):
                if contador_periodos==0 or paso_siguiente==1:
                    contador_periodos+=1
                    paso_siguiente=0
                for i in range(contador_periodos,int(listapaciente[2])+1):
                    
                    contador_periodos=i
                    if cp == 0:
                        print("")
                        print("==================================================================")
                        print("")
                        print(f"Graficando periodo: {i}")
                        cp = ejecucion_periodos(i,0,0)
                        if cp==1 and contador_periodos==1:
                            print("")
                            print("Se a determinado una coincidencia en los patrones")
                            listapaciente.insertar("Mortal")
                            listapaciente.insertar(f"{contador_periodos}")
                            listapaciente.insertar("0")
                            print("")
                            print("Enfermedad: ", listapaciente[4])
                            print("Periodo en que se repite el patron inical: ", listapaciente[5])
                        elif cp==1 and contador_periodos!=1:
                            print("")
                            print("Se a determinado una coincidencia en los patrones")
                            listapaciente.insertar("Grave")
                            listapaciente.insertar(f"{contador_periodos}")
                            listapaciente.insertar("0")   
                            print("")
                            print("Enfermedad: ", listapaciente[4])
                            print("Periodo en que se repite el patron inical: ", listapaciente[5])
                        elif cp>1:
                            print("")
                            print("Se a determinado una coincidencia en los patrones")
                            print("")
                            if contador_periodos-cp == 1:
                                listapaciente.insertar("Mortal")
                            else:
                                listapaciente.insertar("Grave")
                            listapaciente.insertar(f"{cp}")
                            listapaciente.insertar(f"{contador_periodos-cp}")
                            print("Enfermedad: ", listapaciente[4])
                            print(f"Patron del periodo {listapaciente[5]} se repite en {listapaciente[6]} periodos")
                        sleep(1)
                    if cp == 0 and i==int(listapaciente[2]):
                        print("")
                        print("No se observo coincidencia en los patrones")
                        listapaciente.insertar("Leve")
                        listapaciente.insertar("0")
                        listapaciente.insertar("0")    
                        print("")    
                        print("Enfermedad: ", listapaciente[4])
            else:
                print("")
                print("Se ha llegado al limite de periodos propuestos\no se encontro coincidencia")        
        else:
            return opciongrafica
      
def ejecucion_periodos(periodo,op,nump):
    patron= grafica.iterar(int(listapaciente[3+(nump*7)]),int(listapaciente[3+(nump*7)]))
    guardarPatron(patron,int(listapaciente[3+(nump*7)]) ,int(listapaciente[3+(nump*7)])) 
    if op==0:
        print("Numero de celulas sanas: ", patron.count("0"))
        print("Numero de celulas contagiadas: ", patron.count("1"))
        print("")
        grafica.graficarLista(int(listapaciente[3]), (int(listapaciente[3])*int(listapaciente[3])),periodo)
    
    if patron.count("0")== (int(listapaciente[3+(nump*7)])*int(listapaciente[3+(nump*7)])):
        coincidepatron=0
    else:
        coincidepatron=listgrafica.buscar(patron)
    
    listgrafica.insertar(patron)
    #solo comprobacion
    #print(periodo)
    #for  g in listgrafica.imprimir():
       # print(str(g)) 
    return coincidepatron
    
def simulacion_para_el_archivo(nump):
    contador_periodos=0
    cp = 0
    #print("lectura de periodo: ", int(listapaciente[2+(nump*7)]))
    
    if contador_periodos<int(listapaciente[2+(nump*7)]):
        for i in range(1,int(listapaciente[2+(nump*7)])+1):
            contador_periodos=i
            if cp == 0:
                cp = ejecucion_periodos(i,1,nump)
                if cp==1 and contador_periodos==1:
                    listapaciente.insertar("Mortal")
                    listapaciente.insertar(f"{contador_periodos}")
                    listapaciente.insertar("0")
                elif cp==1 and contador_periodos!=1:
                    listapaciente.insertar("Grave")
                    listapaciente.insertar(f"{contador_periodos}")
                    listapaciente.insertar("0")   
                elif cp>1:
                    if contador_periodos-cp == 1:
                        listapaciente.insertar("Mortal")
                    else:
                        listapaciente.insertar("Grave")
                    listapaciente.insertar(f"{cp}")
                    listapaciente.insertar(f"{contador_periodos-cp}")
            if cp == 0 and i==int(listapaciente[2+(nump*7)]):
                listapaciente.insertar("Leve")
                listapaciente.insertar("0")
                listapaciente.insertar("0")  
    #print("Datos despues de interar:")     
    #for p in listapaciente.imprimir():
     #   print(str(p))         

if __name__ == '__main__':
    archivo=lector_archivo()
    generararchivo=Archivo_salida()
    grafica = ListaGrafica()
    listapaciente=ListaEnlazada()
    listgrafica=ListaEnlazada()
    #  Se inicia el menu
    while True:
        opcion = menu()
        if opcion == 4:
            sys.exit(0)
        
   
import sys
from lector import lector

def menu():
    print("====================== Menu ======================")
    print("=  1. Cargar archivo                             =")
    print("=  2. Seleccionar Paciente                       =")
    print("=  3. Generar archivo                            =")
    print("=  4. salir                                      =")
    print("==================================================")
    opcion= int(input("Ingrese la opcion: "))

    # Condicionales para entrar a opciones
    if opcion == 1:
        print("")
        direccion = input("Ingrese la direccion del archivo: ")
        print("") 
        lector.cargar(direccion)
        print("")
        input("<<<<Presione una tecla para salir>>>>")

    elif opcion == 2:
        print("pulso 2")
    elif opcion == 3:
        print("pulso 3")
    else:
        return opcion
        
if __name__ == '__main__':
    #  Se inicia el menu
    while True:
        opcion = menu()
        if opcion == 4:
            sys.exit(0)
        
   # C:\Users\pedrto\Desktop\prueba.xml
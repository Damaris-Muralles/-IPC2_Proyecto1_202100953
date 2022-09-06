from Estructura import ListaEnlazada
import xml.etree.cElementTree as ET
from xml.dom import minidom

class Archivo_salida():
    def __init__(self):
        self.listainformacion=ListaEnlazada()
        
    def datos(self,dato):
        self.listainformacion.insertar(dato)

    def construir(self, dat, tam):
        self.datos(dat)
        if tam==int(self.listainformacion.contador):
            #print("datos en contructor de archivo")
            #for dato in self.listainformacion.imprimir():
                #print(dato)
            #Construimos el xml
            pacientes = ET.Element("pacientes")
            contador=int(self.listainformacion.contador/7)
            #print(contador)
            #i=0
            for i in range(contador):
                paciente = ET.SubElement(pacientes,'paciente')
                datospersonales =ET.SubElement(paciente,'datospersonales')
                ET.SubElement(datospersonales, "nombre").text = f"{str(self.listainformacion[0+(i*7)])}"
                ET.SubElement(datospersonales, "edad",).text = f"{str(self.listainformacion[1+(i*7)])}"
                ET.SubElement(paciente, "periodos").text = f"{str(self.listainformacion[2+(i*7)])}"
                ET.SubElement(paciente, "m",).text = f"{str(self.listainformacion[3+(i*7)])}"
                ET.SubElement(paciente, "resultado").text = f"{str(self.listainformacion[4+(i*7)])}"
                if int(self.listainformacion[5+(i*7)])!=0:
                    ET.SubElement(paciente, "n").text = f"{str(self.listainformacion[5+(i*7)])}"
                if int(self.listainformacion[6+(i*7)])!=0:
                    ET.SubElement(paciente, "n1").text = f"{str(self.listainformacion[6+(i*7)])}"
            
            with open("ArchivoSalida.xml", "w" ,encoding= "utf-8") as f:
                f.write(self.estructurando(pacientes)) 
            
            f.close()
            print("¡ARCHIVO COMPLETADO!")

    def estructurando(self, elem):
        rough_string = ET.tostring(elem, 'utf-8').decode('utf8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")     

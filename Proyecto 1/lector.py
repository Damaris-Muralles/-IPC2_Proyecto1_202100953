from xml.dom import minidom

doc = minidom.parse("Tarea1.xml")
pacientes = doc.getElementsByTagName("datospersonales")
n = 0
for  datos in pacientes:
    n = n+1
    nombre = datos.getElementsByTagName("nombre")[0]
    edad = datos.getElementsByTagName("edad")[0]
    print("paciente no."+ str(n))
    print("nombre:%s" % nombre.firstChild.data)
    print("edad:%s" % edad.firstChild.data)
    
from graphviz import Digraph

class Nodo:
    def __init__(self, estado=None, fila=None, columna=None):
        self.estado = estado
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anterior = None

class ListaGrafica:
    def __init__(self):
        self.head = None
        self.end = None
        self.tam=0

    def insertar(self, estado, fila, columna):
        nuevoNodo = Nodo(estado, fila, columna)
        if self.head == None:
            self.head = nuevoNodo
            self.end = self.head
        else:
            nuevoNodo.anterior= self.end
            self.end.siguiente = nuevoNodo
            self.end = nuevoNodo
        self.tam += 1

    def imprimir(self):              
        print("*** Inicio de lista ***")
        print()
        nodoTemporal = Nodo("",0,0)
        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo:"+str(contador)+" -> "+nodoTemporal.estado+" fila: "+nodoTemporal.fila+
            "columna: "+nodoTemporal.columna)
            nodoTemporal = nodoTemporal.siguiente
        print()
        print("*** Lista Terminada ***")

    def borrar(self):
        for i in range(self.tam-1):
            #creamos un nodo temporal
            nodoTemporal = Nodo("")

            #el temporal empieza en la cabeza
            nodoTemporal = self.head

            #Mientras que el temporal no sea nulo
            while nodoTemporal != None:
            
            #validamos si ese nodo es el que busco
                if nodoTemporal != None:

                    #Si ese nodo es la cabeza
                    if nodoTemporal == self.head:
                        print("Borrando dato en la cabeza")
                        self.head = self.head.siguiente
                        nodoTemporal.siguiente = None
                        self.head.anterior = None
        
                nodoTemporal = nodoTemporal.siguiente
        nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.head

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:
        
        #validamos si ese nodo es el que busco
            if nodoTemporal!= None:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.head:
                    print("Borrando dato en la cabeza")
                    self.head = self.head.siguiente
                    nodoTemporal.siguiente = None


            nodoTemporal = nodoTemporal.siguiente  
        self.tam=0
    """

    def iterar(self):
        print("*** cadena ***")
        print()
        cadena= ""
        nodoTemporal = Nodo("",0,0)
        actual = Nodo("",0,0)
        nodoTemporal = self.head
        actual =self.head.siguiente
        contador=0
        i=0
        while nodoTemporal != None:
            contador = 1
            if contador<=nodoTemporal.columna:
                if contador==1 and (i+1)==1:
                    if nodoTemporal.estado== "0":
                        contagiado=0
                        pass
                    else:
                        pass
                elif contador==nodoTemporal.columna and (i+1)!=nodoTemporal.fila:
                    pass
                elif (i+1)==nodoTemporal.fila and contador==1:
                    pass
                elif (i+1)==nodoTemporal.fila and contador==nodoTemporal.columna:
                    pass
                
            contador += 1

            print("Nodo:"+str(contador)+" -> "+nodoTemporal.estado+" fila: "+nodoTemporal.fila+
            "columna: "+nodoTemporal.columna)
            nodoTemporal = nodoTemporal.siguiente
        print()
        print("*** Terminada ***")
        pass
    """       

    def graficarLista(self, columnas, nuNodos):
        dot = Digraph('G', filename='Inicial.dot', engine='dot', format='svg')
        dot.attr(rankdir = "TB")
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'
        dot.node_attr['style'] = 'filled'

        nodoTemporal = Nodo("",0,0)
        nodoTemporal = self.head

        flag = False
        contador = 0
        contSubgrap = 1
        c = Digraph('child')
        c.attr(rank='same')
        while nodoTemporal != None:

            if flag:   
                c = Digraph('child'+str(contSubgrap))
                contSubgrap += 1            
                c.attr(rank='same')
                flag = False

            contador += 1

            if nodoTemporal.estado == '1':
                c.node(str(contador), "", color="blue", group=str(contador%(columnas)))

            else:
                c.node(str(contador), "", fillcolor="white", group=str(contador%(columnas)))
            
            if contador%columnas == 0:
                dot.subgraph(c)
                flag = True
                

            nodoTemporal = nodoTemporal.siguiente

        
        for i in range(1,contador):
            if i+columnas <= nuNodos:
                dot.edge(str(i), str(i+columnas))

            if i%columnas != 0:
                dot.edge(str(i), str(i+1))
        print("GRAFICA COMPLETADA!")
        dot.view()

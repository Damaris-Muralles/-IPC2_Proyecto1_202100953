from graphviz import Digraph

class Node:
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
        nuevoNodo = Node(estado, fila, columna)
        if self.head == None:
            self.head = nuevoNodo
            self.end = self.head
        else:
            nuevoNodo.anterior= self.end
            self.end.siguiente = nuevoNodo
            self.end = nuevoNodo
        self.tam += 1

    def imprimir(self): 
        #print("tamaño")
        #print(self.tam)
        nodoTemporal = Node("",0,0)
        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            #print("Nodo:"+str(contador)+" -> "+nodoTemporal.estado+" fila: "+nodoTemporal.fila+
            #"columna: "+nodoTemporal.columna)
            nodoTemporal = nodoTemporal.siguiente
        #print()
        
    def borrar(self):
        for i in range(self.tam-1):
            #creamos un nodo temporal
            nodoTemporal = Node("")

            #el temporal empieza en la cabeza
            nodoTemporal = self.head

            #Mientras que el temporal no sea nulo
            while nodoTemporal != None:
            
            #validamos si ese nodo es el que busco
                if nodoTemporal != None:

                    #Si ese nodo es la cabeza
                    if nodoTemporal == self.head:
                        self.head = self.head.siguiente
                        nodoTemporal.siguiente = None
                        self.head.anterior = None
        
                nodoTemporal = nodoTemporal.siguiente
        nodoTemporal = Node("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.head

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:
        
        #validamos si ese nodo es el que busco
            if nodoTemporal!= None:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.head:
                    #print("Borrando dato en la cabeza")
                    self.head = self.head.siguiente
                    nodoTemporal.siguiente = None


            nodoTemporal = nodoTemporal.siguiente  
        self.tam=0
    
    def iterar(self, maxfila, maxcolumna):
        #cadena que guarda el nuevo patron
        cadena= ""
        actual = Node("",0,0)
        actual = self.head
        
        while actual != None:
            # contadores para validacion
            contador=0
            numcontagiado=0
            # siempre que se cambia a un nuevo nodo para su analisis 
            # se inicializa el nodo temporal nuevamente
            nodoTemporal = Node("",0,0)
            nodoTemporal =self.head

            while nodoTemporal!=None:

                if int(actual.fila) == 0 and int(actual.columna)== 0: 
                    if actual.siguiente.estado== "1" and contador==0:
                        numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)+1 and nodoTemporal.columna== actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1

                elif int(actual.fila)==0 and int(actual.columna)>0 and int(actual.columna)< int(maxcolumna)-1:
                    if contador==0:
                        if actual.siguiente.estado== "1":
                            numcontagiado+=1
                        if actual.anterior.estado=="1":
                            numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)+1 and nodoTemporal.columna == actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1  
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1
                elif int(actual.fila)==0 and int(actual.columna)==int(maxcolumna)-1:
                    if actual.anterior.estado== "1" and contador==0:
                        numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)+1 and nodoTemporal.columna == actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1
                elif int(actual.fila)==int(maxfila)-1 and int(actual.columna)==0:
                    if actual.siguiente.estado== "1" and contador==0:
                        numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)-1 and nodoTemporal.columna== actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1
                elif int(actual.fila)==int(maxfila)-1 and int(actual.columna)>0 and int(actual.columna)< int(maxcolumna)-1:
                    if contador==0:
                        if actual.siguiente.estado== "1":
                            numcontagiado+=1
                        if actual.anterior.estado=="1":
                            numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)-1 and nodoTemporal.columna == actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1  
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1
                elif int(actual.fila)==int(maxfila)-1 and int(actual.columna)==int(maxcolumna)-1:
                    if actual.anterior.estado== "1" and contador==0:
                        numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)-1 and nodoTemporal.columna == actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1
                elif int(actual.columna)==0 and int(actual.fila)>0 and int(actual.fila)< int(maxfila)-1:
                    if actual.siguiente.estado== "1" and contador==0:
                        numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)-1 and nodoTemporal.columna== actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1   
                    if int(nodoTemporal.fila) == int(actual.fila)+1 and nodoTemporal.columna== actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1

                elif int(actual.columna)==int(maxcolumna)-1 and int(actual.fila)>0 and int(actual.fila)< int(maxfila)-1:
                    if actual.anterior.estado== "1" and contador==0:
                        numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)-1 and nodoTemporal.columna== actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1   
                    if int(nodoTemporal.fila) == int(actual.fila)+1 and nodoTemporal.columna== actual.columna:
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1
                else:
                    if contador==0:
                        #print("este es info del nodo actual")
                        #print(actual.estado, actual.fila, actual.columna)
                        #print(actual.siguiente.estado)
                        #print(actual.anterior.estado)
                        if actual.siguiente.estado== "1":
                            numcontagiado+=1
                        if actual.anterior.estado=="1":
                            numcontagiado+=1
                        contador=1
                    if int(nodoTemporal.fila) == int(actual.fila)-1 and nodoTemporal.columna== actual.columna:
                        #print("este es info de la finla anterior")
                        #print(nodoTemporal.estado, nodoTemporal.fila, nodoTemporal.columna)
                        #print(nodoTemporal.siguiente.estado, nodoTemporal.siguiente.fila, nodoTemporal.siguiente.columna)
                        #print(nodoTemporal.anterior.estado, nodoTemporal.anterior.fila, nodoTemporal.anterior.columna)
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.anterior.estado =="1" :
                            numcontagiado+=1     
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1   
                    if int(nodoTemporal.fila) == int(actual.fila)+1 and nodoTemporal.columna== actual.columna:
                        #print("este es info de la fila siguiente")
                       # print(nodoTemporal.estado, nodoTemporal.fila, nodoTemporal.columna)
                        #print(nodoTemporal.siguiente.estado, nodoTemporal.siguiente.fila, nodoTemporal.siguiente.columna)
                        #print(nodoTemporal.anterior.estado, nodoTemporal.anterior.fila, nodoTemporal.anterior.columna)
                        if nodoTemporal.estado== "1":
                            numcontagiado+=1
                        if nodoTemporal.anterior.estado =="1":
                            numcontagiado+=1
                        if nodoTemporal.siguiente.estado =="1":
                            numcontagiado+=1

                nodoTemporal=nodoTemporal.siguiente
                
            # validacion para contagios
            if (numcontagiado == 2 or numcontagiado==3) and actual.estado=="1":
                cadena=cadena+"1"
            elif numcontagiado==3 and actual.estado=="0":
                cadena=cadena+"1"
            else:
                cadena=cadena+"0"

            actual = actual.siguiente

        # retorna el nuevo patron
        return cadena
     
    def graficarLista(self, columnas, nuNodos, cont):
        if cont==0:
            dot = Digraph('G', filename='Inicial.dot', engine='dot', format='svg')
        else:
            dot = Digraph('G', filename= f'Periodo{cont}.dot', engine='dot', format='svg')
        dot.attr(rankdir = "TB")
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'
        dot.node_attr['style'] = 'filled'

        nodoTemporal = Node("",0,0)
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
        print("¡GRAFICA COMPLETADA!")
        dot.view()

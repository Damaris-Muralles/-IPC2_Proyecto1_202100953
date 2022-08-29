
class Nodo:
    # clase nodo
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior


class ListaEnlazada:
    # inicializacion
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    # funcion para insertar nuevo dato
    def insertar(self, dato):
        nuevonodo = Nodo(dato)
        # se incertan los datos, si no hay dato se  incerta en el primer nodo, en caso contrario se incerta al final
        if self.cabeza is None:
            self.cabeza = nuevonodo
            self.cola = self.cabeza
        else:
            nuevonodo.anterior = self.cola
            self.cola.siguiente = nuevonodo
            self.cola = nuevonodo
        # contador para el tamaño de la estructura
        self.contador += 1
    # funcion para mostrar en pantalla los datos optenidos
    def imprimir(self):
        actual = self.cabeza

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    # funcion para buscar un dato entre los nodos existentes, por el momento retorna true false(falta ver si sera necesario)
    def buscar(self, dato):
        i=-1
        for d in self.imprimir():
            i=i+1
            if dato == d:
                return True
        
        return False
    # funcion para eliminar
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False
        
        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        
        if eliminado:
            self.contador -= 1
    # funcion para vaciar
    def borrar(self):
        for i in range(self.contador-1):
            #creamos un nodo temporal
            nodoTemporal = Nodo("")

            #el temporal empieza en la cabeza
            nodoTemporal = self.cabeza

            #Mientras que el temporal no sea nulo
            while nodoTemporal != None:
            
            #validamos si ese nodo es el que busco
                if nodoTemporal.dato != None:

                    #Si ese nodo es la cabeza
                    if nodoTemporal == self.cabeza:
                        print("Borrando dato en la cabeza")
                        self.cabeza = self.cabeza.siguiente
                        nodoTemporal.siguiente = None
                        self.cabeza.anterior = None


                nodoTemporal = nodoTemporal.siguiente
        nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.cabeza

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:
        
        #validamos si ese nodo es el que busco
            if nodoTemporal.dato != None:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.cabeza:
                    print("Borrando dato en la cabeza")
                    self.cabeza = self.cabeza.siguiente
                    nodoTemporal.siguiente = None


            nodoTemporal = nodoTemporal.siguiente   
        self.contador=0

    # funcion para obtener datos de acuerdo a un indice, tipo lista
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza

            for _ in range(indice):
                actual = actual.siguiente
            
            return actual.dato
        else:
            raise Exception('Índice no válido, está por fuera del rango.')
    #funcion para asignar datos de acuerdo a un indice, tipo lista
    def __setitem__(self, indice, dato):
        if indice >= 0 and indice < self.contador:
            actual = self.cabeza

            for _ in range(indice):
                actual = actual.siguiente
            
            actual.dato = dato
        else:
            raise Exception('Índice no válido, está por fuera del rango.')
    
    



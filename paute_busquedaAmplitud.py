from queue import Queue 

#Se define la clase Grafo 
class Grafo:
    #Constructor
    def __init__(self,numero_nodos,dirigido=True):
        '''
        Constructor de la clase Grafo
            Parámetros:
            numero_nodos (int): Número de nodos del grafo
            dirigido (boolean): Si el grafo es dirigido o no
        '''
        #Numero de nodos
        self.m_numero_nodos = numero_nodos
        #Lista de nodos del grafo 
        self.m_nodos = range(self.m_numero_nodos)

        #Dirigido o no
        self.m_dirigido = dirigido
        
        #Se crea un diccionario para implementar la lista de adyacencia
        #Inicializa la lista de adyacencia con una lista de conjuntos vacia
        self.m_lista_adyacencia = {}
        #Recorre la lista de nodos
        for nodo in self.m_nodos: 
            self.m_lista_adyacencia[nodo] = set()
    
    def agregar_arista(self,nodo1,nodo2,peso=1):  
        '''
        Función que permite agregar una arista al grafo.
            Parámetros:
            nodo1 (int): Nodo de inicio
            nodo2 (int): Nodo de fin
            peso (int): Peso de la arista
        ''' 
        #Agrega la arista al nodo 1 del grafo
        self.m_lista_adyacencia[nodo1].add((nodo2,peso)) 

        #Si el grafo es no dirigido, se agrega la arista al otro nodo
        if not self.m_dirigido:
            #Agrega la arista al otro nodo
            self.m_lista_adyacencia[nodo2].add((nodo1,peso))  

    def imprmir_lista_adyacencia(self): 
        '''
        Funcion que imprime la lista de adyacencia en forma de matriz de adyacencia
        '''
        #Recorre la lista de adyacencia
        for clave in self.m_lista_adyacencia.keys(): 
            #Imprime el nodo y la lista de adyacencia de cada nodo en forma de matriz 
            print("Nodo",clave, ": ", self.m_lista_adyacencia[clave]) 

    def recorrido_bfs(self,nodo_inicial): 
        '''
        Función que permite recorrer el grafo en amplitud
            Parámetros:
            nodo_inicial (int): Nodo inicial del recorrido
        '''
        #Inicializar una lista para los nodos visitados
        nodos_visitados = set()
        #Inicializar cola
        cola = Queue()
        #Agrega el nodo inicial a la cola
        cola.put(nodo_inicial)
        #Agrega el nodo inicial a la lista de visitados
        nodos_visitados.add(nodo_inicial)

        #Mientras la cola no este vacia
        while not cola.empty():
            #Sacar el primer elemento de la cola
            nodo_actual = cola.get()
            #Imprime el nodo actual
            print(nodo_actual, end=" ") 

            #Recorre la lista de adyacencia del nodo actual
            for (nodo_siguiente, peso) in self.m_lista_adyacencia[nodo_actual]:
                #Si el nodo siguiente no ha sido visitado
                if nodo_siguiente not in nodos_visitados:
                    #Agregar el nodo siguiente a la cola
                    cola.put(nodo_siguiente) 
                    #Agregar el nodo siguiente a la lista de visitados 
                    nodos_visitados.add(nodo_siguiente)

if __name__ == '__main__':
    
    #Se crea o instancia el grafo con 5 nodos y no dirigido
    print("***** Grafo no dirigido *****")
    grafo = Grafo(5, False)  
    print("Agregando aristas al grafo")
    
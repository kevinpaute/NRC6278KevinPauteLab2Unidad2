#Se importa la clase queue de python
from queue import Queue 

#Se define la clase Grafo 
class Grafo:
    '''
    Clase que permite representar un grafo con listas de adyacencia

        Atributos:
            m_numero_de_nodos (int): Número de nodos del grafo
            m_nodos (list): Lista de nodos del grafo
            m_dirigido (boolean): Si el grafo es dirigido o no
            m_lista_adyacencia (dict): Diccionario que representa la lista de adyacencia

        Metodos:
            agregar_arista(self,nodo1,nodo2,peso=1): Agrega una arista al grafo
            imprimir_lista_adyacencia(self): Imprime la lista de adyacencia en forma de matriz
            recorrido_bfs(self,nodo_inicial): Recorre el grafo en amplitud 
    '''
  
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
        Método que permite agregar una arista al grafo 
            Parámetros:
                nodo1 (int): Nodo de inicio
                nodo2 (int): Nodo de fin
                peso (int): Peso de la arista
        ''' 
        #Agrega la arista al nodo 1 del grafo al nodo 2
        self.m_lista_adyacencia[nodo1].add((nodo2,peso)) 

        #Si el grafo es no dirigido, se agrega la arista al otro nodo
        if not self.m_dirigido:
            #Agrega la arista al nodo 2 del grafo al nodo 1
            self.m_lista_adyacencia[nodo2].add((nodo1,peso))  

    def imprimir_lista_adyacencia(self): 
        '''Método que imprime la lista de adyacencia en forma de matriz de adyacencia'''
        #Recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys(): 
            #Imprime el nodo y la lista de adyacencia de cada nodo en forma de matriz 
            print("Nodo",llave, ": ", self.m_lista_adyacencia[llave]) 

    def recorrido_bfs(self,nodo_inicial): 
        '''
        Método que permite recorrer el grafo en amplitud 
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
    '''
    Método principal

        Se crea un grafo con 5 nodos
        Se agregan las aristas del grafo
        Se imprime la lista de adyacencia
        Se recorre el grafo en amplitud
    '''   
    
    #PRUEBA 1
    print("***** Grafo 1 *****")
    #Se crea o instancia el grafo con 6 nodos y no dirigido
    grafo = Grafo(6, False)  
    print("Agregando aristas al grafo")
    #Agregar las aristas
    #Agrega la arista (1,0) con peso 1 
    grafo.agregar_arista(1,0)
    #Agrega la arista (0,2) con peso 1 
    grafo.agregar_arista(0,2)
    #Agrega la arista (4,1) con peso 1
    grafo.agregar_arista(4,1)
    #Agrega la arista (4,3) con peso 1 
    grafo.agregar_arista(4,3) 
    #Agrega la arista (3,4) con peso 1
    grafo.agregar_arista(3,5)
    #Agrega la arista (5,2) con peso 1 
    grafo.agregar_arista(5,2)
    #Imprimir la lista de adyacencia 
    print("\nLista de adyacencia")
    grafo.imprimir_lista_adyacencia()
    #Imprime el recorrido en amplitud
    print("\nRecorrido primero en anchura o amplitud")
    #Recorrido a partir del vertice 0
    grafo.recorrido_bfs(0)

    #PRUEBA 2
    print("\n\n***** Grafo 2 *****")
    #Se crea o instancia el grafo con 6 nodos y no dirigido
    grafo = Grafo(6, False)  
    print("Agregando aristas al grafo")
    #Agregar las aristas
    #Agrega la arista (0,1) con peso 1
    grafo.agregar_arista(0,1)
    #Agrega la arista (0,3) con peso 1 
    grafo.agregar_arista(0,3)
    #Agrega la arista (1,2) con peso 1 
    grafo.agregar_arista(1,2)
    #Agrega la arista (3,2) con peso 1 
    grafo.agregar_arista(3,2) 
    #Agrega la arista (3,4) con peso 1
    grafo.agregar_arista(3,4)
    #Agrega la arista (4,5) con peso 1 
    grafo.agregar_arista(4,5)
    #Imprimir la lista de adyacencia 
    print("\nLista de adyacencia")
    grafo.imprimir_lista_adyacencia()
    #Imprime el recorrido en amplitud
    print("\nRecorrido primero en anchura o amplitud")
    #Recorrido a partir del vertice 0
    grafo.recorrido_bfs(0)

    #PRUEBA 3
    print("\n\n***** Grafo 3 *****")
    #Se crea o instancia el grafo con 6 nodos y no dirigido
    grafo = Grafo(6, False)  
    print("Agregando aristas al grafo")
    #Agregar las aristas
    #Agrega la arista (0,1) con peso 3
    grafo.agregar_arista(0,1,3) 
    #Agrega la arista (1,2) con peso 2
    grafo.agregar_arista(1,2,2) 
    #Agrega la arista (3,2) con peso 4
    grafo.agregar_arista(3,2,4)
    #Agrega la arista (4,3) con peso 3  
    grafo.agregar_arista(4,3,3)  
    #Agrega la arista (4,1) con peso 4
    grafo.agregar_arista(4,1,4) 
    #Agrega la arista (5,4) con peso 2
    grafo.agregar_arista(5,4,2)
    #Imprimir la lista de adyacencia   
    print("\nLista de adyacencia")
    grafo.imprimir_lista_adyacencia()
    #Imprime el recorrido en amplitud
    print("\nRecorrido primero en anchura o amplitud")
    #Recorrido a partir del vertice 3
    grafo.recorrido_bfs(3)


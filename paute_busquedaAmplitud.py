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
        

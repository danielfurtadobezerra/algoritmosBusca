import queue
import math

class Node:
    
    id = -1
    pai = None
    x = 0
    y = 0
    custoG = 0
    custoH = 0
    
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        return (self.custoG + self.custoH) < (other.custoG + other.custoH)
    
class Grafo:
    
    matriz = []
    n = 0
    direcionado = False
    coords = []
    
    def __init__(self, n, direcionado): 
        self.n = n
        self.direcionado = direcionado
        for i in range(n):
            self.matriz.append([0]*n)
            self.coords.append((0,0))
            
    def addAresta(self, s, t, distancia):
        if not self.direcionado:
            self.matriz[t][s] = distancia
        self.matriz[s][t] = distancia
        
    def addCoordenadas(self, id, x, y):
        self.coords[id] = (x, y)
        
    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
        
    def distanciaEuclidiana(self, node1, node2):
        x1, y1 = self.coords[node1.id]
        x2, y2 = self.coords[node2.id]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def aEstrela(self, s, t):
        q = queue.PriorityQueue()
        
        node = Node(s, *self.coords[s])
        node.pai = Node(-1, *self.coords[-1])
        node.custoG = 0
        node.custoH = self.distanciaEuclidiana(node, Node(t, *self.coords[t]))
        
        q.put(node)
        
        while not q.empty():
            aux = q.get()
            
            # Teste de Objetivo           
            if aux.id == t:
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in range(self.n):                
                if self.matriz[aux.id][i] > 0 and i != aux.pai.id:
                    node = Node(i, *self.coords[i])
                    node.pai = aux
                    node.custoG = aux.custoG + self.matriz[aux.id][i]
                    node.custoH = self.distanciaEuclidiana(node, Node(t, *self.coords[t]))
                    q.put(node)
            # Expansão de vizinhos
        
        return aux

g = Grafo(10,False)

g.printMatriz()

g.addAresta(0, 2, 5)
g.addAresta(1, 3, 3)
g.addAresta(2, 3, 2)
g.addAresta(3, 5, 1)
g.addAresta(5, 4, 4)
g.addAresta(3, 6, 7)
g.addAresta(6, 9, 8)
g.addAresta(4, 7, 2)
g.addAresta(4, 8, 3)
g.addAresta(8, 9, 2)

g.printMatriz()

objetivo = g.aEstrela(0, 9, distanciaEuclidiana(0,2))
   
while objetivo.id != -1:
    print(objetivo.id)
    objetivo = objetivo.pai

import queue
import heapq

class Node:
    
    id = -1
    pai = None
    
    def __init__(self,id):
        self.id = id

class Grafo:
    
    matriz = []
    n = 0
    direcionado = False
    
    def __init__(self,n,direcionado): 
        self.n = n
        self.direcionado = direcionado
        for i in range(n):
            self.matriz.append([0]*n)            
    
    def addAresta(self,s,t,custo):
        if(not self.direcionado):
            self.matriz[t][s]=custo
        self.matriz[s][t]=custo
        
    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
    
    def cu(self,s,t):
        pq = [(0, Node(s), None)]
        visitados = set()
        
        while pq:
            (custo, node, pai) = heapq.heappop(pq)
            
            if node.id in visitados:
                continue
                
            visitados.add(node.id)
            
            node.pai = pai
            
            if node.id == t:
                return node
            
            for i in range(self.n):
                if self.matriz[node.id][i] != 0 and i not in visitados:
                    filho = Node(i)
                    heapq.heappush(pq, (custo + self.matriz[node.id][i], filho, node))
        
        return Node(-1)
        

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

objetivo = g.cu(0, 9)

while objetivo.id != -1:
    print(objetivo.id)
    objetivo = objetivo.pai

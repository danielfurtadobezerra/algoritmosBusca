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
    
    def addAresta(self,s,t):
        if(not self.direcionado):
            self.matriz[t][s]=1
        self.matriz[s][t]=1
        
    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
    
    def dfs(self, s, t):
        visited = set()
        stack = []
        stack.append(Node(s))
        
        while stack:
            node = stack.pop()
            
            if node.id == t:
                return node
            
            if node.id not in visited:
                visited.add(node.id)
                
                for i in range(self.n):
                    if self.matriz[node.id][i] == 1 and i not in visited:
                        child = Node(i)
                        child.pai = node
                        stack.append(child)
        return None

g = Grafo(10,False)

g.printMatriz()

g.addAresta(0, 2)
g.addAresta(1, 3)
g.addAresta(2, 3)
g.addAresta(3, 5)
g.addAresta(5, 4)
g.addAresta(3, 6)
g.addAresta(6, 9)
g.addAresta(4, 7)
g.addAresta(4, 8)
g.addAresta(8, 9)

g.printMatriz()

objetivo = g.dfs(0, 9)

if objetivo:
    while objetivo.id != -1:
        print(objetivo.id)
        objetivo = objetivo.pai
else:
    print("Caminho não encontrado!")

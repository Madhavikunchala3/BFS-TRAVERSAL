from collections import defaultdict as dd   
class Graph:   
    def __init__(self):
        self.graph = dd(list)
    def addEdgetoGraph(self, x, y):
        self.graph[x].append(y)
    def BFSearch(self, n):
        visited_vertices = ( len(self.graph ))*[False]
        queue = []
        visited_vertices[n] = True
        queue.append(n)
        while queue:
            n = queue.pop(0)
            print (n, end = " ")
            for v in self.graph[ n ]:
                if visited_vertices[v] == False:
                    queue.append(v)
                    visited_vertices[v] = True
                    graph = Graph()
n=int(input("Enter no.of edges: "))
for i in range(0,n):
    v1=int(input("Enter v1 value: "))
    v2=int(input("Enter v2 value: "))
Graph.addEdgetoGraph(v1, v2)
initial=int(input("Enter initial vertex: "))
print ( " The Breadth First Search Traversal for The Graph is as Follows: " )   
      

     

     


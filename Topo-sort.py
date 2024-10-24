class Graph:
    #adjacency list
    def __init__(self):
        self.graph={}
        self.directed = False

    def addVertex(self,vertex):
        #if vertex is not already present, initialise it with no edge
        if vertex not in self.graph:
            self.graph[vertex] = []
    def addEdge(self, src , dest):
        #add source and destination vertex to graph
        self.addVertex(src)
        self.addVertex(dest)

        #add the destination vertex to lost with edge of source
        self.graph[src].append(dest)
    #undirected
        if not self.directed:
            self.graph[dest].append(src)
    def displayGraph(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")
    st1=[]
    def topo(self,vertex,visited):
        st1.append(vertex)
        if vertex not in visited:
            
            for v in self.graph[vertex]:
                visited.append(vertex)
                self.topo(v,visited)
        print(visited)
G=Graph()
G.directed=True
G.addEdge("a","b")
G.addEdge("a","c")
G.addEdge("b","d")
G.addEdge("c","d")
G.addEdge("d","e")
G.addEdge("c","f")
G.addEdge("f","g")
G.addEdge("g","d")
G.displayGraph()
G.topo("a",[])

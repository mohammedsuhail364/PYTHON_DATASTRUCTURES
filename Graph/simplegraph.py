class Graph:
    def __init__(self):
        self.graph={}
        self.li=[]
        self.visited=set()
        self.queue=[]
    def addvertexes(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2,isdirected=False):
        self.addvertexes(vertex1)
        self.addvertexes(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isdirected:
            self.graph[vertex2].append(vertex1)
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}=>{value}")
    def getvertices(self):
        for i in self.graph:
            print('vertices =>',i)
    def getedges(self):
        for key,values in self.graph.items():
            for i in values:
                print(f"({key},{i})")
    def removevertices(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key,values in self.graph.items():
                if vertex in values:
                    values.remove(vertex)
    def isedge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]
    def removeedges(self,vertex1,vertex2):
        if self.isedge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
    def matrix(self):
        c=0
        li=[]
        for key,value in self.graph.items():
            c+=1
            li.append(key)
        li1=li.copy()
        li1.sort()
        for x in range(c):
            self.li.append([])
            for row in range(c):
                if li1[row] in self.graph[li[x]]:
                    self.li[x].append(1)
                else:
                    self.li[x].append(0)
        for x in self.li:
            print(x)
    def dfs(self,start,isvisited = set()):
        if start not in isvisited:
            isvisited.add(start)
            print(start,end=' ')
            for child in self.graph[start]:
                self.dfs(child)
    def bfs(self,start):
        isvisited={start}
        queue=[start]
        while len(queue)>0:
            current=queue.pop(0)
            print(current,end=' ')
            for child in self.graph[current]:
                if child not in isvisited:
                    queue.append(child)
                    isvisited.add(child)

graph1=Graph()
graph1.addedges('A',"B")
graph1.addedges('B',"C")
graph1.addedges('B',"D")
graph1.addedges('C',"D")
graph1.display()
# print("------------------------------")
# # graph1.getvertices()
# # graph1.getedges()
# graph1.removevertices('C')
# graph1.display()
# print("------------------------------")
# graph1.removeedges('A',"B")
# graph1.display()
# print("------------------------------")
# graph1.matrix()
graph1.dfs('A')
print()
graph1.bfs('A')


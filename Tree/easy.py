# a=[5,4,2]
# b=[1,0,0]
# a2=list(map(str,a))
# b2=list(map(str,b))
# a1=''.join(a2)
# b1=''.join(b2)
# print(a1)
# print(b1)
# sum1=int(a1)
# sum2=int(b1)
# sum3=sum1+sum2
# print(sum3)
# sum4=list(str(sum3))
# sum5=list(map(int,sum4))
# print(sum5)
class graph:
    def __init__(self) -> None:
        self.graph={}
        self.visited=set()
        self.queue=[]
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2):
        self.addvertex(vertex1)
        self.addvertex(vertex2)
        self.graph[vertex1].append(vertex2)
        # self.graph[vertex2].append(vertex1)
    def check(self,start):
        self.visited={start}
        self.queue=[start]
        while len(self.queue)>0:
            current=self.queue.pop(0)
            print(current,end=' ')
            for child in self.graph[current]:
                if child not in self.visited:
                    self.visited.add(child)
                    self.queue.append(child)

        
g=graph()
g.addedges(0,1)
g.addedges(1,2)
g.addedges(2,3)
g.addedges(3,0)
g.check(0)
# print(g.graph)

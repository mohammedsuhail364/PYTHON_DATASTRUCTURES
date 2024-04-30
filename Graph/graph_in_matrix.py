# class Graph:
#     def __init__(self, num_vertices):
#         self.num_vertices = num_vertices
#         self.graph = [[0] * num_vertices for _ in range(num_vertices)]
#     def add_edge(self, u, v):
#         self.graph[u][v] = 1
#         self.graph[v][u] = 1  
#     def print_graph(self):
#         for row in self.graph:
#             print(" ".join(map(str, row)))
# num_vertices = 4
# g = Graph(num_vertices)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.print_graph()
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.num_vertices = len(vertices)
        self.graph = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Vertices not found in the graph")
        u_index = self.vertices.index(u)
        v_index = self.vertices.index(v)
        self.graph[u_index][v_index] = 1
        self.graph[v_index][u_index] = 1  # If the graph is undirected

    def print_graph(self):
        header = "  " + " ".join(self.vertices)
        print(header)
        for i, row in enumerate(self.graph):
            row_str = self.vertices[i] + " " + " ".join(map(str, row))
            print(row_str)

# Example usage:
vertices = ['A', 'B', 'C', 'D']
g = Graph(vertices)
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.print_graph()

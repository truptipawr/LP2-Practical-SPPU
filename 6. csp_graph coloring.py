class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, color, c):
        for neighbor in self.graph[v]:
            if color[neighbor] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c

                if self.graph_coloring_util(m, color, v + 1):
                    return True

                color[v] = 0  # Backtrack

        return False

    def branch_and_bound(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            return False, []
        return True, color

# Function to solve the graph coloring problem
def graph_coloring(vertices, edges, m):
    graph = Graph(vertices)
    
    # Adding edges to the graph
    for u, v in edges:
        graph.add_edge(u, v)

    result, color = graph.branch_and_bound(m)

    if result:
        print("Solution found: ")
        for i in range(vertices):
            print(f"Vertex {i}: Color {color[i]}")
    else:
        print(f"No solution exists with {m} colors.")

# Example usage
vertices = 4  # Number of vertices
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]  # Edges of the graph
m = 3  # Number of colors

graph_coloring(vertices, edges, m)

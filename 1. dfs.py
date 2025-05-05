# Depth First Search (DFS) for an undirected graph

class Graph:
    def __init__(self):
        self.graph = {}

    # Add an edge to the undirected graph
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    # Recursive DFS traversal from a given start vertex
    def dfs(self, vertex, visited, traversal):
        visited.add(vertex)
        traversal.append(vertex)
        for neighbor in sorted(self.graph[vertex]):  # Sort for consistent output
            if neighbor not in visited:
                self.dfs(neighbor, visited, traversal)

    # DFS for all components in the graph
    def dfs_all(self):
        visited = set()
        component_number = 1
        for vertex in sorted(self.graph):
            if vertex not in visited:
                traversal = []
                self.dfs(vertex, visited, traversal)
                print(f"Component {component_number}: {' -> '.join(map(str, traversal))}")
                component_number += 1


# Example usage
if __name__ == "__main__":
    g = Graph()

    # Building a sample undirected graph
    # Component 1
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('E', 'F')
    
    # Component 2
    #g.add_edge('X', 'Y')
    #g.add_edge('Y', 'Z')

    print("📌 Depth First Search (DFS) Traversal of the Graph:\n")
    g.dfs_all()

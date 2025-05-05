from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # Add an edge to the undirected graph
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    # BFS traversal from a given start vertex
    def bfs(self, start, visited, traversal):
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            traversal.append(vertex)

            for neighbor in sorted(self.graph[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Perform BFS for all components
    def bfs_all(self):
        visited = set()
        component_number = 1
        for vertex in sorted(self.graph):
            if vertex not in visited:
                traversal = []
                self.bfs(vertex, visited, traversal)
                print(f"Component {component_number}: {' -> '.join(traversal)}")
                component_number += 1

# Example usage
if __name__ == "__main__":
    g = Graph()

    # Component 1
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('E', 'F')

    print("📌 Breadth First Search (BFS) Traversal of the Graph:\n")
    g.bfs_all()

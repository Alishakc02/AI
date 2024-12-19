from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, startVertex, searchVertex):
        visited = [False] * self.V
        queue = deque()
        queue.append(startVertex)
        visited[startVertex] = True

        while queue:
            currentVertex = queue.popleft()
            print(currentVertex, end=' ')

            if currentVertex == searchVertex:
                return True

            for v in self.adj[currentVertex]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    
        return False

def adj_matrix():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    G = Graph(V)
    
    for _ in range(E):
        src, dest = map(int, input("Enter the source and destination of edge: ").split())
        G.add_edge(src, dest)
        
    return G

if __name__ == "__main__":
    G = adj_matrix()
    startVertex = int(input("Enter the starting vertex for BFS: "))
    searchVertex = int(input("Enter the vertex to search for: "))
    
    print("BFS traversal:")
    if G.bfs(startVertex, searchVertex):
        print(f"\nKey {searchVertex} found!")
    else:
        print(f"\nKey {searchVertex} not found!")

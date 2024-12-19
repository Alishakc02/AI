class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs_util(self, v, visited, searchVertex, found):
        visited[v] = True
        print(v, end=' ')
        
        if v == searchVertex:
            found[0] = True
            return
        
        for i in self.adj[v]:
            if not visited[i]:
                self.dfs_util(i, visited, searchVertex, found)
                if found[0]:  # Stop further recursion if the search vertex is found
                    return

    def dfs(self, startVertex, searchVertex):
        visited = [False] * self.V
        found = [False]
        self.dfs_util(startVertex, visited, searchVertex, found)
        return found[0]

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
    startVertex = int(input("Enter the starting vertex for DFS: "))
    searchVertex = int(input("Enter the vertex to search for: "))
    
    print("DFS traversal:")
    if G.dfs(startVertex, searchVertex):
        print(f"\nKey {searchVertex} found!")
    else:
        print(f"\nKey {searchVertex} not found!")

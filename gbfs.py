from queue import PriorityQueue

class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

def create_node(vertex):
    return Node(vertex)

def add_edge(graph, src, dest):
    new_node = create_node(dest)
    new_node.next = graph[src]
    graph[src] = new_node

def gbfs(graph, heuristic, start_node, goal_node):
    visited = [False] * len(graph)
    pq = PriorityQueue()
    pq.put((heuristic[start_node], start_node))
    visited[start_node] = True
    
    print("GBFS Path:", start_node, end=" ")

    while not pq.empty():
        current_node = pq.get()[1]

        if current_node == goal_node:
            print("->", goal_node)
            return

        best_child = -1
        best_heuristic = float('inf')

        current_neighbor = graph[current_node]
        while current_neighbor is not None:
            neighbor = current_neighbor.vertex

            if not visited[neighbor]:
                visited[neighbor] = True
                pq.put((heuristic[neighbor], neighbor))

                if heuristic[neighbor] < best_heuristic:
                    best_child = neighbor
                    best_heuristic = heuristic[neighbor]

            current_neighbor = current_neighbor.next

        if best_child != -1:
            print("->", best_child, end=" ")

    print("\nNo path found.")

def main():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = [None] * num_nodes

    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (source destination):")
    for _ in range(num_edges):
        src, dest = map(int, input().split())
        add_edge(graph, src, dest)

    print("Enter the heuristic values for each node separated by spaces:")
    heuristic_input = input().split()
    heuristic = [int(value) for value in heuristic_input]

    start_node = int(input("Enter the starting node: "))
    goal_node = int(input("Enter the goal node: "))

    gbfs(graph, heuristic, start_node, goal_node)

if __name__ == "__main__":
    main()

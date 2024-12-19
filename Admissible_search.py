import heapq

MAX_NODES = 10
INF = 9999

class Node:
    def __init__(self, node, cost, heuristic):
        self.node = node
        self.cost = cost
        self.heuristic = heuristic

def find_min_cost(frontier):
    min_cost = INF
    min_index = -1
    for i, (current_cost, _) in enumerate(frontier):
        if current_cost < min_cost:
            min_cost = current_cost
            min_index = i
    return min_index

def a_star_search(start, goal):
    frontier = [(0, start)]
    visited = [False] * MAX_NODES
    parent = [-1] * MAX_NODES

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node != -1:
                path.append(current_node)
                current_node = parent[current_node]
            print("Path:", ' -> '.join(map(str, path[::-1])))
            return

        for next_node in range(MAX_NODES):
            cost = graph[current_node][next_node]
            if cost != INF and not visited[next_node]:
                new_cost = current_cost + cost
                priority = new_cost + heuristic[next_node]
                heapq.heappush(frontier, (priority, next_node))
                parent[next_node] = current_node
                visited[next_node] = True

    print("No path found.")

def initialize_graph():
    global graph, heuristic
    graph = [[INF] * MAX_NODES for _ in range(MAX_NODES)]
    heuristic = [INF] * MAX_NODES

def add_edge(source, destination, cost):
    graph[source][destination] = cost

def set_heuristic(node, value):
    heuristic[node] = value

def main():
    initialize_graph()
    
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter the edges in the format: source destination cost")
    for _ in range(num_edges):
        source, destination, cost = map(int, input().split())
        add_edge(source, destination, cost)

    print("Enter the heuristic values for each node:")
    for i in range(num_nodes):
        value = int(input(f"Node {i}: "))
        set_heuristic(i, value)

    start_node = int(input("Enter the start node: "))
    goal_node = int(input("Enter the goal node: "))

    print("\nA* Search:")
    print("Start Node:", start_node)
    print("Goal Node:", goal_node)
    a_star_search(start_node, goal_node)

if __name__ == "__main__":
    main()

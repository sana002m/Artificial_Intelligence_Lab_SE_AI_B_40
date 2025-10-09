import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # cost from start to node
        self.h = h  # heuristic (estimated cost to goal)
        self.f = g + h  # total cost

    def __lt__(self, other):  # for priority queue
        return self.f < other.f

def astar_search(graph, heuristics, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]  # reverse path

        closed_set.add(current.name)

        for neighbor, cost in graph[current.name].items():
            if neighbor in closed_set:
                continue

            g = current.g + cost
            h = heuristics[neighbor]
            neighbor_node = Node(neighbor, current, g, h)

            # check if a better path exists
            if any(open_node.name == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None

# Example Graph (with distances)
graph = {
    'HOME': {'BANK': 45, 'GARDEN': 40, 'SCHOOL': 50},
    'BANK': {'HOME': 45, 'POLICE STATION': 60},
    'GARDEN': {'HOME': 40, 'RAILWAY STATION': 72},
    'SCHOOL': {'HOME': 50, 'POST OFFICE': 59, 'RAILWAY STATION': 75},
    'RAILWAY STATION': {'SCHOOL': 75, 'GARDEN':72, 'UNIVERSITY':40},
    'POST OFFICE': {'SCHOOL': 59},
    'POLICE STATION': {'BANK': 60, 'UNIVERSITY': 28},
    'UNIVERSITY': {'POLICE STATION': 28, 'RAILWAY STATION': 40},
}

# Heuristic values (straight-line estimates to goal 'UNIVERSITY')
heuristics = {
    'HOME': 120,
    'BANK': 80,
    'GARDEN': 100,
    'SCHOOL': 70,
    'RAILWAY STATION': 20,
    'POST OFFICE': 110,
    'POLICE STATION': 26,
    'UNIVERSITY':0
}

# Run A* Search
start, goal = 'HOME', 'UNIVERSITY'
path = astar_search(graph, heuristics, start, goal)
print(f"Shortest path from {start} to {goal}: {path}")

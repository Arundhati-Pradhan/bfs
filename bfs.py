from queue import Queue

adjacent_list = {
    'A' :['B','C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
        
print(adjacent_list)   

visited = {}
level = {}
parent = {}
bfs_traversal = []
queue = Queue()

for node in adjacent_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

source_node = input("Enter source node: ")
visited[source_node] = True
level[source_node] = 0
queue.put(source_node)

while not queue.empty():
    pop_node = queue.get()
    bfs_traversal.append(pop_node)

    for next_node in adjacent_list[pop_node]:
        if not visited[next_node]:
            visited[next_node] = True
            parent[next_node] = pop_node
            level[next_node] = level[pop_node] + 1
            queue.put(next_node)

print(bfs_traversal)


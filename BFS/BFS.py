#реализация поиска в ширину
graph = {'A': ['B', 'C', 'E', 'H'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D',],
         'F': ['C','J'],
         'G': ['C'],
         'H': ['A','I','J'],
         'I': ['H','J'],
         'J': ['H','I','F']}

# находит кратчайший путь между двумя узлами графа, используя BFS
def bfs_short(graph, first, last):
    explored = []
    queue = [[first]]
 
    if first == last:
        return "Ты что троль :/"
 
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == last:
                    return new_path
 
            explored.append(node)
 
    #если нет пути между двумя узлами
    return "Нет пути между данными узлами"
 
print(bfs_short(graph, 'E', 'F') )
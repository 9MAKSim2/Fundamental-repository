Grapf = [[0,1], [0,2], [0,3], [2,3], [4,5], [1, 6], [6, 7]]

def search_connection(start, end, graph):
    nodes = sorted(list(set(node for edge in graph for node in edge))) # Получаем все узлы
    num_nodes = len(nodes)
    dist_matrix = [[0]*num_nodes for _ in range(num_nodes)] # Матрица расстояний (заполняем нулями)
    for i in range(num_nodes): # Заполняем диагональ единичками
        dist_matrix[i][i] = 1
    
    def bfs(start_node): # обход в ширину
        start = nodes.index(start_node) # получаем индекс стартового узла
        visited = {start_node: 1}  # Словарь посещённых узлов (узел: расстояние)
        inter = [start_node]     
        while inter:
            current = inter.pop(0)
            current_dist = visited[current]
            for neighbor in nodes:
                if [current, neighbor] in graph or [neighbor, current] in graph:
                    if neighbor not in visited:
                        visited[neighbor] = current_dist + 1
                        inter.append(neighbor)
        
        # Заполняем строку матрицы
        for node, dist in visited.items():
            col = nodes.index(node)
            dist_matrix[start][col] = dist
    
    # Выполняем BFS для каждого узла
    for node in nodes:
        bfs(node)
    
    return dist_matrix

# Вывод результатов
result = search_connection(1, 2, Grapf)
nodes = sorted(list(set(node for edge in Grapf for node in edge)))

for i in result:
    print(*i)
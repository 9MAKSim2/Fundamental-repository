import random

Grapf = [[0,1], [0,2], [0,3], [2,3], [4,5], [1, 6], [6, 7]]

def count_nodes(graph):
    amount_of_nodes = list(set([i for l in graph for i in l]))
    return amount_of_nodes, len(amount_of_nodes) 

def weight_of_nodes():
    points = count_nodes(Grapf)[0]
    weights_unsorted = []
    for x in points:
        weights_unsorted.append(random.randrange(1,20))
    weights = sorted(weights_unsorted)
    totally = list(zip(points, weights))
    return totally

def binary_search(graph, mission):
    left, right = 0, len(graph) - 1
    while left <= right:
        mid = (left + right) // 2
        if graph[mid][1] == mission:
            return graph[mid][0]
        elif graph[mid][1] < mission:
            left = mid+1
        else:
            right = mid - 1
    return -1,
correct_list = weight_of_nodes()

print(correct_list)
print(binary_search(correct_list, 12))
        


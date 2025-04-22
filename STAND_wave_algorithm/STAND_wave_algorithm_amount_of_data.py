import timeit
import random as rd
from voln import wave_algorithm, get_vertices

NUM_OF_EDGES = [100, 1000, 10000, 100000]

def random_node(vertices):
    initial_node = rd.choice(vertices)
    end_node = rd.choice(vertices)
    while initial_node == end_node:
        end_node = rd.choice(vertices)
    return initial_node, end_node

def add_random_edge(num_of_edges, edges): # функция создания случайного ребра
    initial_node = rd.randint(0, num_of_edges * 2)
    connected_node = rd.randint(0, num_of_edges * 2)
    while initial_node == connected_node:
        connected_node = rd.randint(0, num_of_edges * 2)
    if (initial_node, connected_node) in edges or (connected_node, initial_node) in edges:
        add_random_edge(num_of_edges, edges)
    else:
        edges.append((initial_node, connected_node))

def create_grapf(num_of_edges): # функция создания графа из случайных ребер
    random_graph = []
    for i in range(num_of_edges):
        add_random_edge(num_of_edges, random_graph)
    return random_graph

def start_test(num_of_edges): # тест алгоритма с линейным увеличением входных данных
    graph  = create_grapf(num_of_edges)
    nodes = random_node(get_vertices(graph))
    start = timeit.default_timer()
    wave_algorithm(graph, nodes[0], nodes[1])
    time = float(timeit.default_timer() - start)
    return ("%.10f" % time).rstrip('0')

for i in NUM_OF_EDGES:
    print(f'Количество ребер: {i} | Время: {start_test(i)}')
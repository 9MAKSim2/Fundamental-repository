from voln import wave_algorithm
import timeit

def test_multiple_edges():
    """Тест с несколькими ребрами и общими вершинами."""
    edges = [(1, 2), (2, 3), (3, 4), (2, 5)]
    start = timeit.default_timer()
    wave_algorithm(edges, 0, 1)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_multiple_edges())
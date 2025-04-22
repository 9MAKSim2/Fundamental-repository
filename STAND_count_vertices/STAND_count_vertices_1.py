from voln import count_vertices
import timeit

def test_single_edge():
    """Тест с одним ребром."""
    edges = [(1, 2)]
    start = timeit.default_timer()
    count_vertices(edges)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_single_edge())
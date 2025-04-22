from voln import get_vertices
import timeit

def test_string_vertices():
    """Тест со строковыми вершинами."""
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    start = timeit.default_timer()
    get_vertices(edges)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_string_vertices())
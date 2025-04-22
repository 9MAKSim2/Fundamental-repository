from voln import wave_algorithm
import timeit

def test_string_vertices():
    """Тест со строковыми вершинами."""
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    start = timeit.default_timer()
    wave_algorithm(edges, 'A', 'C')
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_string_vertices())
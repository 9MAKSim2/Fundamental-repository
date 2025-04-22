from voln import wave_algorithm
import timeit

def test_single_edge():
    """Тест с одним ребром."""
    edges = [(1, 2)]
    start = timeit.default_timer()
    wave_algorithm(edges, 0, 1)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_single_edge())
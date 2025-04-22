from voln import wave_algorithm
import timeit

def test_empty_input():
    edges = []
    start = timeit.default_timer()
    wave_algorithm(edges, 1, 5)
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')

print(test_empty_input())
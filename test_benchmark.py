from searching import busqueda_lineal, busqueda_binaria

# Escenario de los 100K 
case_4 = list(range(100000))

# target que NO existe
target = 200_000


def test_benchmark_lineal(benchmark):
    benchmark.pedantic(
        busqueda_lineal,
        args=(case_4, target),
        rounds=5,
        iterations=5
    )


def test_benchmark_binaria(benchmark):
    benchmark.pedantic(
        busqueda_binaria,
        args=(case_4, target),
        rounds=5,
        iterations=5
    )
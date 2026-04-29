from searching import busqueda_lineal, busqueda_binaria

case_1 = [1, 2, 3, 4, 5, 6, 7, 8]
case_2 = list(range(32))
case_3 = list(range(128))

#  BÚSQUEDA LINEAL

def test_busqueda_lineal():
    assert busqueda_lineal(case_1, 8) == 7
    assert busqueda_lineal(case_1, 1) == 0
    assert busqueda_lineal(case_1, 4) == 3
    assert busqueda_lineal(case_1, 16) == -1
    assert busqueda_lineal([], 10) == -1


#  BÚSQUEDA BINARIA

def test_busqueda_binaria():
    assert busqueda_binaria(case_1, 8) == 7
    assert busqueda_binaria(case_1, 1) == 0
    assert busqueda_binaria(case_1, 4) == 3
    assert busqueda_binaria(case_1, 16) == -1
    assert busqueda_binaria([], 10) == -1
def calcular_volume(raio):
    if type(raio) == str or raio < 0:
        return Exception
    volume = (4/3*3.14*raio**3)
    return round(volume,2)



assert calcular_volume(1) == 4.19
assert calcular_volume(0) == 0
assert calcular_volume('gdgdgg') == Exception
assert calcular_volume('h3gt646g') == Exception
assert calcular_volume(-367) == Exception
print('okay')
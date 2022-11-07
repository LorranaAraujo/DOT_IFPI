def negativo(valor):
    if type(valor) == str :
        return Exception
    if valor < 0 :
        return True
    elif valor > 0:
        return False
    

assert negativo(10) == False
assert negativo(-90) == True
assert negativo('hxdudh') == Exception
assert negativo(-90.2) == True
assert negativo(98.5) == False
print('okay')
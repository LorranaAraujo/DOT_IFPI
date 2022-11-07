def perfeito(valor):
    if type(valor)!= int:
        return Exception
    soma = 0
    for i in range(1,valor):
        if valor %i == 0:
            soma = soma+i

    if soma==valor:
        return True
    else:
        return False
    
assert perfeito(6) == True
assert perfeito(5) == False
assert perfeito('dbhdh') == Exception
assert perfeito(26.23) == Exception
print('okay')
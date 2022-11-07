def idade_categoria(idade):
    if type(idade) != int:
        return Exception

    if  idade >=5 and idade <=7 :
        return 'INFANTIL A'
    
    elif  idade >=8 and idade <=10 :
        return 'INFANTIL B'
    
    elif  idade >=11 and idade <=13 :
        return 'JUVENIL A'
    
    elif  idade >=14 and idade <=17 :
        return 'JUVENIL B'
    
    elif idade >=18 and idade <=60:
        return 'ADULTO'
    elif idade >60:
        return 'IDOSO'
    else:
        print('nao pode ser menor que 5 anos')

assert idade_categoria(13) == 'JUVENIL A'
assert idade_categoria(12) == 'JUVENIL A'
assert idade_categoria(5) == 'INFANTIL A'
assert idade_categoria(16) == 'JUVENIL B'
assert idade_categoria(79) == 'IDOSO'

assert idade_categoria('34') == Exception
print('ok')
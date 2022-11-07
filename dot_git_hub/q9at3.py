def par(valor):
    if type(valor) != int:
        return Exception
    if valor%2 == 0:
        return True
    elif valor%2 != 0:
        return False
    
assert par(5) == False
assert par(86) == True 
assert par(91.5) == Exception
assert par('hdhdhh') == Exception
print('okay')
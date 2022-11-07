def idade_pessoa(anos,meses,dias):
    if type(anos) != int or type(meses) != int or type(dias) != int:
        return Exception
    if (anos not in range(0,121)) or (meses not in range(0,13)) or (dias not in range(0,31)):
        return Exception
    return anos*365 + meses*30 + dias


assert idade_pessoa(10,2,2) == 3712
assert idade_pessoa(17,2,9) == 6274
assert idade_pessoa('17',2,9) == Exception
assert idade_pessoa('17','17',9) == Exception
assert idade_pessoa(121,12,26) == Exception
print('ok')
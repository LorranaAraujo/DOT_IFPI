def n_primo(n):
    if type(n) != int:
        return Exception
    if n == 1:
        return False
    e_primo = True
    for i in range(2,n):
        if n % i == 0:
            e_primo = False
    return e_primo



assert n_primo(3) == True
assert n_primo(88) == False
assert n_primo(7) == True
assert n_primo(9) == False
assert n_primo(13) == True
assert n_primo(6.9) == Exception
assert n_primo('gygus') == Exception
assert n_primo(77) == False
assert n_primo(1) == False


print('todos ok')
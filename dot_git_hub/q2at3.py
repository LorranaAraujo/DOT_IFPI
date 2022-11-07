def media(n1,n2,n3,letra):
    if type(n1) == str or type(n2) == str or type(n3) == str or type(letra) != str :
        return Exception
    if letra == 'A' :
        media_a = (n1+n2+n3)/3
        return round(media_a,2)
    elif letra == 'P':
        media_p = ((n1*5)+(n2*3)+(n3*2))/3
        return round(media_p,2)
    
    return False

assert media(2,2,2,'A') == 2
assert media(2,2,2,'P') == 6.67
assert media('657',47,345,'P') == Exception
assert media(2,3,6,'l') == False
assert media(1,2,3,4) == Exception
print('okay')
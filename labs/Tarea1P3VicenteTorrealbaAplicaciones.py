def divisores_propios(n):
    l = []
    z = n
    n -= 1
    while n > 0:
        v = z/n
        if int(v) == v:
            l.append(n)
        n -= 1
    return l
def amigos(n1,n2):
    l1 = divisores_propios(n1)
    l2 = divisores_propios(n2)
    o1 = 0
    o2 = 0
    ll1 = len(l1)-1
    ll2 = len(l2)-1
    while ll1 >= 0:
        o1 += l1[ll1]
        ll1 -= 1
    while ll2 >= 0:
        o2 += l2[ll2]
        ll2 -= 1
    if ((o1 == n2) and (o2 == n1)):
        return True
    else:
        return False
n1 = int(input('Ingrese el primer numero:'))
n2 = int(input('Ingrese el segundo numero:'))
a = amigos(n1,n2)
print(a)

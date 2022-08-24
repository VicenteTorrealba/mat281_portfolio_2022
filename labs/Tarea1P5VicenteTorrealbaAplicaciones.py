def es_primo(p):
    for i in range(2,p):
        if p % i == 0:
            return False
    return True
def lista_de_primos(p):
    l = []
    for i in range(2,p):
        if es_primo(i):
            l.append(i)
    return l
def goldbash(g):
    l = lista_de_primos(g)
    ll = len(l)
    lg = []
    for i in range(0,ll):
        for j in range(i,ll):
            li = l[i]
            lj = l[j]
            if (li + lj == g):
                pg = (li,lj)
                lg.append(pg)
    return lg
g = int(input('Ingrese el numero:'))
gg = goldbash(g)
print(gg)
        

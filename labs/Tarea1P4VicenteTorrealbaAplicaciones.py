def collatz(n):
    l = [n]
    t = True
    while t:
        if (n%2) == 0:
            n /= 2
            n = int(n)
            l.append(n)
            if n == 1:
                t = False
        else:
            n = 3*n + 1
            l.append(n)
    return l
n = int(input('Ingrese el numero inicial:'))
c = collatz(n)
print(c)
        

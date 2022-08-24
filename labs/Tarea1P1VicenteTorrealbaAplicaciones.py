n = int(input('Ingrese la cantidad de sumas:'))
c = 0
while n >= 1:
    c += ((-1)**(n+1))/(2*n-1)
    n -= 1
c = 4*c
print(c)

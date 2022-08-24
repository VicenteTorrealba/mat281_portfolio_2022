def factorial(n):
    f = 1
    while n > 0:
          f *= n
          n -= 1
    return f
def calcular_e(n):
    e = 0
    while n >= 0:
        f = factorial(n)
        e += 1/f
        n -= 1
    return e

n = int(input('Ingrese Cantidad de sumas:'))
e = calcular_e(n)
print(e)

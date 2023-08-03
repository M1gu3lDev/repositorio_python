entrada = str(input("digite um numero"))
lista = []
for numero in entrada:
    numero = int(numero)
    lista.append(numero)
c = 0
soma = 0
lista.reverse()
for bin in lista:
    potencia = bin*2**c
    soma += potencia
    c += 1

print(soma)
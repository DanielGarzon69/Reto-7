def es_primo(numero):
    if numero < 2:
        return False
    i = 2
    while i <= int(numero ** 0.5):
        if numero % i == 0:
            return False
        i += 1
    return True

print("Los números primos del 1 al 100 son:")
numero = 1
while numero <= 100:
    if es_primo(numero):
        print(numero) 
    numero += 1
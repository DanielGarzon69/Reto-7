def print_divisors(n):
    print("Los divisores del número son:")
    i = 1 
    while i <= n: 
        if n % i == 0:
            print(i)
        i += 1 

numero = int(input("Ingrese un número entre 2 y 50: "))

if 2 <= numero <= 50:
    print_divisors(numero)
else:
    print("El número ingresado no está en el rango permitido (2-50).")

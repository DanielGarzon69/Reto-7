# Solicitar al usuario que ingrese un número natural n mayor que 2
n = int(input("Ingrese un número natural n ≥ 2: "))

# Verificar si n es mayor que 2
if n < 2:
    print("El número ingresado no es válido. Debe ser mayor o igual a 2.")
else:
    print(f"Números pares en forma descendente hasta 2 que son menores o iguales a {n}:")
    par = n if n % 2 == 0 else n - 1  # Comenzar desde n si es par, o desde n-1 si es impar
    while par >= 2:
        print(par)
        par -= 2
        
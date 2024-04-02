n = int(input("Ingrese un número natural para calcular su factorial: "))
def factorial(n):
    if n < 0:
        print("No se puede calcular el factorial de un número negativo.")
    elif n == 0:
        print("El factorial de 0 es 1.")
    else:
        resultado = 1
        i = 1
        while i <= n:
            resultado *= i
            i += 1
        print(f"El factorial de {n} es: {resultado}")
factorial(n)
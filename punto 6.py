def adivinar_numero():
    print("Piensa en un número del 1 al 100.")
    print("Lo adivinare.")
    print("Por favor, responde con 'mayor', 'menor' o 'igual'.")

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intento = (limite_inferior + limite_superior) // 2
        respuesta = input(f"¿Es {intento} tu número? ")

        if respuesta == "igual":
            print(f"¡Adiviné tu número en {intentos} intentos!")
            break
        elif respuesta == "mayor":
            limite_inferior = intento + 1
        elif respuesta == "menor":
            limite_superior = intento - 1
        else:
            print("Por favor, responde con 'mayor', 'menor' o 'igual'.")

        intentos += 1
adivinar_numero()

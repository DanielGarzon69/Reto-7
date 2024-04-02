def año_poblacion_superada(poblacion_A, tasa_crecimiento_A, poblacion_B, tasa_crecimiento_B):
    año = 2022
    while poblacion_B <= poblacion_A:
        año += 1
        poblacion_A *= (1 + tasa_crecimiento_A)
        poblacion_B *= (1 + tasa_crecimiento_B)
    return año

# Ejemplo de uso
año_superado = año_poblacion_superada(25, 0.02, 18.9, 0.03)
print("La población de B superará a la de A en el año:", año_superado)

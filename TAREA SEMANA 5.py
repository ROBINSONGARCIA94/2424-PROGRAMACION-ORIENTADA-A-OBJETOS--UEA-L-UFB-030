# Programa: Calculadora de Áreas
# Funcionalidad: Calcula el área de diferentes figuras geométricas (círculo, rectángulo, triángulo).
# Tipos de Datos Utilizados: integer, float, string, boolean.

import math


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): Radio del círculo.

    Retorna:
    float: Área del círculo calculada.
    """
    area = math.pi * radio ** 2
    return area


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dados su base y altura.

    Parámetros:
    base (float): Base del rectángulo.
    altura (float): Altura del rectángulo.

    Retorna:
    float: Área del rectángulo calculada.
    """
    area = base * altura
    return area


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dados su base y altura.

    Parámetros:
    base (float): Base del triángulo.
    altura (float): Altura del triángulo.

    Retorna:
    float: Área del triángulo calculada.
    """
    area = (base * altura) / 2
    return area


# Función principal
def main():
    # Calcular y mostrar el área de un círculo
    radio_circulo = 5.0
    area_circulo = calcular_area_circulo(radio_circulo)
    print(f"Área del círculo con radio {radio_circulo}: {area_circulo:.2f}")

    # Calcular y mostrar el área de un rectángulo
    base_rectangulo = 3.0
    altura_rectangulo = 7.0
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print(f"Área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo}: {area_rectangulo}")

    # Calcular y mostrar el área de un triángulo
    base_triangulo = 4.0
    altura_triangulo = 6.0
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo}: {area_triangulo}")


if __name__ == "__main__":
    main()

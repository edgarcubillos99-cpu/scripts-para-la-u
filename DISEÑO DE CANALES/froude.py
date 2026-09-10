import math

def froude_solver():
    print("--- Froude Calc ---")
    print("1. Rectangular")
    print("2. Trapezoidal")
    print("3. Triangular")
    print("4. Circular")

    tipo = input("Seccion (1-4): ")

    Q = float(input("Caudal Q (m3/s): "))
    y = float(input("Tirante y (m): "))
    g = 9.81

    # Manejo de condicionales segun el tipo de seccion
    if tipo == '1':
        b = float(input("Ancho b (m): "))
        A = b * y
        T = b
    elif tipo == '2':
        b = float(input("Ancho b (m): "))
        z = float(input("Talud z: "))
        A = (b + z * y) * y
        T = b + 2 * z * y
    elif tipo == '3':
        z = float(input("Talud z: "))
        A = z * (y ** 2)
        T = 2 * z * y
    elif tipo == '4':
        d0 = float(input("Diametro d0 (m): "))
        r = d0 / 2
        # Control de desbordamiento para tuberias llenas
        if y > d0:
            print("Flujo a presion!")
            return
        # Uso de radianes para la seccion circular
        theta = 2 * math.acos(1 - y/r)
        A = (r**2 / 2) * (theta - math.sin(theta))
        T = 2 * math.sqrt(r**2 - (r-y)**2)
    else:
        print("Opcion invalida")
        return

    # Calculos hidraulicos unificados
    D = A / T
    V = Q / A
    Fr = V / math.sqrt(g * D)

    # Salida por consola truncada a 4 decimales
    print("\n--- Resultados ---")
    print("A =", round(A, 4), "m2")
    print("T =", round(T, 4), "m")
    print("D =", round(D, 4), "m")
    print("V =", round(V, 4), "m/s")
    print("Fr=", round(Fr, 4))

    # Evaluacion del regimen
    if Fr < 1:
        print("-> Subcritico")
    elif Fr > 1:
        print("-> Supercritico")
    else:
        print("-> Critico")

# Llamada a la funcion principal al ejecutar el script
froude_solver()

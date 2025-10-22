from sympy import Matrix

def calcular_inversa_entera(matriz):
    try:
        matriz_sym = Matrix(matriz)
        
        if matriz_sym.shape[0] != matriz_sym.shape[1]:
            return "La matriz no es cuadrada, no tiene inversa"
        
        if matriz_sym.det() == 0:
            return "El determinante es 0, la matriz no tiene inversa"
        
        inversa = matriz_sym.inv()
        return inversa
    
    except Exception as e:
        return f"Error: {e}"

# Ejemplos de prueba
matriz2x2 = [[1, 2], [3, 4]]
matriz3x3 = [[2, 1, 3], [0, 1, 4], [5, 2, 1]]
matriz4x4 = [
    [1, 0, 2, -1],
    [3, 0, 0, 5],
    [2, 1, 4, -3],
    [1, 0, 5, 0]
]
matriz_singular = [[1, 2], [2, 4]]

ejemplos = [("2x2", matriz2x2), ("3x3", matriz3x3), ("4x4", matriz4x4), ("Singular", matriz_singular)]

for nombre, mat in ejemplos:
    print(f"\nInversa matriz {nombre}:\n", calcular_inversa_entera(mat))

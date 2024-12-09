from scipy.optimize import linprog

# Coeficientes de la función objetivo (minimizar costo)
c = [2, 10]

# Coeficientes de las desigualdades (Ax <= b)
A = [
    [-8, -4],  # 8x + 4y >= 16 => -8x - 4y <= -16
    [1, 1],    # x + y <= 11
    [2, 2],    # 2x + 2y <= 20
    [1, -2]    # x <= 2y => x - 2y <= 0
]
b = [-16, 11, 20, 0]

# Llamada a linprog para resolver el problema
result = linprog(c, A_ub=A, b_ub=b, method="simplex")

# Resultados
if result.success:
    x, y = result.x
    print(f"Kilos de A: {x:.2f}")
    print(f"Kilos de B: {y:.2f}")
    print(f"Costo mínimo: {result.fun:.2f} euros")
else:
    print("No se encontró solución óptima.")

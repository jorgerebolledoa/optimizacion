from scipy.optimize import linprog

# Coeficientes de la función objetivo
c = [1, -2]  # Min z = x1 - 2x2

# Matriz de coeficientes para las restricciones de desigualdad
A = [
    [-4, 6],  # -4x1 + 6x2 <= 9
    [1, 1]    # x1 + x2 <= 10
]

# Vector de límites de las restricciones de desigualdad
b = [9, 10]

# Restricciones para x1, x2 ≥ 0
x_bounds = (0, None)

# Resolver el problema relajado (sin la restricción de enteros)
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method="highs")

# Mostrar resultado
if result.success:
    print("Solución óptima relajada:")
    print("x1 =", result.x[0])
    print("x2 =", result.x[1])
    print("Valor óptimo de z =", result.fun)
else:
    print("No se encontró una solución óptima.")

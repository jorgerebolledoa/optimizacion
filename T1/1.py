import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Definimos los coeficientes de la función objetivo (FO)
c = [-5000, -4000]  # Negativo para maximización en linprog (que minimiza por defecto)

# Coeficientes de las restricciones
A = [
    [1, 1],    # Restricción de piezas
    [2, 1]     # Restricción de horas
]

# Lado derecho de las restricciones
b = [53, 80]

# Resolvemos el problema usando el método simplex
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='simplex')

# Espacio factible y puntos en el gráfico
x_vals = np.linspace(0, 60, 200)
y1 = 53 - x_vals  # y <= 53 - x (piezas)
y2 = 80 - 2 * x_vals  # y <= 80 - 2x (horas)

# Graficar la región factible
plt.figure(figsize=(10, 7))
plt.plot(x_vals, y1, label=r'$x + y \leq 53$')
plt.plot(x_vals, y2, label=r'$2x + y \leq 80$')
plt.fill_between(x_vals, 0, np.minimum(y1, y2), where=(y1 >= 0) & (y2 >= 0), color='grey', alpha=0.3)

# Etiquetas y límites
plt.xlim(0, 60)
plt.ylim(0, 60)
plt.xlabel('Número de collares (x)')
plt.ylabel('Número de pulseras (y)')
plt.title('Región factible para maximizar los beneficios')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

# Solución óptima
sol_x = res.x[0]  # Número de collares
sol_y = res.x[1]  # Número de pulseras
max_benefit = -res.fun  # Negativo porque estamos maximizando

print(f"Número óptimo de collares: {sol_x}")
print(f"Número óptimo de pulseras: {sol_y}")
print(f"Beneficio máximo: {max_benefit}")

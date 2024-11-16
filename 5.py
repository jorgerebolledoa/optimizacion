import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) y su derivada
def f(x):
    return x**2 * np.cos(x) - x / 10

def gradient_f(x):
    return 2 * x * np.cos(x) - x**2 * np.sin(x) - 1/10

# Parámetros iniciales
x0 = 6  # valor inicial
alpha = 0.2  # tasa de aprendizaje inicial
tolerance = 1e-6  # tolerancia para la convergencia
max_iter = 100  # número máximo de iteraciones

# Aplicamos el método del gradiente
def gradient_descent(x0, alpha, tolerance, max_iter):
    x_n = x0
    x_values = [x_n]
    
    for _ in range(max_iter):
        grad = gradient_f(x_n)
        x_next = x_n - alpha * grad
        x_values.append(x_next)
        
        # Comprobamos si la diferencia es menor que la tolerancia
        if abs(x_next - x_n) < tolerance:
            break
            
        x_n = x_next
    
    return x_values

# Ejecución con alpha = 0.2
x_values_0_2 = gradient_descent(x0, 0.2, tolerance, max_iter)

# Ejecución con alpha = 0.d
x_values_0_d = gradient_descent(x0, 0.1, tolerance, max_iter)

# Visualización de resultados
plt.plot(x_values_0_2, label="alpha = 0.2")
plt.plot(x_values_0_d, label="alpha = 0.d")
plt.xlabel("Iteraciones")
plt.ylabel("Valor de x")
plt.legend()
plt.title("Descenso de gradiente para diferentes valores de alpha")
plt.show()


import pulp

# Crear un problema de optimización
prob = pulp.LpProblem("Minimización_Z", pulp.LpMinimize)

# Crear las variables de decisión (enteras no negativas)
x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')

# Definir la función objetivo
prob += x1 - 2 * x2, "Función Objetivo"

# Agregar las restricciones
prob += -4 * x1 + 6 * x2 <= 9, "Restricción 1"
prob += x1 + x2 <= 14, "Restricción 2"

# Resolver el problema
prob.solve()

# Imprimir el estado de la solución
print(f"Estado de la solución: {pulp.LpStatus[prob.status]}")

# Imprimir los valores óptimos de las variables, si existe una solución óptima
if pulp.LpStatus[prob.status] == 'Optimal':
    print(f"Valor óptimo de x1: {x1.varValue}")
    print(f"Valor óptimo de x2: {x2.varValue}")
    print(f"Valor óptimo de z: {pulp.value(prob.objective)}")
else:
    print("No se encontró una solución óptima.")

import numpy as np

def fitness_function_1(x):
    """Función fitness para el problema 1: f(x) = x^3 + 3x^2 - 9x + 1"""
    return x**3 + 3*x**2 - 9*x + 1

def fitness_function_2(x):
    """Función fitness para el problema 2: f(x) = 7*sin(x)"""
    return 7 * np.sin(x)

def initialize_population(size, bounds):
    """Inicializa la población de individuos dentro de los límites dados."""
    return np.random.uniform(bounds[0], bounds[1], size)

def select_parents(population, fitness_values):
    """Selecciona dos padres usando selección por ruleta."""
    # Asegurarse de que las aptitudes sean positivas
    fitness_values = fitness_values - np.min(fitness_values) + 1e-6  # Evitar ceros y valores negativos
    probabilities = fitness_values / np.sum(fitness_values)
    parents_indices = np.random.choice(len(population), size=2, p=probabilities)
    return population[parents_indices]


def crossover(parent1, parent2):
    """Realiza un cruce de un punto entre dos padres."""
    alpha = np.random.rand()  # Mezcla los genes de los padres
    offspring1 = alpha * parent1 + (1 - alpha) * parent2
    offspring2 = alpha * parent2 + (1 - alpha) * parent1
    return offspring1, offspring2

def mutate(individual, bounds, mutation_rate=0.1):
    """Realiza una mutación en un individuo con una tasa de mutación dada."""
    if np.random.rand() < mutation_rate:
        mutation_value = np.random.uniform(bounds[0], bounds[1]) * 0.1
        individual += mutation_value
        individual = np.clip(individual, bounds[0], bounds[1])  # Asegurar límites
    return individual

def genetic_algorithm(fitness_function, bounds, population_size=20, generations=100, mutation_rate=0.1):
    """Algoritmo genético genérico."""
    # Inicializar población
    population = initialize_population(population_size, bounds)
    best_solution = None
    best_fitness = float('-inf')

    for generation in range(generations):
        # Evaluar la aptitud de la población
        fitness_values = np.array([fitness_function(ind) for ind in population])

        # Guardar el mejor individuo
        max_fitness_idx = np.argmax(fitness_values)
        if fitness_values[max_fitness_idx] > best_fitness:
            best_fitness = fitness_values[max_fitness_idx]
            best_solution = population[max_fitness_idx]

        # Generar nueva población
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, bounds, mutation_rate)
            offspring2 = mutate(offspring2, bounds, mutation_rate)
            new_population.extend([offspring1, offspring2])
        population = np.array(new_population[:population_size])

    return best_solution, best_fitness

# Resolver el primer problema: extremos de f(x) = x^3 + 3x^2 - 9x + 1
bounds_1 = (-10, 10)
best_solution_1, best_fitness_1 = genetic_algorithm(fitness_function_1, bounds_1)
print(f"Problema 1: Mejor solución: x = {best_solution_1}, Fitness = {best_fitness_1}")

# Resolver el segundo problema: máximo local de f(x) = 7*sin(x) en [0, pi]
bounds_2 = (0, np.pi)
best_solution_2, best_fitness_2 = genetic_algorithm(fitness_function_2, bounds_2)
print(f"Problema 2: Mejor solución: x = {best_solution_2}, Fitness = {best_fitness_2}")

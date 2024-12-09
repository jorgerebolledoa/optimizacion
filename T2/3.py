import numpy as np

class AntColony:
    def __init__(self, graph, alpha=1, beta=2, evaporation_rate=0.5, ant_count=10, iterations=100):
        """
        Inicializa los parámetros para el algoritmo de colonias de hormigas.
        :param graph: Matriz de adyacencia del grafo con los costos (np.array).
        :param alpha: Peso del nivel de feromonas.
        :param beta: Peso de la visibilidad (1/costo).
        :param evaporation_rate: Tasa de evaporación de feromonas.
        :param ant_count: Número de hormigas.
        :param iterations: Número de iteraciones.
        """
        self.graph = graph
        self.pheromones = np.ones(graph.shape)  # Inicializa las feromonas.
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.ant_count = ant_count
        self.iterations = iterations
        self.num_nodes = graph.shape[0]

    def run(self, start_node, end_node):
        """
        Ejecuta el algoritmo de colonias de hormigas.
        :param start_node: Nodo inicial.
        :param end_node: Nodo final.
        :return: Ruta de menor costo y su costo.
        """
        best_route = None
        best_cost = float('inf')

        for iteration in range(self.iterations):
            routes = []
            costs = []

            for _ in range(self.ant_count):
                route, cost = self._generate_route(start_node, end_node)
                routes.append(route)
                costs.append(cost)

                if cost < best_cost:
                    best_route = route
                    best_cost = cost

            self._update_pheromones(routes, costs)

        return best_route, best_cost

    def _generate_route(self, start_node, end_node):
        """
        Genera una ruta usando probabilidad basada en feromonas y visibilidad.
        :param start_node: Nodo inicial.
        :param end_node: Nodo final.
        :return: Ruta generada y su costo.
        """
        current_node = start_node
        route = [current_node]
        cost = 0

        while current_node != end_node:
            next_node = self._choose_next_node(current_node, route)
            if next_node is None:  # Si no hay nodo disponible, rompe el ciclo.
                return route, float('inf')

            route.append(next_node)
            cost += self.graph[current_node, next_node]
            current_node = next_node

        return route, cost

    def _choose_next_node(self, current_node, visited):
        """
        Selecciona el siguiente nodo basado en la probabilidad.
        :param current_node: Nodo actual.
        :param visited: Nodos ya visitados.
        :return: El siguiente nodo seleccionado.
        """
        probabilities = []
        neighbors = range(self.num_nodes)
        total = 0

        for neighbor in neighbors:
            if neighbor not in visited and self.graph[current_node, neighbor] > 0:
                pheromone = self.pheromones[current_node, neighbor] ** self.alpha
                visibility = (1 / self.graph[current_node, neighbor]) ** self.beta
                total += pheromone * visibility
                probabilities.append((neighbor, pheromone * visibility))

        if total == 0:
            return None

        probabilities = [(node, prob / total) for node, prob in probabilities]
        nodes, probs = zip(*probabilities)
        return np.random.choice(nodes, p=probs)

    def _update_pheromones(self, routes, costs):
        """
        Actualiza las feromonas según las rutas encontradas.
        :param routes: Lista de rutas generadas.
        :param costs: Lista de costos correspondientes.
        """
        self.pheromones *= (1 - self.evaporation_rate)

        for route, cost in zip(routes, costs):
            if cost == float('inf'):
                continue
            for i in range(len(route) - 1):
                self.pheromones[route[i], route[i + 1]] += 1 / cost


# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de adyacencia: los valores son los costos entre nodos, 0 significa no conectado.
    graph = np.array([
        [0, 2, 0, 1, 0],
        [0, 0, 3, 2, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 2],
        [0, 0, 0, 0, 0]
    ])

    colony = AntColony(graph, alpha=1, beta=2, evaporation_rate=0.5, ant_count=10, iterations=50)
    best_route, best_cost = colony.run(start_node=0, end_node=4)

    print(f"Mejor ruta: {best_route}")
    print(f"Mejor costo: {best_cost}")

import numpy as np
import random

class AntColonyKnapsack:
    def __init__(self, boxes, pallet_dims, alpha=1, beta=2, evaporation_rate=0.5, ant_count=10, iterations=100):
        """
        Inicializa el algoritmo de colonia de hormigas para el problema de la mochila 3D.
        :param boxes: Lista de cajas, cada caja es una tupla (largo, ancho, alto, valor).
        :param pallet_dims: Dimensiones del pallet (largo, ancho, altura).
        :param alpha: Peso del nivel de feromonas.
        :param beta: Peso de la heurística (valor de la caja).
        :param evaporation_rate: Tasa de evaporación de feromonas.
        :param ant_count: Número de hormigas.
        :param iterations: Número de iteraciones.
        """
        self.boxes = boxes
        self.pallet_dims = pallet_dims
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.ant_count = ant_count
        self.iterations = iterations
        self.pheromones = np.ones(len(boxes))  # Feromonas inicializadas uniformemente

    def run(self):
        """
        Ejecuta el algoritmo de colonias de hormigas para encontrar la mejor disposición de cajas.
        :return: Disposición óptima de cajas y su valor total.
        """
        best_solution = None
        best_value = 0

        for _ in range(self.iterations):
            solutions = []
            values = []

            for _ in range(self.ant_count):
                solution, value = self._build_solution()
                solutions.append(solution)
                values.append(value)

                if value > best_value:
                    best_solution = solution
                    best_value = value

            self._update_pheromones(solutions, values)

        return best_solution, best_value

    def _build_solution(self):
        """
        Construye una solución utilizando probabilidades basadas en feromonas y valor.
        :return: Disposición de cajas seleccionadas y su valor total.
        """
        solution = []
        total_value = 0
        remaining_area = self.pallet_dims[0] * self.pallet_dims[1]
        remaining_height = self.pallet_dims[2]

        available_boxes = list(range(len(self.boxes)))

        while available_boxes:
            probabilities = self._calculate_probabilities(available_boxes)
            selected_box = np.random.choice(available_boxes, p=probabilities)

            box = self.boxes[selected_box]
            box_area = box[0] * box[1]
            box_height = box[2]

            if box_area <= remaining_area and box_height <= remaining_height:
                solution.append(selected_box)
                total_value += box[3]
                remaining_area -= box_area
                remaining_height -= box_height

            available_boxes.remove(selected_box)

        return solution, total_value

    def _calculate_probabilities(self, available_boxes):
        """
        Calcula las probabilidades de seleccionar cada caja en función de las feromonas y el valor.
        :param available_boxes: Lista de índices de cajas disponibles.
        :return: Probabilidades normalizadas para las cajas disponibles.
        """
        pheromones = np.array([self.pheromones[i] for i in available_boxes])
        values = np.array([self.boxes[i][3] for i in available_boxes])

        attractiveness = (pheromones ** self.alpha) * (values ** self.beta)
        probabilities = attractiveness / attractiveness.sum()
        return probabilities

    def _update_pheromones(self, solutions, values):
        """
        Actualiza las feromonas en función de las soluciones encontradas.
        :param solutions: Lista de soluciones generadas.
        :param values: Valores correspondientes a las soluciones.
        """
        self.pheromones *= (1 - self.evaporation_rate)

        for solution, value in zip(solutions, values):
            for box_idx in solution:
                self.pheromones[box_idx] += value / sum(values)


# Ejemplo de uso
if __name__ == "__main__":
    # Generación de cajas aleatorias: (largo, ancho, alto, valor)
    num_boxes = 20
    boxes = [(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(10, 100)) for _ in range(num_boxes)]

    # Dimensiones del pallet: (largo, ancho, altura)
    pallet_dims = (10, 10, 15)

    # Mostrar los datos generados
    print("Datos de entrada:")
    print("Cajas (largo, ancho, alto, valor):")
    for i, box in enumerate(boxes):
        print(f"Caja {i+1}: {box}")
    print(f"Dimensiones del pallet: {pallet_dims}")

    # Ejecutar la colonia de hormigas
    colony = AntColonyKnapsack(boxes, pallet_dims, alpha=1, beta=2, evaporation_rate=0.5, ant_count=10, iterations=50)
    best_solution, best_value = colony.run()

    # Mostrar los resultados
    print("\nResultados:")
    print(f"Mejor valor total: {best_value}")
    print("Cajas seleccionadas:")
    for i in best_solution:
        print(f"Caja {i+1}: {boxes[i]}")

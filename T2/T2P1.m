function busquedaAleatoriaYTabu()
    % Parámetros del problema
    maxIter = 1000;       % Máximo de iteraciones
    rango = [50, 100];   % Rango de búsqueda para las variables
    dim = 1;             % Dimensión del problema
    tamTabu = 5;         % Tamaño de la lista tabú

    % Inicialización
    mejorSolucion = rand(1, dim) * (rango(2) - rango(1)) + rango(1);
    mejorCosto = funcionObjetivo(mejorSolucion);
    listaTabu = []; % Lista tabú inicial vacía

    % Algoritmo principal
    for iter = 1:maxIter
        % Generar una solución aleatoria
        nuevaSolucion = rand(1, dim) * (rango(2) - rango(1)) + rango(1);

        % Verificar si está en la lista tabú
        while estaEnListaTabu(listaTabu, nuevaSolucion)
            nuevaSolucion = rand(1, dim) * (rango(2) - rango(1)) + rango(1);
        end

        % Evaluar la solución
        nuevoCosto = funcionObjetivo(nuevaSolucion);

        % Actualizar el mejor costo
        if nuevoCosto < mejorCosto
            mejorSolucion = nuevaSolucion;
            mejorCosto = nuevoCosto;
        end

        % Actualizar la lista tabú
        listaTabu = actualizarListaTabu(listaTabu, nuevaSolucion, tamTabu);

        % Imprimir resultados
        fprintf('Iteración %d: Mejor Costo = %.4f\n', iter, mejorCosto);
    end

    % Mostrar resultados finales
    fprintf('\nMejor Solución Encontrada: [%s]\n', num2str(mejorSolucion));
    fprintf('Costo de la Mejor Solución: %.4f\n', mejorCosto);
end

function costo = funcionObjetivo(x)
    % Ejemplo: Función esfera (minimizar la suma de los cuadrados)
    costo = sum(x.^2);
end

function esta = estaEnListaTabu(listaTabu, solucion)
    % Verifica si una solución está en la lista tabú
    esta = any(ismember(listaTabu, solucion, 'rows'));
end

function listaTabu = actualizarListaTabu(listaTabu, solucion, tamTabu)
    % Añade una solución a la lista tabú y asegura que no exceda el tamaño máximo
    listaTabu = [listaTabu; solucion]; % Añadir la solución
    if size(listaTabu, 1) > tamTabu
        listaTabu(1, :) = []; % Remover la más antigua
    end
end

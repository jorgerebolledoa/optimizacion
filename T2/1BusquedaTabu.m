% Función objetivo (modificar según el problema a resolver)
f = @(x) x(1)^2 + x(2)^2; % Ejemplo: minimizar f(x) = x1^2 + x2^2

% Configuración
dim = 2;                % Dimensión del problema
x_min = -10;            % Límite inferior del espacio de búsqueda
x_max = 10;             % Límite superior del espacio de búsqueda
max_iter = 100;         % Número máximo de iteraciones
tabu_size = 10;         % Tamaño de la lista tabú
neighborhood_size = 50; % Número de vecinos generados por iteración

% Inicialización
current_x = x_min + (x_max - x_min) * rand(1, dim); % Solución inicial aleatoria
best_x = current_x;      % Mejor solución encontrada
best_f = f(current_x);   % Mejor valor de la función objetivo
tabu_list = [];          % Lista tabú
history = [];            % Historial de las soluciones (opcional)

% Preparar la gráfica
figure;
hold on;
xlabel('x1');
ylabel('x2');
title('Búsqueda Tabú - Proceso de Optimización');
grid on;
xlim([x_min, x_max]);
ylim([x_min, x_max]);

% Proceso de búsqueda tabú
for iter = 1:max_iter
    % Generar el vecindario
    neighborhood = [];
    for i = 1:neighborhood_size
        neighbor = current_x + (rand(1, dim) - 0.5) * 2; % Aleatorio en [-1, 1]
        neighbor = max(min(neighbor, x_max), x_min); % Limitar al espacio de búsqueda
        neighborhood = [neighborhood; neighbor];
    end

    % Evaluar las soluciones en el vecindario
    values = [];
    for i = 1:size(neighborhood, 1)
        values = [values; f(neighborhood(i, :))];
    end

    % Filtrar las soluciones tabú
    is_tabu = false(size(neighborhood, 1), 1);
    for i = 1:size(neighborhood, 1)
        for j = 1:size(tabu_list, 1)
            if norm(neighborhood(i, :) - tabu_list(j, :)) < 1e-6
                is_tabu(i) = true;
                break;
            end
        end
    end
    neighborhood(is_tabu, :) = [];
    values(is_tabu) = [];

    % Encontrar la mejor solución en el vecindario
    [min_val, min_idx] = min(values);
    candidate_x = neighborhood(min_idx, :);

    % Actualizar la mejor solución global si es mejor
    if min_val < best_f
        best_f = min_val;
        best_x = candidate_x;
    end

    % Actualizar la solución actual y la lista tabú
    current_x = candidate_x;
    tabu_list = [tabu_list; candidate_x];
    if size(tabu_list, 1) > tabu_size
        tabu_list(1, :) = []; % Eliminar el elemento más antiguo
    end

    % Guardar historial para graficar
    history = [history; current_x];

    % Dibujar el progreso
    scatter(current_x(1), current_x(2), 20, 'b', 'filled'); % Solución actual
    drawnow;
end

% Mostrar la mejor solución
scatter(best_x(1), best_x(2), 100, 'r', 'filled'); % Mejor solución final
legend('Soluciones Evaluadas', 'Mejor Solución Final');
hold off;

% Resultados
fprintf('\nMejor solución encontrada: x = [%f, %f]\n', best_x(1), best_x(2));
fprintf('Valor de la función objetivo: f(x) = %f\n', best_f);


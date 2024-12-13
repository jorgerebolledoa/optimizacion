% Función objetivo (modificar según el problema a resolver)
f = @(x) x(1)^2 + x(2)^2; % Ejemplo: minimizar f(x) = x1^2 + x2^2

% Configuración de la búsqueda
num_iter = 1000;       % Número de iteraciones
dim = 2;               % Dimensión del problema
x_min = -10;           % Límite inferior del espacio de búsqueda
x_max = 10;            % Límite superior del espacio de búsqueda

% Inicialización
best_x = [];           % Mejor solución encontrada
best_f = Inf;          % Valor mínimo encontrado
history = [];          % Historial de valores encontrados (opcional)

% Proceso de búsqueda aleatoria
for iter = 1:num_iter
    % Generar un punto aleatorio en el espacio de búsqueda
    x = x_min + (x_max - x_min) * rand(1, dim);

    % Evaluar la función objetivo
    current_f = f(x);

    % Actualizar la mejor solución si es necesario
    if current_f < best_f
        best_f = current_f;
        best_x = x;
    end

    % Guardar el historial (opcional)
    history = [history; iter, x, current_f];
end

% Resultados
fprintf('Mejor solución encontrada: x = [%f, %f]\n', best_x(1), best_x(2));
fprintf('Valor de la función objetivo: f(x) = %f\n', best_f);

% Visualización del proceso (opcional para problemas en 2D)
if dim == 2
    figure;
    scatter(history(:, 2), history(:, 3), 10, 'filled'); % Puntos explorados
    hold on;
    plot(best_x(1), best_x(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2); % Mejor solución
    xlabel('x1'); ylabel('x2');
    title('Búsqueda aleatoria');
    legend('Puntos explorados', 'Mejor solución');
    grid on;
end


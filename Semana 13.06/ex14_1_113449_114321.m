x = 1:0.01:3;
y_for = zeros(size(x));

% Ciclo for:
tic
for i = 1:length(x)
    y_for(i) = x(i)^2 - 3*x(i) + 2;
end
tempo_for = toc;

% Vetorização:
tic
y_vec = x.^2 - 3.*x + 2;
tempo_vec = toc;

% Tempos:
fprintf('Tempo do for loop: %.6f seconds\n', tempo_for);
fprintf('Tempo da vetorização: %.6f seconds\n', tempo_vec);

% Plot da função:
plot(x, y_for, 'b-');
hold on;
plot(x, y_vec, 'g:');
hold off;
grid on;
xlabel('x');
ylabel('y');
title('Função: y(x) = x^2 - 3x + 2');

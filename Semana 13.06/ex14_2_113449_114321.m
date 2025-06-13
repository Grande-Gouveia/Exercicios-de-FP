disp('This program performs a least−squares fit of an ');
disp('input data set to a straight line.');
% Read the input data
data = readmatrix("input1.dat");
linhas = size(data,1);
for ii = 1:linhas
    x(ii) = data(ii,1);
    y(ii) = data(ii,2);
end
% Accumulate statistics
sum_x = 0;
sum_y = 0;
sum_x2 = 0;
sum_xy = 0;
for ii = 1:linhas
    sum_x = sum_x + x(ii);
    sum_y = sum_y + y(ii);
    sum_x2 = sum_x2 + x(ii)^2;
    sum_xy = sum_xy + x(ii) * y(ii);
end
% Now calculate the slope and intercept.
x_bar = sum_x / linhas;
y_bar = sum_y / linhas;
slope = (sum_xy - sum_x * y_bar) / ( sum_x2 - sum_x * x_bar);
y_int = y_bar - slope * x_bar;
% Tell user.
disp('Regression coefficients for the least−squares line:');
fprintf(' Slope (m) = %8.3f\n', slope);
fprintf(' Intercept (b) = %8.3f\n', y_int);
fprintf(' No. of points = %8d\n', linhas);
% Plot the data points as blue circles with no
% connecting lines.
plot(x,y,'bo');
hold on;
% Create the fitted line
xmin = min(x);
xmax = max(x);
ymin = slope * xmin + y_int;
ymax = slope * xmax + y_int;
% Plot a solid red line with no markers
plot([xmin xmax],[ymin ymax],'r-',"LineWidth",2);
hold off;
% Add a title and legend
title ('\bfLeast−Squares Fit');
xlabel('\bf\itx');
ylabel('\bf\ity');
legend('Input data','Fitted line');
grid on


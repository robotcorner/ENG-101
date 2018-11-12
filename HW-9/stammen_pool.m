%% File Details - Stephen Stammen
    clear; close all; clc; % cleans out the working files / console
%% Dimensions of the yard:
%       Area of the square 1765.3 ft^2
%       radius = 21.0080 ft
%       The yard is 42.015' * % 42.015'
%% Main Program
    x0 = 1.8; % the width of the rectangle
    y0 = 12.5; % the height of the rectangle
    x1 = 10:0.001:25; % creates a series of possible distances
    for idx = 1:length(x1) % from 1 to the length of the x1 vector loop
        R = x0 + x1(idx); % the radius = the rectangle width plus the possible x1 value
        y1 = R - y0; % the point where the circle and the rectangle would touch on the inside of the square 
        if abs((x1(idx)^2+y1^2 - R*R)) < 0.01 % if this equation is close to 0 like it should be, then the values should be accurate
            diameter = 2*R % gives the diameter / sidelenght of the square around the circle 
            AreaSquare = diameter^2 % gives the area of the square
            radius = R % gives the radius
        end % end of if statement
    end % end of the for loop
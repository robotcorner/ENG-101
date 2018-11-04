% Stephen Stammen
% dampedSinusoid.m
% save plot to dampSine.fig w/ the savefig command

clear; % clears variable before starting
close all; % closes all figures
clc; % clears the command line

t = 0:.001:10; % first num = start, second = 10ms increment, thrid = end
e = 2.71828; % e had to be defined because it's not part of MATLAB
expVect = (e.^(-t/2)); % exponent curve
sinusoidVect = sin(2*pi*t); % sinusoid function describe on the HW

dampSin = expVect .* sinusoidVect; % .* dot product multiplication to calculate correctly

hold on; % Makes sure that the graphs add on to each other and don't overwrite
plot(t, sinusoidVect,'DisplayName','sine'); % Plots the sine vector
plot(t, expVect,'DisplayName','exp'); % Plots the exponent vector defined in the HW
plot(t, dampSin,'DisplayName','damp'); % Plots the dampSin fuction
xlabel('time[sec]'); % labels the x axis
ylabel('amplitude [V]'); % labels the y axis
title('Damped Sinusoid Plot'); % give a title
legend(); % provides a legend or key int the top right the with the names descriped from the plot functions
hold off; % turns off the graph holding

savefig('dampSin.fig'); % Saves the file as a figure in MATLAB
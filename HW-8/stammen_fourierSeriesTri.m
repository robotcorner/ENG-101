% fourierSeriesTri.m
% Stephen Stammen
% Housekeeping
    clc; close all; clear;

time = -2:0.001:2; % time vector = 10 seconds in milliseconds
T = 1; % T Period of Signal
tau = 0.5; % Tau  = Width of Pulse
N = 100; % Number of Harmonics / repititions
signal = zeros(1, length(time)); % Initialize Signal / creates a vector of 0's the length of the time vector
mySinc = @(x) sin(x)./(x+eps); % mySinc - Declares a different version of Sinc as a function handle

for idx = 1:N % For Loop up to N terms    
    triWave = (tau/T)*(mySinc((idx*tau*pi)/(2*T)))^2; % This is the signal of an triangluar / saw-like wave
    signal = triWave*cos((2*pi*time*idx)/T)+signal; % This is the Fourier Series Equation
    if (idx==5||idx==10||idx==N) % Plots the graphs of each of these index values
        hold on; % keeps the graph on so each idx value doesn't remove the last graph drawn
        plot(time,signal) % plots this graph for an idx value of 5, 10, and 100  
    end % end if statement
end % end for statement

xlabel('time [sec]') % labels the x axis - These are outside the for loop do they are not written 3 times, once for idx 5, once idx 10, and once idx 100
ylabel('amplitude') % labels the y axis
grid on; % turns the grid on
legend('5 Terms','10 terms', '100 terms') % names each graph on the legend, this needs to be in the order of the if index statement in the for loop
title('Fourier Series of Trianglular Wave') % gives a title

savefig('stammen_fourierSeriesTriangle.fig') % saves the graph
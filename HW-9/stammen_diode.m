%% File Details - Stephen Stammen
% This file plots supply voltage, load voltage w/ an ideal diode, and load voltage w/ a not ideal diode vs time
% Houskeeping
    clc; close all; clear;
%% Equations
% Time Vector
    t = 0:0.01:10; % seconds
% Supply Voltage
    v = 3*exp(-t./3).*sin(pi.*t); % volts - this is the equation provided
    
%% Ploting
% Plot time and voltage
    subplot(3,1,1) % creates a subplot that has 3 rows and 1 column
    plot(t,v) % supply voltage vs time
    grid on % turns on the grid
    title('Supply Voltage vs Time') % provides a title (y axis vs x axis)
    xlabel('time [s]') % labels the x axis
    ylabel('voltage [V]') % labels the y axis
    ylim([-3,3]) % sets a y-axis range 
    
    subplot(3,1,2) % subplot row 2
    v(v<0) = 0; % sets the voltage of anything negative to 0 and overwrites the original voltage vector
    plot(t,v) % ideal diode voltage
    grid on % turns on the grid
    title('Ideal Diode Voltage vs Time') % gives a title
    xlabel('time [s]') % labels the x axis
    ylabel('voltage [V]') % labels the y axis
    ylim([-1,3])
    
    subplot(3,1,3) % subplot row 3
    v(v<0.6) = 0; % sets the voltage of anything under 0.6 to 0 and overwrites the voltage vector with 0's for negative numbers
    plot(t,v) % non-ideal diode voltage
    grid on % turns the grid on
    title('Non-Ideal Diode Voltage vs Time')
    xlabel('time [s]') % labels the x axis
    ylabel('voltage [V]') % labels the y axis
    ylim([-1,3])
    
    savefig('stammen_diode.fig') % saves the graph as a figure










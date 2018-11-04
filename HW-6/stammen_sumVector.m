% sumVector.m
% Stephen Stammen

clear; % clears variable before starting
close all; % closes all figures
clc; % clears the command line

% allows the user to input N the end of the series
N = input('Enter the number of integers  '); 

% Sums all of the vectors from 1 to N and prints because there is no
% semi-colon, so it's not supressed.
vectorSum = sum(1:N) 
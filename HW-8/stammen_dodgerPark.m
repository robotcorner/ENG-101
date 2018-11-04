% Stephen Stammen
%% File Description
% This file creates a plot of the hitting angles and velocities required to
% hit a home run and get over the 8 foot wall at the back of dodgerPark.
%% Housekeeping
    clc; close all; clear;
%% Coversion Factor
    FT2M = 0.3048; % feet to meters
    MPH2MPS = .44704; % miles per hour to miles per second
    M2FT = 1/FT2M; % meters to feet
    MPS2MPH = 1/MPH2MPS; % miles per second to mile per hour
%% Physical Constant
    G = 9.8; % m/s^2
%% Distance from homeplate to the to the wall
    x_dist_m = 330*FT2M; % changes 330 ft to meters
%% Distance above the 4 foot batter to the 8 foot wall
    y_dist_m = (8-4)*FT2M; % the 8' wall minus the 4' hitting height to meters
%% Angle
    ang = 10:1:70; % batting angles from 10 to 70
%% Time Vector    
    t = linspace(0,10,1000); % create a vector of 1000 evenly spaced points between 0 and 10
%% Speed
    v = MPS2MPH*sqrt((G*((x_dist_m)^2)/2)./(cosd(ang).*(sind(ang)*x_dist_m-cosd(ang)*y_dist_m))); % provided equation for velocity converted to per second because thats what the v equation is in
%% Plots Minimum Angles and Lauch Speeds that get the ball over the fence
    plot(ang, v) % Plots the minimum angle and velocity combinations to hit the ball over the back fence for a home run
    xlabel('angle[deg]') % labels the x axis
    ylabel('speed [mph]') % labels the y axis
    xlim([10 45]) % sets a limit on the x axis = to the total wall distance
    savefig('stammen_dodger.fig') % saves the graph
 
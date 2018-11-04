% Stephen Stammen
%% File Description
% This file verifies the angles and velocities if you enter in a specific one in 'stammen_dodgerPark.m' or
% 'stammen_dodger.fig' That file creates a plot of the hitting angles and velocities required to
% hit a home run and get over the 8 foot wall at the back of dodgerPark.
%% Housekeeping
    clc; close all; clear;
%% Coversion Factor
    FT2M = 0.3048; % feet to meters
    MPH2MPS = .44704; % miles per hour to miles per second
    M2FT = 1/FT2M; % meters to feet
    MPS2MPH = 1/MPH2MPS; % miles per second to miles per hour
%% Physical Constant
    G = 9.8; % m/s^2
%% Angle
    ang = 20; % degress
%% Speed
    v = 89.09*MPH2MPS; % velocity converted to miles per second for correct equation math
%% Time Vector    
    t = linspace(0,10,1000); % create a vector of 1000 evenly spaced points between 0 and 10
%% x Position over time
    x = v*cosd(ang).*t; %cosd takes the angle as a degree, which is what was inputed .*t becasue its a vector
%% y Position over time
    y = -0.5*G*t.^2+v*sind(ang).*t; % this is the position formula
%% Plot x position vs y position
    plot(x*M2FT,y*M2FT) % plot x and y positions in feet, meters was just for calculations, this traces a theorhetical ball path through the air
    xlabel('Ball Distance from Home Plate [ft]') % labels the x axis
    ylabel('Height Above the 4 ft Batter [ft]') % labels the y axis
    xlim([0 310]) % sets a limit on the x axis = to the total wall distance
    ylim([0 200]) % sets a limit on the y axis so its not too tall
 
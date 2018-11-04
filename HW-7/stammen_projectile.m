%% File Setup
% Stephen Stammen
% ENG 101 | 10-20-2018
% Housekeeping
    clear
    close all;
    clc
%% set up variables and constants
launchAngle = (5*pi)/12; % specified launch angle
startHeight = 0; % initial height variable
startX = 0; % initial distance variable
startVelocity = 50.75; 
t = 0:.01:10;
g = 9.8; % earths gravity
%% projectile trajectory for ideal porjectivle motion
% vertical distance
y = startHeight - ((1/2)*g.*t.^2) + (startVelocity*sin(launchAngle)).*t; % .multiply because element by element multiplication is needed
% horizontal distance
x = startX + (startVelocity*cos(launchAngle)).*t; % .multiply because element by element multiplication is needed

%% Plot ProjectileGraph1 - Max height for projectile: approximately 122.06
% Subplot 1 = y vs t
subplot(2,1,1) % creates the first subplot - indicated by the last number
plot(t,y) % plots height vs time
grid on % turns the grid on
title('Height vs Time') % gives title
xlabel('time [sec]') % labels the x axis
ylabel('height [m]') % labels y axis
ylim([0 150]) % sets a y lim so the graph is viewed properly
 
% Subplot 2 = x vs t
subplot(2,1,2) % creates the second subplot - indicated by the last number
plot(t,x) % plots distance vs time
grid on % turns on the grid
title('Horizontal Distance vs Time') % gives a title
xlabel('time [sec]') % labels the x axis
ylabel('horizontal distance [m]') % labels the y axis
ylim([0 150]) % gives the y axis a limit so it views properly

%% Plot ProjectileGraph2
figure % creates a second figure
plot(x,y) % plots vertical distance vs horizontal distance
grid on % turns on the grid
title('Vertical Distance vs Horizontal Distance') % gives the graph a title
xlabel('horizontal distance [m]') % labels the x axis
ylabel('height [m]') % labels the y axis
ylim([0 150]) % gives the y axis a lim, show it views properly

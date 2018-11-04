%% File Setup
% Stephen Stammen
% ENG 101 | 10-20-2018
% Housekeeping
    clear
    close all;
    clc
%% set up variables and constants
launchAngle0 = (5*pi)/12;
launchAngle1 = (5*pi)/12-0.255; % The launch angles specified
launchAngle2 = (5*pi)/12-0.425;
startHeight = 0; % initial height
startX = 0; % initial distance
startVelocity = 50.75; % initial velocity
t = 0:.01:10; % creates a time vector
g = 9.8; % earths gravity
%% projectile trajectory for ideal porjectivle motion
% vertical distance w/ different launch angles
y = startHeight - ((1/2)*g.*t.^2) + (startVelocity*sin(launchAngle0)).*t;
y1 = startHeight - ((1/2)*g.*t.^2) + (startVelocity*sin(launchAngle1)).*t; % the y function equation with the diff angles
y2 = startHeight - ((1/2)*g.*t.^2) + (startVelocity*sin(launchAngle2)).*t;
% horizontal distance w/ different launch angles
x = startX + (startVelocity*cos(launchAngle0)).*t;
x1 = startX + (startVelocity*cos(launchAngle1)).*t; % the x function equation with the diff angles
x2 = startX + (startVelocity*cos(launchAngle2)).*t;

%% Plot Projectile2_Graph1 - Multiple angles
% Subplot 1 = y vs t
subplot(2,1,1) % subplot 1
hold on % holds the graph so the plots can be placed on top of each other
plot(t,y,':','DisplayName','\theta zero') % theta 1 - dotted line, gives a name for the legend
plot(t,y1,'-.','DisplayName','\theta one') % theta 2 - dash-dot line, gives name for legend
plot(t,y2,'--','DisplayName','\theta two') % theta 3 - dashed line, name for legend
grid on
hold off
title('Height vs Time') % gives title
xlabel('time [sec]') % these are very self explanatory
ylabel('height [m]')
ylim([0 150]) % sets a y lim so the graph is viewed properly
legend(); % gives a legend in the top right with the display names

% Subplot 2 = x vs t
subplot(2,1,2) % subplot 2
hold on
plot(t,x,':','DisplayName','\theta zero') % theta 1 - dotted line, gives a name for the legend
plot(t,x1,'-.','DisplayName','\theta one') % theta 2 - dash-dot line, gives name for legend
plot(t,x2,'--','DisplayName','\theta two') % theta 3 - dashed line, name for legend
grid on
hold off
title('Horizontal Distance vs Time') % gives a title
xlabel('time [sec]')
ylabel('horizontal distance [m]')
ylim([0 150]) % sets a y lim so the graph is viewed properly
legend(); % shows the legend, which shows the display names
%% Plot Projectile2_Graph2 - Multiple angles
figure % creates a second figure
hold on
plot(x,y,':','DisplayName','\theta zero') % theta 1 - dotted line, gives a name for the legend
plot(x1,y1,'-.','DisplayName','\theta one') % theta 2 - dash-dot line, gives name for legend
plot(x2,y2,'--','DisplayName','\theta two') % theta 3 - dashed line, name for legend
grid on
title('Vertical Distance vs Horizontal Distance') % gives the graph a title
xlabel('horizontal distance [m]')
ylabel('height [m]')
ylim([0 150]) % sets a y lim so the graph is viewed properly
legend(); % gives a legend in the top right with the display names
% Which angle produces the furthest horizontal displacement?  theta2 produced the furthest distance at around 257 meters
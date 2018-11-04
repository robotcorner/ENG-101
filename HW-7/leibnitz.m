%% File Setup
% Stephen Stammen
% ENG 101 | 10-27-2018
% Housekeeping - clears work envirionment
    clear;
    close all;
    clc;
%% For Loop that uses vectorization inside of it
for idx = 1:8 % Loops through 8 times
    lSeries = sum(((-1).^((1:2:2*(10^idx))))./((2.*(1:2:2*(10^idx)))+1))*4; % for each loop creates a series to the nTerms 10, 100, 1000, 10000... 10^8. Then the lSeries is calculated and the sum of that vector is calculated to save memory.
    % LSeries is multiplied by 4 becasue it only returns pi / 4 originally
    accuracy(idx) = abs(lSeries-pi); % creates a vector of the accuracy value calculated after each iteration of the for loop. This value is calculated by taking the value calculated and seeing the difference of the internal pi
end % ends the for loop

%% Graphs accuracy vs the number of terms in the series as a logatrithmic plot
loglog(10.^(1:8),accuracy) % graphs the nTerms vs the accuracy values calculated
grid on % turns the grid on
xlim([10^1 10^8]) % sets an xlim so that the graph is rendered properly
xlabel('Length of Series [N]') % labels the x axis
ylabel('Accuracy') % labels the y axis
title('Accuracy of Leibnitz Series Calculation for \pi') % gives title to graph
savefig('leibnitzAcc.fig'); % Saves the file as a figure in MATLAB


function [y] = myFibon(n)
%Does Fibonanci Recursively
%   1,1,2,3,5,8
    if n == 1 || n == 2
        y = 1;
    else
        y = myFibon(n-1)+myFibon(n-2);
end


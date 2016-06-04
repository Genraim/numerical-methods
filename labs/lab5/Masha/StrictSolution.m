function y = StrictSolution(x)
	alpha = 2.2;
	y = exp(x) + exp(-x) + alpha .* x.^2 - alpha .* x - 2;
end 
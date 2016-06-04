function res = f(x, y)

	alpha = 2.2;
	res = zeros(2, 1);
	res(1) = y(2);
	res(2) = y(1) + 2*alpha + 2 + alpha*x*(1-x);
end
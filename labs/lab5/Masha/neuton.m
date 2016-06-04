function [x, y] = neuton(h)

	x = 0:h:1;
	N = length(x);
	y = zeros(1, N);

	alpha = 2.2;
	lastY1 = exp(1) - exp(-1) + alpha;



	epsilon = .001;

	mu = 1;
	muNext = 100000;
	temp = 0;

	while abs(muNext - mu) >= epsilon
		muNext = mu - func(mu)/(exp(1)/2 + exp(-1)/2);
		temp = mu;
		mu = muNext;
		muNext = temp;
	end

	res = runge(h, mu);

	y = res(1,:);


	function val = func(mu)
		y = runge(h, mu);
		val = y(2, end) - lastY1;
	end
end
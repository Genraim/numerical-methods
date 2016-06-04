function [x, y] = prog(h)
	alpha1 = 2.2;


	x = 0:h:1;
	N = length(x);


	y = zeros(1,N);
	alpha = zeros(1,N + 1);
	beta = zeros(1,N + 1);

	for i = 1:N
		alpha(i+1) = -B(i)/(A(i)*alpha(i)+C(i));
		beta(i+1) = (F(i) - A(i)*beta(i))/(A(i)*alpha(i)+C(i));
	end

	y(N) = beta(N+1);
	for i = N-1:-1:1
		y(i) = alpha(i+1)*y(i+1) + beta(i+1);
	end


	function res = A(n)
		if (n==1)
			res = 0;
		elseif n<N
			res = 1;
		else
			res = -1;
		end
	end
	function res = B(n)
		if n == 1
			res = 0;
		elseif n < N
			res = 1;
		else
			res = 0;
		end
	end
	function res = C(n)
		if n==1
			res = 1;
		elseif n<N
			res = -(2+h^2);
		else
			res = 1;
		end
	end
	function res = F(n)
		if n == 1
			res = 0;
		elseif n < N
			res = h^2 * (2*alpha1 + 2 + alpha1 * x(n) * (1 - x(n)));
		else
			res = h * (exp(1) - exp(-1) + alpha1);
		end
	end
end
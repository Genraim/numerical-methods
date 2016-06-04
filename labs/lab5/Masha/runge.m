function y = runge(h, mu)

	alpha = 2.2;

	x = 0:h:1;
	N = length(x);
	y = zeros(2, N);
	y(:, 1) = [0; mu];

	k1 = zeros(2, 1);			
	k2 = zeros(2, 1);
	k3 = zeros(2, 1);
	k4 = zeros(2, 1);

	for i = 1:N-1
		k1 = h * f(x(i),y(:,i));
		k2 = h * f(x(i)+h/2,y(:,i) + k1/2);
		k3 = h * f(x(i)+h/2,y(:,i) + k2/2);
		k4 = h * f(x(i)+h,y(:,i) + k3);
		y(:, i+1) = y(:, i) + 1/6*(k1 + 2*k2 + 2*k3 + k4);
	end
end
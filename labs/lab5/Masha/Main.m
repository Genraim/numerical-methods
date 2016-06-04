function Main()
	clear all
	close all
	clc


	x = 0:.01:1;
	y = StrictSolution(x);
	plot(x,y,'LineWidth', 2);
	hold on
	grid on

	[x, y] = neuton(.2);
	plot(x,y,'r','LineWidth', 2);

	% [x, y] = neuton(.1);
	% plot(x,y,'g','LineWidth', 2);

	legend('analytical', 'h = 0.2');
end
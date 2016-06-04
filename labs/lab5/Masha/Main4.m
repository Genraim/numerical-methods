function Main4()
	clear all
	close all
	clc


	x = 0:.01:1;
	y = StrictSolution(x);
	plot(x,y,'LineWidth', 2);
	hold on
	grid on

	[x, y] = neuton(.05);
	plot(x,y,'r','LineWidth', 2);

	[x, y] = prog(.05);
	plot(x,y,'g','LineWidth', 2);

	legend('analytical', 'shoot', 'progonka');
end
function Main2()
	clear all
	close all
	clc


	x = 0:.01:1;
	y = StrictSolution(x);
	plot(x,y,'LineWidth', 2);
	hold on
	grid on

	[x, y] = prog(.1);
	plot(x,y,'r','LineWidth', 2);

	[x, y] = prog(.01);
	plot(x,y,'g','LineWidth', 2);


	legend('analytical', 'h = 0.5', 'h = 0.1');
end
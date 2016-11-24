import turtle;

window = turtle.Screen();
my_turtle = turtle.Turtle();

def star():
	window.clear();
	turtle.hideturtle();
	turtle.setpos(0, 0);
	turtle.left(120);
	for  x in range(5):
		turtle.forward(250);
		turtle.right(144);
	turtle.showturtle();

def isOnTurtle(x, y):
	print("hi");
	if (x >= turtle.xcor() - 10 and x <= turtle.xcor() + 10):
		if (y >= turtle.ycor() - 10 and y <= turtle.ycor() + 10):
			star();

def main():
	star();
	for x in range(100):
		turtle.onclick(isOnTurtle);

main();

window.listen();
window.mainloop();
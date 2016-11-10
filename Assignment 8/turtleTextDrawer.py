import turtle;
import math;

window = turtle.Screen();
my_turtle = turtle.Turtle();


def getProperInput():
	good = False;
	while (good == False):
		print("Welcome to Bryce Hahn's Turtle Text Drawer!\nPlease enter a sentence containing max 6 of the following characters: [B,R,Y,C,E,I]");
		inp = input(">>");
		inp = inp.lower();
		if (len(inp) <= 6):
			good = True;
			if (checkInputForChars(inp)):
				good = True;
			else:
				print("You did not enter the proper options of [B, R, Y, C, E, or I]");
				good = False;
		else:
			print("You entered more than 6 characters...");
			good = False;
	return inp;

def checkInputForChars(inp):
	print(len(inp));
	good = True;
	if not (inp[0] == 'b' or inp[0] == 'r' or inp[0] == 'y' or inp[0] == 'c' or inp[0] == 'e' or inp[0] == 'i'):
		good = False;

	if (len(inp) >= 2):
		if not (inp[1] == 'b' or inp[1] == 'r' or inp[1] == 'y' or inp[1] == 'c' or inp[1] == 'e' or inp[1] == 'i'):
			good = False;

	if (len(inp) >= 3):
		if not (inp[2] == 'b' or inp[2] == 'r' or inp[2] == 'y' or inp[2] == 'c' or inp[2] == 'e' or inp[2] == 'i'):
			good = False;

	if (len(inp) >= 4):
		if not (inp[3] == 'b' or inp[3] == 'r' or inp[3] == 'y' or inp[3] == 'c' or inp[3] == 'e' or inp[3] == 'i'):
			good = False;

	if (len(inp) >= 5):
		if not (inp[4] == 'b' or inp[4] == 'r' or inp[4] == 'y' or inp[4] == 'c' or inp[4] == 'e' or inp[4] == 'i'):
			good = False;

	if (len(inp) >= 6):
		if not (inp[5] == 'b' or inp[5] == 'r' or inp[5] == 'y' or inp[5] == 'c' or inp[5] == 'e' or inp[5] == 'i'):
			good = False;

	if (len(inp) == 7):
		if not (inp[6] == 'b' or inp[6] == 'r' or inp[6] == 'y' or inp[6] == 'c' or inp[6] == 'e' or inp[6] == 'i'):
			good = False;

	return good;

def b():
	turtle.left(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50)
	turtle.right(90);
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);
	turtle.right(90);

def r():
	turtle.left(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);
	turtle.sety(turtle.ycor() + 50);
	turtle.left(45);
	turtle.forward(math.sqrt(5000));
	turtle.left(45);

def y():
	turtle.right(90);
	turtle.forward(50);
	turtle.left(225);
	turtle.sety(turtle.ycor() + 50);
	turtle.forward(math.sqrt(5000));
	turtle.penup();
	turtle.setx(turtle.xcor() + 50);
	turtle.sety(turtle.ycor() - 50);
	turtle.pendown();
	turtle.right(90);
	turtle.forward(math.sqrt(5000));
	turtle.right(45);
	turtle.penup();
	turtle.sety(turtle.ycor() + 50);
	turtle.pendown();
	turtle.right(90);
	turtle.left(90);


def c():
	turtle.left(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.penup();
	turtle.setx(turtle.xcor() - 50);
	turtle.sety(turtle.ycor() - 50);
	turtle.pendown();
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);

def e():
	turtle.left(90);
	turtle.forward(50);
	turtle.right(90);
	turtle.forward(50);
	turtle.right(180);
	turtle.penup();
	turtle.sety(turtle.ycor() - 50);
	turtle.pendown();
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);
	turtle.left(90);
	turtle.forward(50);

def i():
	turtle.penup();
	turtle.setx(turtle.xcor() + 25);
	turtle.sety(turtle.ycor() - 50);
	turtle.pendown();
	turtle.left(90);
	turtle.forward(75);
	turtle.penup();
	turtle.sety(turtle.ycor() + 20);
	turtle.setx(turtle.xcor() - 2.5);
	turtle.pendown();
	turtle.forward(5);
	turtle.right(90);
	turtle.forward(5);
	turtle.right(90);
	turtle.forward(5);
	turtle.right(90);
	turtle.forward(5);
	turtle.right(180);


def space():
	turtle.penup();
	turtle.sety(0);
	turtle.setx(turtle.xcor() + 100);
	turtle.pendown();

def drawInput(inp):
	reset();
	for x in range(len(inp)):
		if (inp[x] == 'b'):
			b();
		elif (inp[x] == 'r'):
			r();
		elif (inp[x] == 'y'):
			y();
		elif (inp[x] == 'c'):
			c();
		elif (inp[x] == 'e'):
			e();
		elif (inp[x] == 'i'):
			i();
		space();


def drawAgain():
	inp = input("Do you wish to go again? (y/n)");
	if (inp == 'y'):
		return True;
	elif (inp == 'n'):
		return False;
	return False;

def reset():
	window.clear();
	turtle.penup();
	turtle.setx(-400);
	turtle.sety(0);
	turtle.pendown();

def main():
	keepGoing = True;
	while (keepGoing == True):
		inp = getProperInput();
		print("the entered input of %s was a proper use and will be printed.." %inp);
		drawInput(inp);
		keepGoing = drawAgain();


main();

window.listen();
window.mainloop();
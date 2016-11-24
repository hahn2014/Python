import turtle;
import math;

window = turtle.Screen();
my_turtle = turtle.Turtle();
keepGoing = True;

"""
#Function Name:		getProperInput()
#Description:		Get the input from the user, and send it through the input checking prior to returning the value
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	string must be less than or equal to 6 characters in length, and must be of the specific 6 usable chars
#Return:			returns the proper string input
"""
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

"""
#Function Name:		checkInputForChars()
#Description:		Checks if the inputed string follows the proper 6 usable characters
#Parameters:		inp as string for the input of the user
#Pre-Conditions:	inp must be a string
#Post-Conditions:	must return a boolean
#Return:			will return true if all characters in inp follows the 6 usable chars, returns false if one or more does not
"""
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

"""
#Function Name:		b()
#Description:		draws out a B with turtle
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		r()
#Description:		draws out a R with turtle
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		y()
#Description:		draws out a Y with turtle
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		c()
#Description:		draws out a C with turtle
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		e()
#Description:		draws out a E with turtle
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		i()
#Description:		draws out a I with turtle
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		space()
#Description:		resets turtle orientation and sets its x a distance away as a space
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
def space():
	turtle.penup();
	turtle.sety(0);
	turtle.setx(turtle.xcor() + 100);
	turtle.pendown();

"""
#Function Name:		drawInput()
#Description:		iterate through all the letters and call their specific draw functions
#Parameters:		inp as string from the users input
#Pre-Conditions:	inp must be a string
#Post-Conditions:	none
#Return:			none
"""
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

"""
#Function Name:		reset
#Description:		resets the board and the turtle for another draw sesh
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
def reset():
	window.clear();
	turtle.penup();
	turtle.setx(-400);
	turtle.sety(0);
	turtle.pendown();

def isOnTurtle(x, y):
	if (x >= turtle.xcor() - 10 and x <= turtle.xcor() + 10):
		if (y >= turtle.ycor() - 10 and y <= turtle.ycor() + 10):
			keepGoing = True;
	keepGoing = False;

"""
#Function Name:		main()
#Description:		function that keeps calling the user input and draw functions, untill the user chooces to stop drawing.
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
def main():
	while (keepGoing == True):
		reset();
		inp = getProperInput();
		print("the entered input of %s was a proper use and will be printed.." %inp);
		drawInput(inp);
		print("Click the turtle if you wish to draw another string, or close the window to quit.");
		turtle.onclick(isOnTurtle);


main();
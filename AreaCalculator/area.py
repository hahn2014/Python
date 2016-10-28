import sys;

"""
Name:			getFunctionType()
Description:	We will get an input from the user as an int telling us which function we are going to be using
Parameters:		No parameters
Preconditions:	We will start with good = false to ensure our input is a valid one!
PostConditions: We can only continue when good = true with good user input
Return:			Returns the function type as an integer from 1 to 5
"""	
def getFunctionType():
	good = False;
	while (good == False):
		print("Choose your function of choice:\n");
		print("1 -> Function 1 (x) = 5x^4+3x^3-10x+2\n2 -> Function 2 (x) = x^2-10\n3 -> Function 3 (x) = 40x+5\n4 -> Function 4 (x) = x^3\n5 -> Function 5 (x) = 20x^2 + 10x - 2");
		print("0 -> Quit");
		try:
			inp = (int)(input(">>"));
			if (inp == 1 or inp == 2 or inp == 3 or inp == 4 or inp == 5 or inp == 0):
				good = True;
			else:
				print("You did not enter a given option of 1, 2, 3, 4, 5, or 0!");
				good = False;
		except ValueError:
			print("You did not enter a proper function number...");
			good = False;
	if (inp == 0):
		print("Goodbye!");
		sys.exit();
	return (int)(inp);

"""
Name:			getShapeType()
Description:	We will get an input from the user as an int telling us which geometry shape we will use for the function x input
Parameters:		No parameters
Preconditions:	We will start with good = false to ensure our input is a valid one!
PostConditions: We can only continue when good = true with good user input
Return:			Returns the shape type as an integer from 1 to 3
"""	
def getShapeType():
	good = False;
	while (good == False):
		print("Would you like to calculate the area using the rectangle (1), trapezoid (2), or both (3)");
		try:
			inp = (int)(input(""));
			if (inp == 1 or inp == 2 or inp == 3):
				good = True;
			else:
				print("You did not enter a given option of 1, 2, or 3!");
				good = False;
		except ValueError:
			print("You did not enter a proper number...");
			good = False;
	return (int)(inp);


"""
Name:			getShapeCount()
Description:	We will get an input from the user as an int telling us how many of the desired shapes we will be using to calculate the area
Parameters:		kind as an integer telling the function if its a rectangle, trapezoid, or both (to get input twice)
Preconditions:	We will start with good = false to ensure our input is a valid one!
PostConditions: We can only continue when good = true with good user input
Return:			Returns the shape count as an integer above 0
"""	
def getShapeCount(kind):
	good = False;
	while (good == False):
		if (kind == 1): #for rectangles
			print("Enter how many Rectangles you want");
			try:
				inp = (int)(input(">>"));
				if (inp > 0):
					count = inp;
					count1 = -1;
					good = True;
				else:
					print("You entered a number bellow 1...");
					good = False;
			except ValueError:
				print("You did not enter a proper number...");
				good = False;
		elif (kind == 2): #for trapezoids
			print("Enter how many Trapezoids you want");
			try:
				inp = (int)(input(">>"));
				if (inp > 0):
					count = inp;
					count1 = -1;
					good = True;
				else:
					print("You entered a number bellow 1...");
					good = False;
			except ValueError:
				print("You did not enter a proper number...");
				good = False;
		elif (kind == 3): #for both
			print("Enter how many Rectangles and Trapezoids you want")
			try:
				inp = (int)(input("Rectangles>>"));
				if (inp > 0):
					count = inp;
					good = True;
				else:
					print("You entered a number bellow 1...");
					good = False;
				inp = (int)(input("Trapezoids>>"));
				if (inp > 0):
					count1 = inp;
					good = True;
				else:
					print("You entered a number bellow 1...");
					good = False;
			except ValueError:
				print("You did not enter a proper number...");
				good = False;
	return [count, count1];

"""
Name:			getStartingPoint()
Description:	We will get an input from the user as an int telling us where on the x-axis the area calculation will start
Parameters:		No parameters
Preconditions:	We will start with good = false to ensure our input is a valid one!
PostConditions: We can only continue when good = true with good user input
Return:			Returns the starting point as an float from [-∞, ∞] (can be anywhere between a integer too/float)
"""	
def getStartingPoint():
	good = False;
	while (good == False): # starting point
		print("Enter the starting point");
		try:
			inp = (float)(input(">>"));
		except ValueError:
			print("You did not enter a proper number...");
			good = False;
		good = True;
	return (float)(inp);

"""
Name:			getEndingPoint()
Description:	We will get an input from the user as an int telling us where on the x-axis the area calculation will end
Parameters:		start as an integer so we know where the start of the number line is
Preconditions:	We will start with good = false to ensure our input is a valid one!
PostConditions: We can only continue when good = true with good user input
Return:			Returns the ending point as an float from (start, ∞] (can be anywhere between a integer too/float)
"""	
def getEndingPoint(start):
	good = False;
	while (good == False): #ending point
		print("Enter the ending point");
		try:
			inp = (float)(input(">>"));
			if (inp > start):
				good = True;0
			else:
				print("You entered a number bellow or equal to the starting point, this doesn't work...");
				good = False;
		except ValueError:
			print("You did not enter a proper number...");
			good = False;
	return (float)(inp);

"""
Name:			f1()
Description:	Input current shape into the function to recive the height of the shape on the number line
Parameters:		x a float to be plugged into the equation
Preconditions:	x must be a valid number
PostConditions: No post conditions
Return:			Returns the height of the shape from the input of the function
"""	
def f1(x):
	return (5 * (x ** 4)) + (3 * (x ** 3)) - (10 * x) + 2;

"""
Name:			f2()
Description:	Input current shape into the function to recive the height of the shape on the number line
Parameters:		x a float to be plugged into the equation
Preconditions:	x must be a valid number
PostConditions: No post conditions
Return:			Returns the height of the shape from the input of the function
"""	
def f2(x):
	return (x ** 2) - 10;

"""
Name:			f3()
Description:	Input current shape into the function to recive the height of the shape on the number line
Parameters:		x a float to be plugged into the equation
Preconditions:	x must be a valid number
PostConditions: No post conditions
Return:			Returns the height of the shape from the input of the function
"""	
def f3(x):
	return (40 * x) + 5;

"""
Name:			f4()
Description:	Input current shape into the function to recive the height of the shape on the number line
Parameters:		x a float to be plugged into the equation
Preconditions:	x must be a valid number
PostConditions: No post conditions
Return:			Returns the height of the shape from the input of the function
"""	
def f4(x):
	return (x ** 3);

"""
Name:			f5()
Description:	Input current shape into the function to recive the height of the shape on the number line
Parameters:		x a float to be plugged into the equation
Preconditions:	x must be a valid number
PostConditions: No post conditions
Return:			Returns the height of the shape from the input of the function
"""	
def f5(x):
	return (20 * (x ** 2)) + (10 * x) - 2;

"""
Name:			calculateArea()
Description:	iterate through n number of shapes calling the desired equation to plug x value into each iteration, the adding the current area to the total
Parameters:		function as the function type to use, kind as the shape used, start as the point on the x-axis to start from, end as the point on the x-axis to end at, count as the n number of shapes
Preconditions:	all inputs must be valid numbers
PostConditions: No post conditions
Return:			Returns the total calculated area from the iteration of functions
"""	
def calculateArea(function, kind, start, end, count):
	area = [0, 0];

	if (kind == 1):
		n = count[0];
		w = (end - start) / n;
		areaTotal = 0;
		x = start;
		
		for i in range(n):
			if (function == 1):
				h = f1(x);
			elif (function == 2):
				h = f2(x);
			elif (function == 3):
				h = f3(x);
			elif (function == 4):
				h = f4(x);
			elif (function == 5):
				h = f5(x);
			
			areaTotal += (w * h);
			x += w;
			#print("w:%s h:%s x:%s area:%s total:%s" %(w, h, x, (w*h), areaTotal));

		area = areaTotal;


	elif (kind == 2):
		n = count[0];
		w = (end - start) / n;
		areaTotal = 0;
		x = start;
		x1 = start + w;
		
		for i in range(n):
			if (function == 1):
				h = f1((x + x1) / 2);
			elif (function == 2):
				h = f2((x + x1) / 2);
			elif (function == 3):
				h = f3((x + x1) / 2);
			elif (function == 4):
				h = f4((x + x1) / 2);
			elif (function == 5):
				h = f5((x + x1) / 2);
			
			areaTotal += (w * h);
			x += w;
			x1 += w;
			#print("w:%s h:%s x:%s area:%s total:%s" %(w, h, x, (w*h), areaTotal));

		area = areaTotal;

	return area;

"""
Name:			runAgain()
Description:	We will get an input from the user as an int telling us if we want to run another area calculation, or quit the program
Parameters:		no parameters
Preconditions:	We will start with good = false to ensure our input is a valid one!
PostConditions: We can only continue when good = true with good user input
Return:			Returns true if user wants to run again, or false to quit
"""	
def runAgain():
	print("Do you wish to run another area calculation [1], or quit [0]");
	good = False;
	while (good == False):
		try:
			inp = (int)(input(">>"));
			if (inp == 1 or inp == 0):
				good = True;
			else:
				print("You did not enter a proper value of 0 or 1...");
				good = False;
		except ValueError:
			print("You did not enter a proper digit...");
			good = False;
	if (inp == 1):
		return True;
	elif (inp == 0):
		return False;

"""
Name:			main()
Description:	main loop called once that gets all the functions for inputs and calculations 
Parameters:		no parameters
Preconditions:	No pre conditions
PostConditions: No post conditions
Return:			No return values
"""	
def main():
	running = True;
	while (running == True):
		print("Welcome to Bryce Hahn's Area Calculator!");
		function 	= getFunctionType();
		shape 		= getShapeType();
		count 		= getShapeCount(shape);
		startPoint  = getStartingPoint();
		endPoint 	= getEndingPoint(startPoint);

		printMethods(function, shape, startPoint, endPoint, count);

		running = runAgain();

"""
Name:			runAgain()
Description:	Prints the proper line(s) of output telling the user what function he called, the values entered and the calculated area output.
Parameters:		function as the function type to use, kind as the shape used, start as the point on the x-axis to start from, end as the point on the x-axis to end at, count as the n number of shapes
Preconditions:	All inputs must be a proper number value
PostConditions: No post conditions
Return:			No Return value
"""	
def printMethods(function, kind, start, end, count):
	if (function == 1):
		if (kind == 1):
			print("The area under f(x)=5x^4+3x^3-10x+2 between %s and %s through %s rectangles is %s" 	%(start, end, count[0], calculateArea(function, 1, start, end, count)));
		elif (kind == 2):
			print("The area under f(x)=5x^4+3x^3-10x+2 between %s and %s through %s trapezoids is %s" 	%(start, end, count[0], calculateArea(function, 2, start, end, count)));
		elif (kind == 3):
			print("The area under f(x)=5x^4+3x^3-10x+2 between %s and %s through %s rectangles is %s" 	%(start, end, count[0], calculateArea(function, 1, start, end, count)));
			print("The area under f(x)=5x^4+3x^3-10x+2 between %s and %s through %s trapezoids is %s" 	%(start, end, count[1], calculateArea(function, 2, start, end, count)));
	elif (function == 2):
		if (kind == 1):
			print("The area under f(x)=x^2-10 between %s and %s through %s rectangles is %s" 			%(start, end, count[0], calculateArea(function, 1, start, end, count)));
		elif (kind == 2):
			print("The area under f(x)=x^2-10 between %s and %s through %s trapezoids is %s" 			%(start, end, count[0], calculateArea(function, 2, start, end, count)));
		elif (kind == 3):
			print("The area under f(x)=x^2-10 between %s and %s through %s rectangles is %s" 			%(start, end, count[0], calculateArea(function, 1, start, end, count)));
			print("The area under f(x)=x^2-10 between %s and %s through %s trapezoids is %s" 			%(start, end, count[1], calculateArea(function, 2, start, end, count)));
	elif (function == 3):
		if (kind == 1):	
			print("The area under f(x)=40x+5 between %s and %s through %s rectangles is %s" 			%(start, end, count[0], calculateArea(function, 1, start, end, count)));
		elif (kind == 2):
			print("The area under f(x)=40x+5 between %s and %s through %s trapezoids is %s" 			%(start, end, count[0], calculateArea(function, 2, start, end, count)));
		elif (kind == 3):
			print("The area under f(x)=40x+5 between %s and %s through %s rectangles is %s" 			%(start, end, count[0], calculateArea(function, 1, start, end, count)));
			print("The area under f(x)=40x+5 between %s and %s through %s trapezoids is %s" 			%(start, end, count[1], calculateArea(function, 2, start, end, count)));
	elif (function == 4):
		if (kind == 1):
			print("The area under f(x)=x^3 between %s and %s through %s rectangles is %s" 				%(start, end, count[0], calculateArea(function, 1, start, end, count)));
		elif (kind == 2):
			print("The area under f(x)=x^3 between %s and %s through %s trapezoids is %s" 				%(start, end, count[0], calculateArea(function, 2, start, end, count)));
		elif (kind == 3):
			print("The area under f(x)=x^3 between %s and %s through %s rectangles is %s" 				%(start, end, count[0], calculateArea(function, 1, start, end, count)));
			print("The area under f(x)=x^3 between %s and %s through %s trapezoids is %s" 				%(start, end, count[1], calculateArea(function, 2, start, end, count)));
	elif (function == 5):
		if (kind == 1):
			print("The area under f(x)=20x^2+10x-2 between %s and %s through %s rectangles is %s" 		%(start, end, count[0], calculateArea(function, 1, start, end, count)));
		elif (kind == 2):
			print("The area under f(x)=20x^2+10x-2 between %s and %s through %s trapezoids is %s" 		%(start, end, count[0], calculateArea(function, 2, start, end, count)));
		elif (kind == 3):
			print("The area under f(x)=20x^2+10x-2 between %s and %s through %s rectangles is %s" 		%(start, end, count[0], calculateArea(function, 1, start, end, count)));
			print("The area under f(x)=20x^2+10x-2 between %s and %s through %s trapezoids is %s"		%(start, end, count[1], calculateArea(function, 2, start, end, count)));

main();

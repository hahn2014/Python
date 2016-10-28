import sys;

print("\n\n\nWelcome to Bryce Hahn's python calculator program\nFor basic Calculations [1]\nFor advanced Calculations [2]\nFor Equations [3]\n\n");

try:
	inp = (int)(input(">>"));
except ValueError:
	print("Improper input...");

if (inp == 1):
	#use the simple calculator with only +, -, *, /, and ^
	print("\n\nWelcome to the basic calculator. Please enter a single operator. (+, -, *, /, ^)");
	good = False;
	while (good == False):
		inp = '';
		while (len(inp) != 1):
			inp = input(">>");
			if (len(inp) == 1):
				break;
			print("Please enter only one character");
			
		if (inp == '+' or inp == '-' or inp == '*' or inp == '/' or inp == '^'):
			operator = inp;
			good = True;
		else:
			print("You did not enter a proper symbol...");
			good = False;
	a = 0; b = 0; good = False;
	while (good == False):
		print("Please enter the 1st number of the equation");
		try:
			a = (float)(input(">>"));
			good = True;
		except ValueError:
			print("You did not enter a proper number...");
			good = False;
	good = False;
	while (good == False):
		print("Please enter the 2nd number of the equation");
		try:
			b = (float)(input(">>"));
			good = True;
		except ValueError:
			print("You did not enter a proper number...");
			good = False;
	print("Equation: %s%s%s" %(a, operator, b));
	
	if (operator == "+"):
		print("Result  : %" %((float)(a) + (float)(b)));
	elif (operator == "-"):
		print("Result  : %" %((float)a - (float)b));
	elif (operator == "*"):
		print("Result  : %" %((float)a * (float)b));
	elif (operator == "/"):
		print("Result  : %" %((float)a / (float)b));
	elif (operator == "^"):
		print("Result  : %" %((float) a ** (float)b));
	else:
		print("Shit went wrong...");
elif (inp == 2):
	#use the advanced calculator with sin, cos, tan, and square root
	print("\n\nWelcome to the advanced calculator.\nFor SIN [1]\nFor COS [2]\nFor TAN [3]\nFor Square Root [4]");
	
	
	
	
	
	
	
	
	
	
elif (inp == 3):
	#allow brackets and multiple simple calculations into one calculation.
	print("\n\nWelcome to advanced calculator equation.\nEnter a equation with Brackets and multiple simple calculations.");
	
	
	
	
	
	
	
	
elif (inp == 4):
	print("Goodbye!");
	sys.exit();
else:
	print("This was not a proper option...");
	sys.exit();

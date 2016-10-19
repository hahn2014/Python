import sys;
conti = 1;
while (conti == 1):
	cont = 0;
	print("\n\n\n\nWelcome to Bryce Hahn's Python Calculator!\nFor Programming Mode, enter [1]");
	print("For Scientific Mode, enter [2]");
	print("To Quit, enter [3]");
	while (cont == 0):
		try:
			inp = (int)(input(">>"));
			cont = 1;
		except:
			print("You did not input a proper value of 1, 2, or 3...");
			cont = 0;
	
	if (inp == 2): #python calculator...
		cont = 1;
		operator = '';
		a = '';
		b = '';
		
		while (cont == 1):
			good = 0;
			while (good == 0):
				inp = '';
				while (len(inp) != 1):
					inp = input("Input a operating symbol (+, -, *, /, ^)\n>>");
					if (len(inp) == 1):
						break;
					print("Please enter only one character");
					
				if (inp == '+' or inp == '-' or inp == '*' or inp == '/' or inp == '^'):
					operator = inp;
					good = 1;
				else:
					print("You did not enter a proper symbol of (+, -, *, /, ^)");
					good = 0;
			
			print("\nPlease enter the first number of the problem (a) EX: a*b=...");
			good = 0;
			while (good == 0):
				try:
					inp = (float)(input(">>"));
					good = 1;
				except:
					print("You did not enter a proper decimal...");
					good = 0;
			a = inp;
			
			print("\nPlease enter the second number of the problem (b) EX: a*b=...");
			good = 0;
			while (good == 0):
				try:
					inp = (float)(input(">>"));
					good = 1;
				except:
					print("You did not enter a proper decimal...");
					good = 0;
			b = inp;
			
			print("\n\nequation ->   %s%s%s" %(a, operator, b));
			
			if (operator == '+'):
				print("result -> %s\n\n" %((float)(a) + (float)(b)));
			elif (operator == '-'):
				print("result -> %s\n\n" %((float)(a) - (float)(b)));
			elif (operator == '*'):
				print("result -> %s\n\n" %((float)(a) * (float)(b)));
			elif (operator == '/'):
				print("result -> %s\n\n" %((float)(a) / (float)(b)));
			elif (operator == '^'):
				print("result -> %s\n\n" %((float)(a) ** (float)(b)));
			else:
				print("This shouldn't have been called, clossing");
				sys.exit();
			#ask to run again infinite loop..
			try:
				inp = (int)(input("\n\nDo you wish to calculate another problem [1]\nSwitch to a different mode [2]\nOr quit? [3]"));
			except:
				print("The entered value was not a proper decimal...");
				sys.exit();
			if (inp == 1):
				cont = 1;
			elif (inp == 2):
				cont = 0;
				conti = 1;
			elif (inp == 3):
				cont = 0;
				conti = 0;
				print("Goodbye!");
				sys.exit();
			else:
				print("Inproper value...");
	elif (inp == 1): #decimal to binary conversion...
		cont = 0;
		while (cont == 0):
			print("\n\nFor converting Binary to Decimal [1]\nFor converting Decimal to Binary [2]");
			try:
				inp = (int)(input(">>"));
				cont = 1;
			except:
				print("You did not enter a value of 1, or 2...");
				cont = 0;
			if (inp == 1): #binary to decimal
				while (cont == 1):
					inp = input("\n\nInput a binary (base 2) to be converted to (base 10) decimal format\n");
					try:
						converted = (int)(inp, 2);
						cont = 0;
					except ValueError:
						print("You did not enter a proper binary...");
						cont = 1;
				print("The entered input of %s is a proper binary string" %inp);
				num = 0;
				for x in range(len(inp)):
					if (inp[x] == '1'):
						num += pow(2, len(inp)-x-1);
					elif (inp[x] == '0'):
						num += 0;
					else:
						print("IDK");
					#if ((int)(str(inp.index(inp, x))) == 1):
						#add to the final
					#	print("%s fits into out number." %(pow(2, len(inp)-x)));
					#	num += pow(2, (len(inp)-x));
					
				print("\n\n\nfinal number -> %s | %s\n" %(num, converted));



			elif (inp == 2): #decimal to binary
				while (cont == 1):
					inp = input("\n\nInput a decimal (base 10) to be converted to (base 2) binary format:\n");
					try:
						converted = (int)(inp);
						cont = 0;
					except:
						print("You did not enter a proper decimal...");
						cont = 1;
					if (converted < 0):
						print("The entered value was bellow 0...");
						cont = 1;
					print("User entered a proper value of %s" %inp);
				returnmemory = "";
				leadingOne = 0;
				for x in range(100, -1, -1):
					power = pow(2, x);
					#print("checking if %s goes into %s." %(power, converted));
					if (converted - power >= 0):
						returnmemory += "1";
						converted -= power;
						leadingOne = 1;
					else:
						if (leadingOne == 1):
							returnmemory += "0";
				print("\n\n\nfinal conversion: %s\n" %returnmemory);
			#ask to run again infinite loop..
			try:
				inp = (int)(input("\n\nDo you wish to convert another number [1]\nSwitch to a different mode [2]\nOr quit? [3]"));
			except:
				print("the entered value was not a proper decimal...");
				sys.exit();
			if (inp == 1):
				cont = 0;
			elif (inp == 2):
				cont = 1;
				conti = 1;
			elif (inp == 3):
				cont = 1;
				conti = 0;
				print("Goodbye!");
				sys.exit();
			else:
				print("Inproper value...");
				sys.exit();
	elif (inp == 3):
		print("Sorry you did not want to use this awesome program! Goodbye");
		sys.exit();
	else:
		print("You entered an inproper input..");
		sys.exit();



import sys;
"""
#Function Name:		drawBoard()
#Description:		Redraw the game board with the new X and O plays showing current players turn
#Parameters:		board as values of the board positions, curPlayer as the currently active player
#Pre-Conditions:	board must be a string list, curPlayer must be an int of 1 or 0
#Post-Conditions:	none
#Return:			none
"""
def drawBoard(board, curPlayer):
	print("\n\nCurrent Player's Turn: %s" %("X" if curPlayer == 0 else "O"));
	print("╔═══╦═══╦═══╗");
	print("║ %s ║ %s ║ %s ║" %(board[0], board[1], board[2]));
	print("╠═══╬═══╬═══╣");
	print("║ %s ║ %s ║ %s ║" %(board[3], board[4], board[5]));
	print("╠═══╬═══╬═══╣");
	print("║ %s ║ %s ║ %s ║" %(board[6], board[7], board[8]));
	print("╚═══╩═══╩═══╝");

"""
#Function Name:		getPlayerCount()
#Description:		input how many players the player would like to start with
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	number of players must be 1 or 2
#Return:			return inp as integer
"""
def getPlayerCount():
	good = False;
	while (good == False):
		print("Welcome to Bryce Hahn's Tic Tac Toe Game! How many players are we playing with? (1 to play against AI, 2 to take turns)");
		try:
			inp = (int)(input(">>"));
			if (inp == 1 or inp == 2):
				good = True;
		except:
			print("You did not enter a proper integer as input");
	return inp;

"""
#Function Name:		getPlayerMove()
#Description:		get the user input for the current play and validate that it was within the board and has not been played before..
#Parameters:		board as values of the board positions, curPlayer as the currently active player
#Pre-Conditions:	board must be a string list, curPlayer must be an int of 1 or 0
#Post-Conditions:	inp must be an integer between 1 and 9
#Return:			inp as integer for the users choice of move
"""
def getPlayerMove(board, curPlayer):
	good = False;
	while (good == False):
		print("\n%s's Turn, Please enter which box you would like to place your move in." %("X" if curPlayer == 0 else "O"));
		try:
			inp = (int)(input(">>"));
			if (inp == 1 or inp == 2 or inp == 3 or inp == 4 or inp == 5 or inp == 6 or inp == 7 or inp == 8 or inp == 9):
				if (validMove(board, inp)):
					good = True;
				else:
					print("\nYou did not enter a valid move, %s has already been used.." %(inp));
			else:
				print("\nYou did not enter a proper board value between 1 and 9!");
		except ValueError:
			print("\nYou did not enter a proper decimal integer input for the board position!");
	return inp;

"""
#Function Name:		validMove()
#Description:		ensure that the user can actually play at the desired spot and it has not been played on before
#Parameters:		board as values of the board positions, move as the desired spot the user wishes to play on
#Pre-Conditions:	board must be a string list, move must be an integer
#Post-Conditions:	return must be a boolean
#Return:			return true if you can play at move, false if you can not
"""
def validMove(board, move):
	if (board[move - 1] == "X" or board[move - 1] == "O"): #this spot has already been filled by the x or o player
		return False;
	else: #this spot is still a number, so it's empty
		return True;

"""
#Function Name:		updateBoard()
#Description:		update board with the new move from the current player
#Parameters:		move as the desired spot the user wishes to play on, curPlayer as the current player, board as values of the board positions
#Pre-Conditions:	move must be an integer, curPlayer must be an integer, board must be a list of strings
#Post-Conditions:	return must be a board list of string
#Return:			return board with the updated play spot
"""
def updateBoard(move, curPlayer, board):
	if (curPlayer == 0): #0 == X
		board[move - 1] = "X";
	else:
		board[move - 1] = "O";
	return board;

"""
#Function Name:		switchPlayers()
#Description:		switch between player 1 and 2
#Parameters:		curPlayer as the current players index
#Pre-Conditions:	curPlayer must be an integer of 1 or 2
#Post-Conditions:	return must be the oposite value of the input
#Return:			return curPlayer as integer
"""
def switchPlayers(curPlayer):
	if (curPlayer == 0):
		curPlayer = 1;
	else:
		curPlayer = 0;
	return curPlayer;

"""
#Function Name:		getAIMove()   - BASIC AI CALL
#Description:		The ai play method, will only look for the first opened place on the board and choose said spot as the play move
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns place as an integer between 1 and 9
#Return:			return the ai's move
"""
def getAIMove(board):
	place = 0;
	for x in range(len(board)):
		if not (board[x] == "X" or board[x] == "O"): #if the current spot on the board is unplayed, ai will go here
			place = x + 1;
			break;
	return place;




####################   ~~ ADVANCED AI DEFENSE  ~~   ####################


"""
#Function Name: 	getAIMoveAdvanced()   - ADVANCED AI CALL
#Description:		the ai play method, will first check for defending the win, then will attack for 
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return must be an integer for the ai move
#Return:			returns the value for the AI
"""
def getAIMoveAdvanced(board):
	#first check for any way to avoid X from winning (2 in a row, block the 3rd spot)
	place = checkForPotentialLoss(board);
	print("AI Will play at %s as defense" %place);
	#now check for an open spot for us to keep playing to attempt a 3 in a row
	if (place == 0):
		place = checkForBestAIMove(board);
		print("AI had no need to defend, we will attack at %s" %place);
	return place;

########################
#	horizontal check   #
########################

"""
#Function Name:		HorizRow1()
#Description:		Checks the top row for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def HorizRow1(board):
	if (board[0] == "1" and board[1] == "X" and board[2] == "X"): 
		return 1;
	elif (board[0] == "X" and board[1] == "2" and board[2] == "X"):
		return 2;
	elif (board[0] == "X" and board[1] == "X" and board[2] == "3"):
		return 3;
	return 0;

"""
#Function Name:		HorizRow2()
#Description:		Checks the middle row for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def HorizRow2(board):
	if (board[3] == "4" and board[4] == "X" and board[5] == "X"): 
		return 4;
	elif (board[3] == "X" and board[4] == "5" and board[5] == "X"):
		return 5;
	elif (board[3] == "X" and board[4] == "X" and board[5] == "6"):
		return 6;
	return 0;

"""
#Function Name:		HorizRow3()
#Description:		Checks the bottom row for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def HorizRow3(board):
	if (board[6] == "7" and board[7] == "X" and board[8] == "X"): 
		return 7;
	elif (board[6] == "X" and board[7] == "8" and board[8] == "X"):
		return 8;
	elif (board[6] == "X" and board[7] == "X" and board[8] == "9"):
		return 9;
	return 0;

"""
#Function Name:		checkHorizForLoss()
#Description:		calls all the horizontal line checks to ensure there are no 2 in a rows for X
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def checkHorizForLoss(board):
	move = HorizRow1(board);
	
	if (move == 0):
		move = HorizRow2(board);

	if (move == 0):
		move = HorizRow3(board);
	return move;


########################
#	 vertical check    #
########################

"""
#Function Name:		VertCol1()
#Description:		Checks the left column for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def VertCol1(board):
	if (board[0] == "1" and board[3] == "X" and board[6] == "X"): 
		return 1;
	elif (board[0] == "X" and board[3] == "4" and board[6] == "X"):
		return 4;
	elif (board[0] == "X" and board[3] == "X" and board[6] == "7"):
		return 7;
	return 0;

"""
#Function Name:		VertCol2()
#Description:		Checks the middle column for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def VertCol2(board):
	if (board[1] == "2" and board[4] == "X" and board[7] == "X"): 
		return 2;
	elif (board[1] == "X" and board[4] == "5" and board[7] == "X"):
		return 5;
	elif (board[1] == "X" and board[4] == "X" and board[7] == "8"):
		return 8;
	return 0;

"""
#Function Name:		VertCol3()
#Description:		Checks the right column for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def VertCol3(board):
	if (board[2] == "3" and board[5] == "X" and board[8] == "X"): 
		return 3;
	elif (board[2] == "X" and board[5] == "6" and board[8] == "X"):
		return 6;
	elif (board[2] == "X" and board[5] == "X" and board[8] == "9"):
		return 9;
	return 0;

"""
#Function Name:		checkVertForLoss()
#Description:		calls all the vertical line checks to ensure there are no 2 in a rows for X
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def checkVertForLoss(board):
	move = VertCol1(board);
	
	if (move == 0):
		move = VertCol2(board);

	if (move == 0):
		move = VertCol3(board);
	return move;


########################
#	 diagonal check    #
########################

"""
#Function Name:		DiagLine1()
#Description:		Checks the left to right diagonal for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def DiagLine1(board):
	if (board[0] == "1" and board[4] == "X" and board[8] == "X"): 
		return 1;
	elif (board[0] == "X" and board[4] == "5" and board[8] == "X"):
		return 5;
	elif (board[0] == "X" and board[4] == "X" and board[8] == "9"):
		return 9;
	return 0;

"""
#Function Name:		DiagLine2()
#Description:		Checks the right to left diagonal for 2 in a row to prevent x from winning
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def DiagLine2(board):
	if (board[2] == "3" and board[4] == "X" and board[6] == "X"): 
		return 3;
	elif (board[2] == "X" and board[4] == "5" and board[6] == "X"):
		return 5;
	elif (board[2] == "X" and board[4] == "X" and board[6] == "7"):
		return 7;
	return 0;

"""
#Function Name:		checkDiagForLoss()
#Description:		calls all the diagonal line checks to ensure there are no 2 in a rows for X
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def checkDiagForLoss(board):
	move = DiagLine1(board);

	if (move == 0):
		move = DiagLine2(board);
	return move;

"""
#Function Name:		checkForPotentialLoss()
#Description:		calls all the methods to ensure there are no 2 in a rows for columns, rows, and diagonals
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns as integer
#Return:			returns the deffense positions
"""
def checkForPotentialLoss(board):
	#check for horizontal potentials
	place = checkHorizForLoss(board);
	#check for vertical potentials
	if (place == 0): #if place isn't 0, we found a spot we need to cover
		place = checkVertForLoss(board);
	#check for diagonal potentials
	if (place == 0): #if place is still 0, then check the diagonals.
		place = checkDiagForLoss(board);
	return place;






####################   ~~ ADVANCED AI ATTACKING  ~~   ####################

########################
#	horizontal check   #
########################

"""
#Function Name:		horizRow1()
#Description:		checks the top horizontal row for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def horizRow1(board):
	if (board[0] == "X" and board[1] == "2" and board[2] == "3"):
		return 3;
	elif (board[0] == "1" and board[1] == "X" and board[2] == "3"):
		return 1;
	elif (board[0] == "1" and board[1] == "2" and board[2] == "X"):
		return 1;
	elif (board[0] == "1" and board[1] == "2" and board[2] == "3"): #nothing on this row
		return 3;
	return 0;

"""
#Function Name:		horizRow2()
#Description:		checks the middle horizontal row for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def horizRow2(board):
	if (board[3] == "X" and board[4] == "5" and board[5] == "6"):
		return 6;
	elif (board[3] == "4" and board[4] == "X" and board[5] == "6"):
		return 4;
	elif (board[3] == "4" and board[4] == "5" and board[5] == "X"):
		return 4;
	elif (board[3] == "4" and board[4] == "5" and board[5] == "6"): #nothing on this row
		return 5;
	return 0;

"""
#Function Name:		horizRow2()
#Description:		checks the bottom horizontal row for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def horizRow3(board):
	if (board[6] == "X" and board[7] == "8" and board[8] == "9"):
		return 9;
	elif (board[6] == "7" and board[7] == "X" and board[8] == "9"):
		return 7;
	elif (board[6] == "7" and board[7] == "8" and board[8] == "X"):
		return 7;
	elif (board[6] == "7" and board[7] == "8" and board[8] == "9"): #nothing on this row
		return 7;
	return 0;

"""
#Function Name:		checkHorizForAttack()
#Description:		calls all the horizontal line checks for the best possible move
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def checkHorizForAttack(board):
	move = horizRow1(board);

	if (move == 0):
		move = horizRow2(board);

	if (move == 0):
		move = horizRow3(board);
	return move;

########################
#	 vertical check    #
########################

"""
#Function Name:		vertCol1()
#Description:		checks the left vertical row for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def vertCol1(board):
	if (board[0] == "X" and board[3] == "4" and board[6] == "7"):
		return 7;
	elif (board[0] == "1" and board[3] == "X" and board[6] == "7"):
		return 1;
	elif (board[0] == "1" and board[3] == "4" and board[6] == "X"):
		return 1;
	elif (board[0] == "1" and board[3] == "4" and board[6] == "7"): #nothing on this row
		return 4;
	return 0;

"""
#Function Name:		vertCol2()
#Description:		checks the middle vertical row for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def vertCol2(board):
	if (board[1] == "X" and board[4] == "5" and board[7] == "8"):
		return 8;
	elif (board[1] == "2" and board[4] == "X" and board[7] == "8"):
		return 2;
	elif (board[1] == "2" and board[4] == "5" and board[7] == "X"):
		return 2;
	elif (board[1] == "2" and board[4] == "5" and board[7] == "8"): #nothing on this row
		return 4;
	return 0;

"""
#Function Name:		vertCol3()
#Description:		checks the right vertical row for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def vertCol3(board):
	if (board[2] == "X" and board[5] == "6" and board[8] == "9"):
		return 9;
	elif (board[2] == "3" and board[5] == "X" and board[8] == "9"):
		return 3;
	elif (board[2] == "3" and board[5] == "6" and board[8] == "X"):
		return 3;
	elif (board[2] == "3" and board[5] == "6" and board[8] == "9"): #nothing on this row
		return 6;
	return 0;

"""
#Function Name:		checkVertForAttack()
#Description:		calls all the vertical line checks for the best possible move
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def checkVertForAttack(board):
	move = vertCol1(board);

	if (move == 0):
		move = vertCol2(board);

	if (move == 0):
		move = vertCol3(board);
	return move;


########################
#	 diagonal check    #
########################

"""
#Function Name:		diagLine1()
#Description:		checks the left to right diagonal line for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def diagLine1(board):
	if (board[0] == "X" and board[4] == "5" and board[8] == "9"): 
		return 9;
	elif (board[0] == "1" and board[4] == "X" and board[8] == "9"):
		return 1;
	elif (board[0] == "1" and board[4] == "5" and board[8] == "X"):
		return 1;
	elif (board[0] == "1" and board[4] == "5" and board[8] == "9"):
		return 5;
	return 0;

"""
#Function Name:		diagLine2()
#Description:		checks the right to left diagonal line for the best possible move to play
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def diagLine2(board):
	if (board[2] == "X" and board[4] == "5" and board[6] == "7"): 
		return 7;
	elif (board[2] == "3" and board[4] == "X" and board[6] == "7"):
		return 3;
	elif (board[2] == "3" and board[4] == "5" and board[6] == "X"):
		return 3;
	elif (board[2] == "3" and board[4] == "5" and board[6] == "7"):
		return 5;
	return 0;

"""
#Function Name:		checkDiagForAttack()
#Description:		calls all the diagonal line checks for the best possible move
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def checkDiagForAttack(board):
	move = DiagLine1(board);

	if (move == 0):
		move = DiagLine2(board);
	return move;


"""
#Function Name:		checkForBestMove()
#Description:		calls all the methods to ensure for the best possible move
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	return as integer between 1 and 9
#Return:			returns the attack position
"""
def checkForBestAIMove(board):
	#check for horizontal best
	place = checkHorizForAttack(board);
	#check for vertical best
	if (place == 0):
		place = checkVertForAttack(board);
	#check for diagonal best
	if (place == 0):
		place = checkDiagForAttack(board);
	return place;
	

"""
#Function Name: 	getMove()
#Description:		tests what the current player is and gets the input based on that, aswell checks if the AI should play a move
#Parameters:		board as a list of move positions, curPlayer as the current players value, players as the number of players playing
#Pre-Conditions:	board must be a full list of positions, curPlayer must be an integer of 1 or 0, players must be an integer of 1 or 2
#Post-Conditions:	move must be a integer between the designated post-conditions from the respective return statements
#Return:			returns move as the next move for the current player
"""
def getMove(board, curPlayer, players):
	if (curPlayer == 0): #x will always be user input
		move = getPlayerMove(board, curPlayer);
	else: #o will be ai controlled while playing as 1 player
		if (players == 2): #2 players, user input
			move = getPlayerMove(board, curPlayer);
		else:
			move = getAIMoveAdvanced(board); #getAIMove(board); #getAIMove() will not win
	return move;

"""
#Function Name: 	checkHoriz()
#Description:		checks for a match of 3 in a row horizontally on each line, ie: 1, 2, 3; 4, 5, 6; 7, 8, 9
#Parameters:		board as a list of move positions, curPlayer as the current players value
#Pre-Conditions:	board must be a full list of positions, curPlayer must be an integer of 1 or 0
#Post-Conditions:	must return a boolean
#Return:			returns true if there was a 3 in a row match, false if all 3 rows failed
"""
def checkHoriz(board, curPlayer):
	if (curPlayer == 1):
		p = "X";
	else:
		p = "O";

	if (board[0] == p and board[1] == p and board[2] == p):
		return True;
	elif (board[3] == p and board[4] == p and board[5] == p):
		return True;
	elif (board[6] == p and board[7] == p and board[8] == p):
		return True;
	else:
		return False;

"""
#Function Name: 	checkVert()
#Description:		checks for a match of 3 in a row vertically on each line, ie: 1,4,7; 2,5,8; 3,6,9
#Parameters:		board as a list of move positions, curPlayer as the current players value
#Pre-Conditions:	board must be a full list of positions, curPlayer must be an integer of 1 or 0
#Post-Conditions:	must return a boolean
#Return:			returns true if there was a 3 in a row match, false if all 3 rows failed
"""
def checkVert(board, curPlayer):
	if (curPlayer == 1):
		p = "X";
	else:
		p = "O";
	if (board[0] == p and board[3] == p and board[6] == p):
		return True;
	elif (board[1] == p and board[4] == p and board[7] == p):
		return True;
	elif (board[2] == p and board[5] == p and board[8] == p):
		return True;
	else:
		return False;

"""
#Function Name: 	checkDiag()
#Description:		checks for a match of 3 in a row diagonally for both lines, ie: 1,5,9; 7,4,3
#Parameters:		board as a list of move positions, curPlayer as the current players value
#Pre-Conditions:	board must be a full list of positions, curPlayer must be an integer of 1 or 0
#Post-Conditions:	must return a boolean
#Return:			returns true if there was a 3 in a row match, false if all 3 rows failed
"""
def checkDiag(board, curPlayer):
	if (curPlayer == 1):
		p = "X";
	else:
		p = "O";
	if (board[0] == p and board[4] == p and board[8] == p):
		return True;
	elif (board[6] == p and board[4] == p and board[2] == p):
		return True;
	else:
		return False;

"""
#Function Name: 	getSpotsLeft()
#Description:		returns how many possible moves remain on the board, if it returns 0, then there are no spaces left
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns an integer from 0 to 8
#Return:			returns the number of spots available for a potential play
"""
def getSpotsLeft(board):
	left = 0;
	for x in range(len(board)):
		if (board[x] == str(x + 1)):
			left += 1;
	return left;

"""
#Function Name: 	checkWin()
#Description:		calls all the check methods to check for any 3 in a row for both X and O
#Parameters:		board as a list of move positions
#Pre-Conditions:	board must be a full list of positions
#Post-Conditions:	returns an integer from 0 to 3
#Return:			returns 0 if X won, 1 if O won, 2 if ites a tie, and 3 if they're still playing
"""
def checkWin(board):
	if (checkHoriz(board, 1) == True):
		return 0; #x has won
	if (checkHoriz(board, 0) == True):
		return 1; #x has lost

	if (checkVert(board, 1) == True):
		return 0; #x has won
	if (checkVert(board, 0) == True):
		return 1; #x has lost

	if (checkDiag(board, 1) == True):
		return 0; #x has won
	if (checkDiag(board, 0) == True):
		return 1; #x has lost

	if (checkHoriz(board, 1) == False and checkHoriz(board, 0) == False and checkVert(board, 1) == False and checkVert(board, 0) == False and checkDiag(board, 1) == False and checkDiag(board, 0) == False and getSpotsLeft(board) == 0):
		return 2; #its a tie if all else fails
	return 3; #still playing


"""
#Function Name: 	printResults()
#Description:		When a player wins, or the game ties, this method will print the result of the game
#Parameters:		res as integer for what print method the method should print
#Pre-Conditions:	res must be an integer
#Post-Conditions:	none
#Return:			none
"""
def printResults(res):
	if (res == 0): #its a win
		print("\nPlayer X has won vs Player O");
	elif (res == 1): #its a loss in relation to X vs O
		print("\nPlayer X has lost to player O");
	elif (res == 2): #its a tie!
		print("\nThere was a tie between X and O!");

"""
#Function Name: 	playAgain()
#Description:		asks the user if they wish to play another game or quit
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	return must be a boolean
#Return:			returns true if they want to play again, or false if they want to quit
"""
def playAgain():
	print("Do you wish to play again? (y/n)");
	inp = input(">>");
	if (inp == "y"):
		return True;
	elif (inp == "n"):
		print("Goodbye!");
		return False;

"""
#Function Name: 	printTotalResults()
#Description:		prints the final results of all the games played
#Parameters:		ties as the sum of all the ties, xwin as the sum of all wins from x, owin as the sum of all wins from 0
#Pre-Conditions:	ties as an integer, xwin as an integer, owin as an integer
#Post-Conditions:	none
#Return:			none
"""
def printTotalResults(ties, xwin, owin):
	print("\n\n");
	print("╔═══════════════╗");
	print("║ -TOTAL SCORE- ║");
	print("╠════════╦══════╣");
	print("║ X WINS ║   %s  ║" %(xwin));
	print("╠════════╬══════╣");
	print("║ O WINS ║   %s  ║" %(owin));
	print("╠════════╬══════╣");
	print("║  TIES  ║   %s  ║" %(ties));
	print("╚════════╩══════╝");
	print("\n")

"""
#Function Name: 	main()
#Description:		calls all the required initiation methods, and iterates through the loop until the game is won, then asks to play again
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			none
"""
def main():
	players = getPlayerCount(); totalXWins = 0; totalOWins = 0; totalTies = 0; keepPlaying = True;
	while (keepPlaying == True):
		curPlayer = 0; res = 3; board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
		while (res == 3):
			drawBoard(board, curPlayer);
			move = getMove(board, curPlayer, players);
			board = updateBoard(move, curPlayer, board);
			curPlayer = switchPlayers(curPlayer);
			res = checkWin(board);
		if (res == 0): totalXWins += 1;
		elif (res == 1): totalOWins += 1;
		elif (res == 2): totalTies += 1;
		printResults(res);
		printTotalResults(totalTies, totalXWins, totalOWins);
		keepPlaying = playAgain();

main();
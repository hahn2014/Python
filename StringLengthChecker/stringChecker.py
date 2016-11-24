"""
#Function Name:		numberOfMatchingCharacters
#Description:		Will compare two strings and return how many matching letters they have
#Parameters:		str1 as String for first input, str2 as String for second input
#Pre-Conditions:	both str1 and str2 must be strings
#Post-Conditions:	return value must be an integer
#Return:			returns how many characters are matching between the two strings as an integer
"""
def numberOfMatchingCharacters(str1, str2):
	matching = 0;
	if (len(str1) == len(str2)):
		for x in range(len(str1)):
			if (str1[x] == str2[x]):
				matching += 1;
	elif (len(str1) > len(str2)):
		for x in range(len(str2)):
			if (str1[x] == str2[x]):
				matching += 1; 
	elif (len(str1) < len(str2)):
		for x in range(len(str1)):
			if (str1[x] == str2[x]):
				matching += 1;
	
	return matching;

"""
#Function Name:		isLarger
#Description:		Takes in two strings and compares the two lengths to eachother
#Parameters:		str1 as String for first input, str2 as String for second input
#Pre-Conditions:	both str1 and str2 must be strings
#Post-Conditions:	return value must be a boolean
#Return:			returns true if inp1 is greater, or false if it is smaller or equal to
"""
def isLarger(inp1, inp2):
	if (len(inp1) > len(inp2)):
		return True;
	else:
		return False;

"""
#Function Name:		percentageMatching
#Description:		devides the number of matching by the largest string to get the percentage of similarity
#Parameters:		largest as int of characters from largest string, matching as int of number of matching characters between the two inputs
#Pre-Conditions:	both largest and matching must be integers
#Post-Conditions:	return value can be a floating point or integer
#Return:			returns the devided parameters multiplied by 100 to show percentage of similarity
"""
def percentageMatching(largest, matching):
	return (matching / largest) * 100;

"""
#Function Name:		getUserInput
#Description:		takes in user input as string for comparison
#Parameters:		inpnum as integer for debug to show which input we are entering
#Pre-Conditions:	inpnum must be a integer
#Post-Conditions:	inp will be a string
#Return:			returns the inputed value by the user
"""
def getUserInput(inpnum):
	print("Please enter a string input for input %s" %inpnum);

	inp = input(">>");
	return inp;

"""
#Function Name:		main
#Description:		calls all the functions to get input, calculate the similarchars and get the percentage
#Parameters:		none
#Pre-Conditions:	none
#Post-Conditions:	none
#Return:			no return value
"""
def main():
	inp1 = getUserInput(1);
	inp2 = getUserInput(2);
	matching = numberOfMatchingCharacters(inp1, inp2);
	print("number of matching -> %s" %matching);

	if (isLarger(inp1, inp2)):
		percentage = percentageMatching(len(inp1), matching);
	elif (isLarger(inp2, inp1)):
		percentage = percentageMatching(len(inp2), matching);
	else:
		percentage = 100;
	print("[%s] and [%s] are %s percent similar." %(inp1, inp2, percentage));

main();
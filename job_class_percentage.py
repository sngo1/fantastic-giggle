# Team fantastic-giggle
# Jen Yu & Samantha Ngo
# K#03
# 2017-09-14

import random;

OCCUPATIONS = {};

# Function to read in the csv file:
def csvToDict(file) :
	for line in open(file, 'r'):
		currentLine = line;
		if currentLine.find('"') :
			startQuote = currentLine.find('"');
			endQuote = currentLine[1].find('"');
			# Takes out the occupation from the quotes.
			occupation = currentLine[1:endQuote];
			percentage = currentLine[endQuote + 1:];
		else:
			# Determines the occupation and the percentage
			quote = currentLine.find('"');
			occupation = currentLine[:quote];
			percentage = currentLine[quote + 1:];
		# Adds occupation and percentage to the dictionary accordingly.
		OCCUPATIONS[occupation] = percentage;

csvToDict('occupation.csv');
print OCCUPATIONS;

# Ways to approach:
# 1. Give each occupation a percentile range in 1000 and then run a random 
# number.(Mostly hard coded for occupations)
# 2. For each key in OCCUPATIONS, run randomizer to see if it returns the 
# occupation range
# 3. Create a dictionary to store the associated ranges.

# Occupations and associated ranges for matching random numbers; stored
# in lists for order. 
# Should this be a global or local variable?
occupationRange = [];
occupationAttached = [];

# Function to find random occupation based on a weighted percentage; allows
# for user to change dictionary if necessary, but with same format.
def randomOccupation():
	# Counter for iterating through lists simultaneously.
	a = 0;
	# Acts as a start and end for each occupation's range.
	sum = 0;
	# For each key, determine the unique range from 1-1000 for that occupation
	# based on its percentage and add it to the lists.
	for k in OCCUPATIONS:
		if !(k == "Job Class" || k == "Total"):
			occupationAttached[a] = k;
			sum += OCCUPATIONS[k] * 10;
			occupationRange[a] = sum;
			a += 1;
	# Pick a random number from 1-998
	num = random.randint(1,998);
	# Find the range it falls into and the occupation associated with that 
	# range.
	b = 0;
	while num > occupationRange[b]:
		b += 1;
	return occupationAttached[b];
		

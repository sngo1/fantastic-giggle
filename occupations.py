# Team fantastic-giggle
# Jen Yu & Samantha Ngo
# K#03 StI/O: Divine your Destiny!
# 2017-09-14

import random

OCCUPATIONS = {}

#Function to read in the csv file of occupations:
def read_occupations(): 
	i = 0
	for line in  open('occupations.csv', 'r'):
		#cases where there are more than one comma
		if line.count(",") > 1:
			#rid the first quotation mark
			line = line[1:]
			#split with the second quotation mark
			curr_line = line.split("\"")
			#remove the remaining comma
			curr_line[1] = curr_line[1].replace(",", "")
		#all other cases, one comma
		else: 
			curr_line = line.split(',')
		#if not the header or the ender, add to dictionary
		if i != 0 and curr_line.count("Total") <= 0: 
			#get rid of the newline
			curr_line[1] = curr_line[1].replace("\n", "")
			#add a key and value to OCCUPATIONS dictionary
			OCCUPATIONS[curr_line[0].strip()] = float(curr_line[1])
		i += 1

read_occupations()

'''
for key in OCCUPATIONS: 
	print key, ": ", OCCUPATIONS[key]
'''

#Picks a random job with the percentage specified in the csv
def job_picker(): 
	picked = False
	while picked == False:
		try: 
			#pick a random percentage
			percent = (random.randint(0,100)/100.0) * 100
			for key in OCCUPATIONS: 
				#if the key has a higher % than the random %, then return the key and value (along with the random %)
				if OCCUPATIONS[key] > percent: 
					return key, OCCUPATIONS[key] #, percent
				#print OCCUPATIONS[key], percent
		except: 
			return "Dictionary is empty."
			
print job_picker()
	 
     
     


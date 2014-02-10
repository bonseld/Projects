 #	Brewer's Buddy			
 #							
 #	Dylan Bonsell			
 #	Created Oct. 4, 2013	
 #							
 #

''' Impports '''
import os
import time
import sys

''' Beer Globals '''
class beer_globals:
	def __init__(self, beer, hops, yeast, ings, ABV, storage):
		self.beer = beer
		self.hops = hops
		self.yeast = yeast
		self.ings = ings
		self.ABV = ABV
		self.storage = storage

''' Beer Class '''
class beer:
	def __init__(self, name, style, ABV, IBU, brewed_on, secondary_on, bottled_on, ings, yeasts, hops, storage):
		self.name = name
		self.style = style
		self.ABV = ABV
		self.IBU = IBU
		self.brewed_on = brewed_on
		self.secondary_on = secondary_on
		self.bottled_on = bottled_on
		self.ings = ings
		self.yeasts = yeasts
		self.hops = hops
		self.storage = storage

''' Ingredients (ings) Class '''
class ing:
	def __init__(self, name, ammount, time):
		self.name = name
		self.ammount = ammount
		self.time = time

''' Yeast Class '''
class yeast:
	def __init__(self, name, amount, starter):
		self.name = name
		self.amount = amount
		self.starter = starter

''' Hop Class '''
class hop:
	def __init__(self, name, amount, time, use):
		self.name = name
		self.amount = amount
		self.time = time
		self.use = use

''' ABV Class '''
class abv:
	def __init__(self, OG, FG, percent):
		self.OG = OG
		self.FG = FG
		self.percent = percent

''' Storage Class '''
class storage:
	def __init__(self, t, tt, total, tap):
		self.t = t
		self.tt = tt
		self.total = total
		self.tap = tap

''' Open Working Files '''
# Opens the files Beers.txt, Hops.txt, and Yeast.txt, and Ings.txt,
# parses them, then links (calls linker) and created objects for them.
# Returns a beer_globals
def read_files():
	#Open Files
	beers = open('Beers', 'r')
	hps = open('Hops', 'r')
	yea = open('Yeast', 'r')
	ins = open('Ings', 'r')
	ab = open('Abv', 'r')
	store = open('Storage', 'r')

	#Create the new object
	BG = beer_globals([], [], [], [], [], [])

	#Update Yeast Types
	for line in yea:
		words = line.split('\'')
		new_yeast = yeast(words[0], words[1], words[2])
		BG.yeast.append(new_yeast)

	#Update Hop Types
	for line in hps:
		words = line.split('\'')	
		new_hops = hop(words[0], words[1], words[2], words[3])
		BG.hops.append(new_hops)

	#Update Ingredients
	for line in ins:
		words = line.split('\'')
		new_ing = ing(words[0], words[1], words[2])
		BG.ings.append(new_ing)

	#Update Abv
	for line in ab:
		words = line.split('\'')
		new_abv = abv(words[0], words[1], words[2])
		BG.ABV.append(new_abv)

	#Update Storage
	for line in store:
		words = line.split('\'')
		new_storage = storage(words[0], words[1], words[2], words[3])
		BG.storage.append(new_storage)

	#Update Beers
	for line in beers:
		words = line.split('\'')
		beer_file = open(("Beer/" + words[0]), 'r')
		hops = beer_file.readline().split('\'')
		ings = beer_file.readline().split('\'')
		new_beer = beer(words[0], words[1], words[2], words[3], words[4], words[5], words[6], ings, words[7], hops, words[8])
		BG.beer.append(new_beer)
	#Call Linker
	BG = linker(BG)
	return BG

''' Object Linker '''
#File Object Linker.
def linker(beer_globals):
	for beer in beer_globals.beer:

		#Links Hops
		hps = []
		for hp in beer.hops:
			for item in beer_globals.hops:
				if int(hp) == beer_globals.hops.index(item):
					hps.append(item)
		beer_globals.beer[beer_globals.beer.index(beer)].hops = hps

		#Links Ings
		ingred = []
		for ing in beer.ings:
			for item in beer_globals.ings:
				if int(ing) == beer_globals.ings.index(item):
					ingred.append(item)
		beer_globals.beer[beer_globals.beer.index(beer)].ings = item

		#Links Yeast
		for item in beer_globals.yeast:
			if int(beer.yeasts) == beer_globals.yeast.index(item):
				beer_globals.beer[beer_globals.beer.index(beer)].yeasts = item

		#Links Storage
		for item in beer_globals.storage:
			if int(beer.storage) == beer_globals.storage.index(item):
				beer_globals.beer[beer_globals.beer.index(beer)].storage = item

		#Links Abv
		for item in beer_globals.ABV:
			if int(beer.ABV) == beer_globals.ABV.index(item):
				beer_globals.beer[beer_globals.beer.index(beer)].ABV = item
	return beer_globals




''' Cleanup Line Spaces '''
#Removes white spaces from a line
def cleanup_line(line):
	newline = ''
	for c in line:
		if c != ' ':
			newline += c
	return newline

''' Text Parser '''
def line_parse(line, beer_globals):
	if line == 'BEER':
		beer_menu(beer_globals)
	elif line == 'ABV' or line == "ABV CALC" or line == 'ABVCALC':
		ABV_menu(beer_globals)
	elif line == 'YEAST' or line == 'YEAST CALC' or line == 'YEASTCALC':
		yeast_menu(beer_globals)
	elif line == 'HELP':
		print 'Valid commands are: beer, abv, yeast, help, \'beer_name \''
		raw_input("Press Enter to continue...")
	else:
		valid_in = False
		for beer in beer_globals.beer:
			if line == beer.name.upper():
				information(beer)
				valid_in = True
		if valid_in == False:
			print 'You have entered an invalid input. Please type \'Help\' for more information.'
			raw_input("Press Enter to continue...")

''' Information Printing '''
#Prints information of a beer in a nice format.
def information(beer):
	os.system('cls' if os.name=='nt' else 'clear')
	print ('Name: ' + beer.name)
	print ('Style: ' + beer.style)
	print ('ABV: ' + beer.ABV.percent)
	print ('IBU: ' + beer.IBU)
	print ('Brewed On: ' + beer.brewed_on)
	if beer.secondary_on != None:
		print('Secondary On: ' + beer.secondary_on)
	if beer.bottled_on != None:
		print('Bottled On: ' + beer.bottled_on)
	print ('Yeast: ' + beer.yeasts.name)
	print ('   ' + beer.yeasts.amount)
	print ('   ' + beer.yeasts.starter)
	#Prints Hops List
	print ("Hops:")
	try:
		i = 1
		for ho in beer.hops:
			print ('   ' + str(i) + ': ' + str(ho.name))
			print ('      ' + ho.amount)
			print ('      ' + ho.time)
			print ('      ' + ho.use)
			i += 1
	except TypeError:
		print ('   1' + ': ' + str(beer.hops.name))
	#Prints Ingredients List
	print ("Ingredients:")
	try:
		i = 1
		for ig in beer.ings:
			print ("   " + str(i) + ': ' + str(ig.name))
			print ('      ' + ig.amount)
			print ('      ' + ig.time)
			i += 1
	except TypeError:
		print ('   1' + ': ' + str(beer.ings.name))
	if beer.storage != None:
		print('Ammount in Storage: ' + beer.storage.total)

	#Waits for Input
	raw_input("Press Enter to continue...")
	os.system('cls' if os.name=='nt' else 'clear')

''' ABV Calculator '''
def ABV_menu(beer_globals):
	og = raw_input("Please enter the Original Gravity in SG:" + "\n")
	fg = raw_input("Please enter the Final Gravity in SG:" + "\n")
	abv = (float(og)-float(fg))*131.25
	print "The Calculated ABV is " + str(abv) + "%\n"
	raw_input("Press Enter to continue...")
	os.system('cls' if os.name=='nt' else 'clear')

''' Beer Menu '''
#Starts the beer list, allows selection, returns beer object
def beer_menu(beer_globals):
	os.system('cls' if os.name=='nt' else 'clear')
	quit = 0
	found = 0
	while (quit == 0):
		print 'Beer Menu:'
		i = 1

		#Prints the list of beer
		for beer in beer_globals.beer:
			print (str(i) + ': ' + str(beer.name))

		#Prompts for beer input
		line = raw_input("Please enter a choice from the list of beers:" + "\n")

		#Checks for help input
		if line.upper() == 'HELP':
			print "Enter a beer name or number, or type exit to exit"
			raw_input("Press Enter to continue...")
			os.system('cls' if os.name=='nt' else 'clear')

		#Checks for exit input
		elif line.upper() == 'EXIT':
			quit = 1
			return

		#Try Catch to see if they referred to beer by int or name
		try: 
	   		 information(beer_globals.beer[int(line) - 1])
	   		 found = 1
		except ValueError: 
			for beer in beer_globals.beer:
				if beer.name.upper() == line.upper():
					found = 1
					information(beer)
					return beer
		else:
			if found == 0:
				print " You have not entered a beer choice. Use \'Help\' for more information"
				raw_input("Press Enter to continue...")
				os.system('cls' if os.name=='nt' else 'clear')



''' Menu '''
def menu(beer_globals):
	beer_globals.beer.sort()	#Sorts the beer list
	os.system('cls' if os.name=='nt' else 'clear')
	while True:
		print "Menu:"
		print "Beer"
		print "ABV Calc"	#TODO
		print "Yeast Calc"	#TODO
		line = raw_input("Please enter a choice from the menu:" + "\n")
		line = line.upper()
		#Call Text Parser
		line_parse(line, beer_globals)
		os.system('cls' if os.name=='nt' else 'clear')

try:
	beer_list = read_files()
	menu(beer_list)
except KeyboardInterrupt:
	print '\n' + "A keyboard interrupt was detected. Program shutting down."
	sys.exit()

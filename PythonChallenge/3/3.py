import re
f = open(raw_input("What is the file name?: "), 'r')
newline = ""
for line in f:
	matchObj = re.search('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', line, 0)
	if matchObj:
		print matchObj.group()
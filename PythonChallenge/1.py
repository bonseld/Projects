line = raw_input("What is the line?")
newline = ""
for i in line:
	if i.lower() == 'k':
		newline += 'm'
	elif i.lower() == 'o':
		newline += 'q'
	elif i.lower() == 'e':
		newline += 'g'
	else:
		newline += i

print newline
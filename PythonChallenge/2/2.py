f = open(raw_input("What is the file name?:"), 'r')
newline = ""
for line in f:
	for i in line:
		if ord(i) in range(97, 123):
			newline += i
print newline
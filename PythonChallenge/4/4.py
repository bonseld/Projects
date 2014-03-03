import urllib

f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579")
for i in range(1, 400):
	newstr = f.read()
	print newstr
	f = urllib.urlopen(("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(newstr.split()[-1])))

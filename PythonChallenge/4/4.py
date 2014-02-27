import urllib

f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
for i in range(1, 400):
	newstr = str(f.read()).split()[-1]
	print newstr
	f = urllib.urlopen(("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + newstr))
print f.read()

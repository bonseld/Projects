import urllib
f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
print f.read()
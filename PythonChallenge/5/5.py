import pickle

new = pickle.load(open(raw_input("What is the file? : "), 'r'))
s = ""
for i in new:
	print i
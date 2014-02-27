import string
print raw_input("What is the line?").translate(string.maketrans("yzabcdefghijklmnopqrstuvwx", "abcdefghijklmnopqrstuvwxyz"))

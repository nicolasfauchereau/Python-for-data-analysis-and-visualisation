#!/Users/nicolasf/anaconda/bin/python 
# This is a python script 

import sys # I import the sys module, part of the Python standard library

X = sys.argv[1:] # reading the command line arguments, X is list

X = " ".join(map(str,X)) # transform everything into a string

print(X.upper()) # printing the content, uppercase if applicable
#imports the module for argument variables
from sys import argv

#variable filename declared
script, filename = argv

#opens file contents in terminal
txt = open(filename)

#pastes file contents on screen
print "Here's your file %r:" % filename
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

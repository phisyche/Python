from sys import argv
from os.path import exists

script, ex16_sample.txt, ex17file2.txt = argv

print "Copying from %s to %s" % (ex16_sample.txt, ex17file2.txt)

# we could do these two on one line too, how?
input = open(ex16_sample.txt)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(ex17file2.txt)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(ex17file2.txt, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

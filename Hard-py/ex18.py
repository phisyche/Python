def print_two(*args):
    arg1, arg2 = args
    print "args: %r, arg2:%r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("x_crypt", "Ken")
print_two_again("x_crypt", "Ken")
print_one("First!")
print_none()

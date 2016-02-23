import random

number = random.randint(0, 100)

while True:
    user_answer = int(raw_input('guess a number: '))

    if user_answer == number:
        print "Thats accurate, how did you do it?".format(user_answer)
    elif user_answer < number:
        print "Too low".format(user_answer)
    elif user_answer > number:
        print "Too high".format(user_answer)

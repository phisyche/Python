from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
    "Your mom would be proud. If she were smarter.",
    "I have a small puppy that's better at this."]

    print quips[randint(0, len(quips)-1)]
    exit(1)

def princess_lives_here():
    print "Youshiny crown."
    print "She offers you some cake."

    eat_it = raw_input("> ")

    if eat_it == "eat it":
        print "You explode like a pinata full of frogs."
        print "The Princess cackles and eats the frogs. Yum!"
        return 'death'

    elif eat_it == "do not eat it":
        print "She throws the cake at you and it cuts off your head."
        print "The last thing you see is her munching on your torso. Yum!"
        return 'death'

    elif eat_it == "make her eat it":
        print "The Princess screams as you cram the cake in her mouth."
        print "Then she smiles and cries and thanks you for saving her."
        print "She points to a tiny door and says, 'The Koi needs cake too.'"
        print "She gives you the very last bit of cake and shoves you in."
        return 'gold_koi_pond'

    else:
        print "The princess looks at you confused and just points at the cake."
        return 'princess_lives-here'

def gold_koi_pond():
    print "There is a garden with a koi pond in the center."
    print "You walk close and see a massive fin poke out."
    print "You peek in and a creepy looking Koi stares at you."
    print "It opens its mouth waiting for food."

    feed_it = raw_input("> ")

    if feed_it == "feed it":
        print "The Koi jumps, and rather than eating the cake, eats your arm."
        print "You fall in and the Koi shrugs than eats you."
        print "You are then pooped out sometime later."
        return 'death'

    elif feed_it == "do not feed it":
        print "The Koi grimaces, then thrashe around for a second."
        print "It rushes to the other end of the pond, braces against the wall..."
        print "then it *lunges* out of the water, up in the air and over your"
        print "entire body, cake and all."
        print "You are then pooped out a week later."
        return 'death'

    elif feed_it == "throw it in":
        print "The Koi "

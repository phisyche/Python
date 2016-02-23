#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__init__
#self
#methods vs functions

class Human():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak_name(self):
        print "My name is %s" % self.name

    def speak(self, text):
        print text

    def perform_math_task(self, math_operation, *args):
        print "%s performed a math operation and the result was %f" % (self.name, math_operation(*args))

def add(a, b):
    return a + b
    
x_crypt = Human("Karanja", "Male")

x_crypt.perform_math_task(add, 24, 60)
print x_crypt.name
print x_crypt.gender

x_crypt.speak("Science is programming.")

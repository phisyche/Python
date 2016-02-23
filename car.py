class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.wheels = wheels
        self.miles = miles
        self.year = year
        

mustang = Car('Ford', 'Mustang')
print mustang.wheels
print Car.wheels

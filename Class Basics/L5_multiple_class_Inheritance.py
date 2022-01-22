class Horse():
    """ Creates objects like horses """
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def legs(self):
        print(f'{self.name} has four legs')

    def tail(self):
        print('It has a beautiful tail')

    def voice(self):
        print('Wonderful voice')

class Donkey():
    """ Creates objects like donkeys"""

    def __init__(self, name, color, load):
        self.name = name
        self.color = color
        self.load = load

    def legs(self):
        print(f'{self.name} has 2 legs')

    def tail(self):
        print('It has a tail')

    def work(self):
        print('Very hardworking animal')


class Mule(Horse, Donkey):
    
    def __init__(self, name, speed, load):

        super().__init__(name, speed, load)
        self.appearance = 'inbetween'
        
    def description(self):
        print("It looks like a donkey and a horse")

##    def legs(self):
##        """ This method will override every method of parents with the same name"""
##        print(f'{self.name} has four strong legs')
    
"""
if a method is common to both classes then the object will get the method
from 1st parent class
"""
my_mule = Mule('johny', '10', '1 ton')
my_mule.legs()
my_mule.tail()
my_mule.work()

my_mule.description()



        

                        #Classes
"""
- Classes represent real world situation and things
- Class define a general behaviour of whole category of objects
- Objects are created on the basis of classes
- model real world situations using oops
"""
"""
- creating objects from class is called instantiation
- work is done on instances of a class
- classes are stored and imported from modules
"""
#Modeling dogs-> 2 pieces of info: name,age -&- 2 behaviors: sit, roll over

#Class names are capitalized which by convention represent classes in python

class Dog():
    """ A simple attempt to model a dog """

    def __init__(self, name, age): #causes error without "__init__"
        """ Initialize name and age attributes """

        self.name= name     
        self.age= age

#A varaiable prefixed with "self" is avaialable to every other method in the class

    def sit(self):
        """ Simulate a dog sitting in response to command """
        print(self.name.title()+" is sitting now")

    def roll_over(self):
        """ Simulate a dog roll over in response to command """
        print(self.name.title()+" rolled over")



my_dog=Dog('tony', 6)
print("my dog's name is ",my_dog.name.title())
print("my dog's age is ",my_dog.age,"years")

#Creating multiple instances
your_dog=Dog('stark', 4)
sarah_dog=Dog('lilli', 3)

print("\nyour dog's name is", your_dog.name.title())
print("sarah's dog name is", sarah_dog.name.title())


#Calling methods
"""After the creation of object or instance we can call any method
defined with in the class using dot notation for that object"""

my_dog.sit()
my_dog.roll_over()




















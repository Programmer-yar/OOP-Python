
class Car():
    """A class to make car object/instances"""
    
"""-----------------------------------------------------"""
    def __init__(self, make, model, year):
        """Initialize attributes to make a car"""

        self.make=make
        self.model=model
        self.year=year
        
        self.odometer_reading=0
"""---------------------------------------------------------------"""

    def get_description(self):

        long_name = self.make+' '+self.model+' '+str(self.year)
        return long_name.title()
"""---------------------------------------------------------------"""

    def update_odometer(self, mileage):
        """ updates odometer attribute """
        if mileage>self.odometer_reading:
            
            self.odometer_reading = mileage

        else:
            print("Tempering with mileage is not allowed.")
"""----------------------------------------------------------------"""


    def increment_odometer(self, miles):
        """ Increments odometer value by certain amount """
        self.odometer_reading += miles
"""----------------------------------------------------------------"""


    def read_odometer(self):
        """print a statement to show car's mileage"""

        print("It has covered",self.odometer_reading,"km of distance.")
"""________________________________________________________________________"""

my_new_car=Car('suzuki' , 'wagon-r' , 2018)
print(my_new_car.get_description())
my_new_car.read_odometer()

                     #Modifying attribute's value

""" Modifying value directly """

my_new_car.odometer_reading=23

my_new_car.read_odometer()

""" Modifying value through a method """
my_new_car.update_odometer(50)
my_new_car.update_odometer(40)

my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()






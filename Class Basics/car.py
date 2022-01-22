""" A class that can be used to represent a car"""

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

        long_name = self.make+'|'+self.model+'|'+str(self.year)
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






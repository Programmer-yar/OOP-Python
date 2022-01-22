                            #INHERITANCE

"""
- A procedure when one class takes/inherits all attributes and methods
  of a class
- can also define its own unique attributes and methods
- The class which inherits attributes, methods from original class is called
  "child class"
- for inheritance to occur child class must be in the same programme as parent
  class
"""
class Car():
    """A class to make car object/instances"""
    

    def __init__(self, make, model, year):
        """Initialize attributes to make a car"""

        self.make=make
        self.model=model
        self.year=year
        
        self.odometer_reading=0
    """---------------------------------------------------------------"""

    def get_description(self):
 
        long_name = '|'+self.make+' - '+self.model+' - '+str(self.year)+'|'
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


class ElectricCar(Car):
    """Aspects specific to electric car"""

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class """

        super().__init__(make, model, year)
        self.battery_size = 30


    def describe_battery(self):
        """ this method will print statement describing battery """
        print("the car has", self.battery_size , "KWh battery")


    def get_range(self):

        if self.battery_size==30:
            range = 120
            
        elif self.battery_size==70:
            range = 240

        msg="this car can go approximately "+str(range)
        msg+="km, in one charge"
        print(msg)


my_tesla=ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_description())
my_tesla.describe_battery()
my_tesla.get_range()





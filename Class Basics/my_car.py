from car import Car

my_new_car=Car('toyota','grandy','2020')
print(my_new_car.get_description())
my_new_car.odometer_reading=50
my_new_car.read_odometer()
my_new_car.increment_odometer(75)
my_new_car.read_odometer()

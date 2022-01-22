"""    Magic Methods or Double Underscore/DUnder str Methods
"""
class Employee:
    raise_amt = 1.04

    #'__init__' automatically executes when an object is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #Below method is used for Unambigious representation of the object
    #Used for debugging and logging
    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay}) '

    #Used for readable representation of the object
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    #DUnder add method
    def __add__(self, other):
        return self.pay +other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 100000)
emp_2 = Employee('Ahmad', 'Yar', 200000)

#Before defining '__repr__' method, below statement will return output:
#<__main__.Employee object at 0x02001F88>
#After defining '__repr__' method, the output will be the input used to
#create the object
print(emp_1)

#both give same result
print(repr(emp_1))
print(emp_1.__repr__())

#'__add__'
print(1+2)
print(int.__add__(1, 2)) #'__add__' method from 'int' class
print(str.__add__('a', 'b')) #'__add__' method from 'str' class

print(emp_1 + emp_2) #Uses add method of Employee class

print(len('test')) #'len' is also a special method or 'DUnder'
print('test'.__len__()) #'__len__()' of array class
print(len(emp_1))
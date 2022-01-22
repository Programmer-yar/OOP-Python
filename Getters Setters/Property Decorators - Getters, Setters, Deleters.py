class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@gmail.com'

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('fullname deleted!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# changing the 'first' Name of employee after instance creation
emp_1.first = 'Jim'

"""
Email will still contain 'John', 
Now we will remove 'self.email' from constructor '__init__'
and make class method called 'email()' 
and call this method like 'instance.email()'
but this approach is not desireable
so we will use 'property' decorator
- property decorator
allows us to access method like an attribute without the need for other
people(already using this class) to change their code
"""

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname, '\n')

"""
- Setters:
if we want to change the fullname like
'instance.fullname = "Corey Schafer"'
then we will get (can't set attribute) error, which means that we need define Setter
"""

# Try this by commenting out fullname setter
emp_1.fullname = 'Corey Schafer'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname, '\n')

"""
- Deleters:
if we want to delete an attribute we can set a deleter method for 
that attribute
"""
del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
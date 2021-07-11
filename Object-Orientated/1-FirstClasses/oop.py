class Employee:
    # if the class should contain no code
    pass 

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# setting the attributes directly
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# can also run this way
# in this case 'emp_1' runs as self
Employee.fullname(emp_1)

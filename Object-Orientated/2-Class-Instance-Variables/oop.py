
class Employee:

    # class variable
    # variable should be the same for all instances
    raise_amount = 1.04

    num_of_emps = 0

    def __init__(self, first, last, pay):
        # these are the instance variables
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # do not use self because this variable should be the same 
        # for all instances
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.04)

    # method using the class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# accessing the class variable
Employee.raise_amount

# prints the instance variables
print(emp_1.__dict__)
# prints the class variables
print(Employee.__dict__)

# updating raise_amount for all instances
Employee.raise_amount = 1.05

# updating raise_amount for only one instance
emp_1.raise_amount = 1.05




'''
1. Classes are blue print of Object
2. An instance is the object of that Class
3. __init__ is constructor function in python
4. self is reference to the instance. It can be any name but by convention used as self.
5. for creating any method in a class an instance is required as an argument. So we pass self as an instance by default.
6. calling any method using instance without () return the object to that method not the value of that method.
7.  printing emp1.fullname() is similar as printing Employee.fullname(emp2). 
    In first case emp1 instance is automatically passed and in second case we need to manually pass the instance.
8. Here first is an argument and self.first is an instance variable whose value is assign with first argument. In self.first, first can be any name other than argument.
    But due to some convention we use the same name as argument.
'''

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Ish', 'Ver', 20000)
emp2 = Employee('Test', 'User', 10000)

print(emp1.fullname())
print(Employee.fullname(emp2))
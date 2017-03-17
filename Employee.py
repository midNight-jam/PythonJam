class Employee(object):
  raise_amount = 1.04
  no_of_emps = 0

  def __init__(self, first, last, pay): # constructor, first arg to each meth in class always the "self", the instance
    self.first = first
    self.last = last
    self.pay = pay
    # self.email = first + '.' + last +'@dark.com'
    Employee.no_of_emps +=1 # incrementing the count of the employees

  @property
  def fullName(self): # self is mandatory
    return '{} {}'.format(self.first, self.last)

  def raisePay(self):
    self.pay = self.pay * self.raise_amount
    # self.pay = self.pay * Employee.raiseAmount

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def create_from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first,last,pay)

  @staticmethod
  def isWorkDay(day):
    if day.weekday() > 4 and day.weekday() < 7:
      return False
    return True

  def __repr__(self):
    return "Employee ( '{}', '{}', '{}')".format(self.first, self.last, self.email)


  def __str__(self):
    return "Employee ( '{}','{}')".format(self.fullName, self.email)

  def __add__(self, other):
    return self.pay + other.pay

  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

emp1 = Employee('Jayam', 'Malviya', 45000)
emp2 = Employee('Test', 'Test', 9000)

print(emp1.email)
print(emp2.email)

print(emp1.fullName)  # self ois passed automatically
# print(Employee.fullName(emp1))  # manually have to specify self

Employee.raise_amount = 1.5
print(emp1.pay)
emp1.raisePay()
print(emp1.pay)

print(emp1.__dict__)
print(Employee.__dict__)

emp2.raise_amount = 1.8  # creates this attribute only for emp2
print(emp2.pay)
emp2.raisePay()
print(emp2.pay)
print(emp2.__dict__)


Employee.set_raise_amount(2.0)
print(emp1.pay)
emp1.raisePay()
print(emp1.pay)

print(Employee.no_of_emps)


empStr = 'Jayam-Malviya-8800'
strEmp = Employee.create_from_string(empStr);
print(strEmp.pay)

import datetime
mydate = datetime.date(2016,7,11)
print(Employee.isWorkDay(mydate))


print(repr(emp1))

print(emp1 + emp2)

print(emp2.email)

emp2.fullName = 'ZZZZ CCCC'
print(emp2.fullName)
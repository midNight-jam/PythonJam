li = [9,6,4,7,8,2,1,3,5]
s_li = sorted(li) # returns a new sorted list, uses "TimSort" time : O(nLogN) Space :O(n)
print'Sorted List', s_li
print'Original ', li

li.sort() # does sorting in place
print(li)

s_li = sorted(li, reverse= True) # sorts in descending , reverse
print(s_li)

# sort() only works on list, sorted() works on iterable
# sort() does sorting inplcae, thus changes the original order, while sorted() returns a new collection
tup = (9,8,7,6,5,4,3,2,1)
# tup.sort() no such method

s_tup = sorted(tup)
print'tuple : ',s_tup

di = {'name': 'jayam', 'job': 'na' , 'age':None, 'os': 'all'}
s_di = sorted(di) # sorts and returns the keys of dictionary
print(s_di)


#### Custom sorting ####

# sorting by absoulte values
li = [4,-5,6,-7,1,-2,-3,8,-9]
s_li = sorted(li, key=abs) # abs is called while making comparision
print(s_li)


class Empoyee():
  def __init__(self, name, age, sal):
    self.name = name
    self.age = age
    self.sal = sal

  def __repr__(self):
    return '({},{},${})'.format(self.name, self.age, self.sal)

def e_sort(emp):
  return emp.age  # return the attribute which hsa to be used for comparision for sorting

e1 = Empoyee('jayam',36,56000)
e2 = Empoyee('malviya',26,710000)
e3 = Empoyee('aZZZZ',56,1710000)

emps = [e3, e1, e2]
s_emps = sorted(emps)
print(s_emps)

s_emps = sorted(emps, key = e_sort) # passing in the custom sort method
print(s_emps)

s_emps = sorted(emps, key = e_sort, reverse= True) # descending in age
print(s_emps)

# using Lambda
s_emps = sorted(emps, key = lambda e : e.name, reverse= True ) # using a lambda function for key
print(s_emps)

# using attrgetter
from operator import attrgetter
s_emps = sorted(emps, key = attrgetter('sal'), reverse= True ) # using attergetter for key
print(s_emps)

print 'First module {}'.format(__name__)
# if we are running the file directly then python sets this variable
# if the module was used by another file , then it contains the module name
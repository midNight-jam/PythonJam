nums = [1,2,3,4,5,6,7,8,9,10]

#1 I want 'n' for 'n' in each nums
my_list = []
for n in nums:
  my_list.append(n)
print(my_list)

# List Comprehension , much easier
my_list = [n for n in nums]
print(my_list)


#2 I want 'n*n' for 'n' in each nums
my_list = []
for n in nums:
  my_list.append(n * n)
print(my_list)

# List Comprehension , much easier
my_list = [n*n for n in nums]
print(my_list)

#3 Using a map + lambda
# map :  map runs every thing in the list through a certain function
# lambda : lambda is an anonymous function
my_list = map(lambda n : n*n, nums) # a bit more complex to understand, list copmrehension preffered
print(my_list)



#4 I want 'n' for 'n' in each nums if n is even
my_list = []
for n in nums:
  if(n%2 == 0):
    my_list.append(n)
print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

my_list = [n for n in nums if n & 1 == 0] # using bit
print(my_list)


#4 Map + Lamda : I want 'n' for 'n' in each nums if n is even
my_list = map(lambda n : n % 2 == 0, nums)
print(my_list)

#5 I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
  for i in range(4):
    my_list.append((letter, i))
print(my_list)


my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


############ Dictionary Comprehensions ############

names = ['John','Corey','Ganan','Poss','Kunai','Popoe','Lokan']
majors= ['MD','ME','EC','ME','EE','IT','CS']
# zip mathces the two list with index same, means it will put element at 0 in both list ina tuple
# and element at 1 in both list at another and so on...
print(zip(names,majors))

my_dict = {}
for name, major in zip(names,majors):
  my_dict[name] = major
print(my_dict)

# observe that we dont have [] braces instead {} brackets for map
my_dict = {name: major for name,major in zip(names,majors) if name !='Kunai'}
print(my_dict)




############ Set Comprehensions ############

nums = [1,1,2,2,3,4,5,5,6,6,7,7,7,8,8,9,10]
my_set = set()
for n in nums:
  my_set.add(n)
print(my_set)

my_set = {n for n in nums} # creatinga set. Observe {},  and no : (colon)
print(my_set)

############ Generator Expressions ############

nums = [1,2,3,4,5,6,7,8,9,10]

def gen_sq(nums):
  for n in nums:
    yield (n**2)

my_gen = gen_sq(nums)
for n in my_gen:
  print(n)

my_gen = (n**2 for n in nums)
for n in my_gen:
  print(n)

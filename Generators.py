# this is not a memory efficient method as we require another storage
# to hold the result, thus we need double space
def square_nums(nums):
  sq_nums = []  # another var to store squared nos
  for i in nums:
    sq_nums.append(i * i)
  return sq_nums


def sq_nums_Generators (nums):
  for i in nums:
    yield (i * i) # making it a generator
    # in this way it doesnt return the result, rather it calulates the result
    # element by element, thats why we have to use next() or loop to get the whole result



my_nums = square_nums([1,2,3,4,5,6])
print(my_nums)

my_nums = sq_nums_Generators([1, 2, 3, 4, 5, 6])

for n in my_nums:
  print(n)
  # after getting the last value from the generator and still if fetching we get an exception "StopIteration"
  # meaning that the entire Genrator has been exhausted

# using list comprehension also returns a genrator
more_nums = ( i * i for i in [1, 2, 3, 4, 5, 6])
for n in more_nums:
  print(n)

# or converting it to a list, but it looses the performance gain
more_nums = ( i * i for i in [1, 2, 3, 4, 5, 6])
nums_lis = list(more_nums)
print(nums_lis)


########### Generators Comparision ###########
import random
import time
names = ['John','Corey','Ganan','Poss','Kunai','Popoe','Lokan']
majors= ['MD','ME','EC','ME','EE','IT','CS']

def people_list(num_people):
  result = []
  for i in range(num_people): # for i to n
    result.append({
      'id' : i,
      'name' : random.choice(names),
      'major' : random.choice(majors)
    })
  return result

def people_generator(num_people):
  for i in range(num_people):
    person = {
      'id':i,
      'name':random.choice(names),
      'majors':random.choice(majors)
    }
    yield person



def main():
  t1 = time.clock()
  peoples = people_list(50000)
  t2 = time.clock()
  # for p in peoples:
  #   print(p)
  print(t2-t1)

  print("=========Now generators=========")
  t1 = time.clock()
  peoples = people_generator(50000)
  t2 = time.clock()
  # for p in peoples:
  #   print(p)

  print(t2-t1)



if __name__=='__main__':
  main()
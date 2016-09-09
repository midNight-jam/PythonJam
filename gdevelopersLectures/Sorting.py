import time

def sortMethod(dumbList):
  print('Calling sort Method')
  start_time = time.clock()
  sortedLsit = sorted(dumbList) # doesnt sorts the original list, thus returns a new one, original is still intact
  end_time = time.clock()-start_time
  print(sortedLsit)
  print('Time = ', end_time - start_time)

def sortOnCriteria(list,criteria):
  start_time = time.clock()
  sortedLsit = sorted(list,key=criteria)
  end_time = time.clock()-start_time
  print(sortedLsit)
  print('Time = ', end_time - start_time)


def criteriaLastChar(string):
  return string[-1]

def main():
  dumbList = [5,6,1,2,7,4,9,2]
  sortMethod(dumbList)

  dumbStringList = ['zza','az','wwwb','bx','gggggf']
  sortMethod(dumbStringList)
  sortOnCriteria(dumbStringList,len)
  print(sorted(dumbStringList,key=criteriaLastChar))

  print('trying sort')
  print(dumbList)
  dumbList.sort() #sort method doesnt returns a new list, it modifies the original list, thus its faster in the case
  # where list is already sorted, as it doesnt have to create a copy of list.
  print(dumbList)


if __name__=='__main__':
  main()

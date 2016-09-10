def main():
  print('tuples')
  myTuple = (1,2,'First')
  print(myTuple)
  print(myTuple[0])
  print(myTuple[1])
  print(myTuple[2])
  print(myTuple[-1])
  #myTuple[0]=99  TypeError: 'tuple' object does not support item assignment
  print(myTuple)
  myTuple = (3,4,"Second")
  print(myTuple)
  (x,y,z) = myTuple
  print(z)
  #(a,b) = myTuple  ValueError: too many values to unpack (expected 2)

  lonleyTuple = ('Single',)
  print(lonleyTuple)
  print(lonleyTuple[0])

  arrayOfTuples = myTuple *3
  print(arrayOfTuples)
  (a0,a1,a2,a3,a4,a5,a6,a7,a8) = arrayOfTuples
  print(a2)
  for t in arrayOfTuples:
    print(t)

if __name__=='__main__':
  main()

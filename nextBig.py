def nextBig(numbersList):
  nextBigList = [None] * len(numbersList)
  pa = len(numbersList)-1
  pb = pa-1
  currentBig = numbersList[pa]
  while pa>0:
    if numbersList[pb]<currentBig:
      nextBigList[pb] = currentBig
    if numbersList[pb]>numbersList[pa]:
      currentBig = numbersList[pb]
    pa-=1
    pb=pa-1
  return nextBigList

def main():
  print("Sending the array")
  #numbersList = [5,6,3,10,9,12]
  #numbersList = [13,7,6,12]
  numbersList = [4,13,7,6,12]
  for i in nextBig(numbersList):
    print(i)
  print("is the out put correct!")


if __name__=='__main__':
  main()

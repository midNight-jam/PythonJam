
def doDel():
  varOne = 'a variable'
  print(varOne)
  del varOne
  # print(varOne) # results in UnboundLocalError : local variable 'varOne' referenced before assignment

def doDelList():
  list = [2,3,5,6]
  del list[0]
  print(list)
  del list[-2]
  print(list)

def doDelDict():
  dict={}
  dict[1]='orange'
  dict[2]='lemon'
  dict[3]='grape'
  print(dict)
  del dict[2]
  print(dict)

def main():
  doDel()
  doDelList()
  doDelDict()

if __name__ =='__main__':
  main()

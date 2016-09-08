def nextAdjacentBig(numbersList ):
  pa=-1
  pb = pa+1
  while pb<len(numbersList) -1 :
    pc = pb+1
    if numbersList[pb]<numbersList[pc]:
        while pa<pc:
          pa=pb
          numbersList[pa]=numbersList[pc]
          pa += 1
    pb = pb+1

  return numbersList;

def main():

  print('Sending in the array')
  #numbersList = [5,6,3,10,9,12]
  #numbersList = [12,9,3,6,5]
  numbersList = [13,7,6,12]
  #numbersList = [9,12,9,1,0,2,3,6,9]
  for l in nextAdjacentBig(numbersList):
    print(' ', l)

if __name__ =='__main__':
  main()

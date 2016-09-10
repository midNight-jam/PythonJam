def isPerfectSquare(num):
  odd = 1;
  while True:
    if num ==0:
      return True
    if num<0:
      return False
    num-=odd
    odd+=2

# amazingly less code, WOW!!!
def intersection(list1,list2):
  intersecting = [n1 for n1 in list1 if n1 in list2]
  return intersecting

def main():
  nums = [1,2,3,4]

  # the syntax is [ expr for var in list ]
  numSquares = [i*i for i in nums ]
  # The expr to its left is evaluated once for each element to give the values for the new list.

  print("Nums ",nums)
  print("Num Squares ",numSquares)

  words = ['you', 'back','again']
  shoutingWords = [ w[0:4].upper()+w[-1].lower() for w in words]
  print(shoutingWords)

  moreNums = [1,2,3,4,5,6,7,8,9,25,33,36]
  sqrs = [print(n) for n in moreNums if isPerfectSquare(n)]

  someMoreNums = [3,8,4,6,849,546,36]
  print(intersection(moreNums,someMoreNums))

  grocery = ['Tissue','apple','soap','maggi']
  store = ['Ludo','Apple','bat','maggi']
  canBuy = intersection(grocery,store)
  print(canBuy)

if __name__=='__main__':
  main()

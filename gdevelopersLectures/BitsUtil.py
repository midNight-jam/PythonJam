def bitwise_OR(a, b):
    print('Bitwise OR == ', a|b)

def bitwise_AND(a , b):
    print('Bitwise And == ', a&b)


def bitwise_XOR(a, b):
    print('Bitwise And == ', a ^ b)

def findOddNumber( noList):
    xor_Temp = 0;
    for n in noList:
        xor_Temp = xor_Temp ^ n
    print(' Odd occurring is  : ',xor_Temp)
    return xor_Temp

def xorWO_XOR_operator(a,b):
    res = a^b
    res2 = (~a & b ) | (~b & a)
    print("a^b == ",res, " wo xor a^b  ",res2)

def swap_using_XOR(a,b):
    a = a^b
    b = a^b
    a = a^b
    print('After swap a : ',a , '  b : ',b)

def bitsCount(n):
  count = 0
  while (n!=0):
    n = n>>1
    count = count + 1
  return count

def isPowerOfTwo(n):
  if n >0:
    b=0
    while n!=0:
      b = n & 1
      n = n >>1
      if b==1:
        break
    if n==0:
      return True
  return False

def evenOddBits(n):
  b = 0
  s = 0
  while n!=0:
    b = n & 1
    s = s ^ b
    n = n >> 1
  if s ==1:
    print('Odd [1] Bits ')
  else:
    print('Even [1] Bits ')

def isKthBitSet(n,k):
  n = n >> (k-1)
  n = n & 1
  if n == 1:
    return True
  else:
    return False
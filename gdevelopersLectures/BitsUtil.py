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

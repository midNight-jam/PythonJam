import BitsUtil

def useBits():
    BitsUtil.bitwise_OR(1,4)
    BitsUtil.bitwise_AND(1, 4)
    BitsUtil.bitwise_XOR(1, 4)
    BitsUtil.findOddNumber([5,3,7,9,3,3,1,2,9,4,5,7,4,1,2,3,3,2,2])
    a = 88
    b =11
    BitsUtil.swap_using_XOR(a,b)
    BitsUtil.xorWO_XOR_operator(a,b)
    print(" bits count 13 == ", BitsUtil.bitsCount(13))
    print(" is power of 2 == ", BitsUtil.isPowerOfTwo(1))
    BitsUtil.evenOddBits(5);
    print(' ',BitsUtil.isKthBitSet(5,3));

def main():
    print('I am main')
    print('-2 ', (~2))
    useBits()

if __name__ == '__main__':
    main()
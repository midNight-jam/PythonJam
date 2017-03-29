my_list = [1,2,3,4,5,6,7,8,9]

print(my_list[0])
print(my_list[-1]) # len -(given index)

#list[start:end:step] end is non inlcusive
print(my_list[1:-2])
print(my_list[-2:2]) # not possible thus empty array
print(my_list[0:])
print(my_list[:-2])
print(my_list[:]) # entire list

print(my_list[2:-1:2]) # take step of 2, default step is 1, tahts why prints every element
# prints 3 5 7

print(my_list[2:-1:-1]) # empty array as it is going behind
print(my_list[-2:1:-1]) # 8 to 3 in reverse
print(my_list[::-1]) # entire list in reverse

####### String #######
url = 'http://google.com'
print(url)
print(url[2:])
print(url[:3])
print(url[:-3])
print(url[-1:0:-1]) # reverse
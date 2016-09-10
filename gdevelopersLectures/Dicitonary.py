# Strategy note: from a performance point of view, the dictionary is one of your greatest tools,
# and you should use it where you can as an easy way to organize data.
# For example, you might read a log file where each line begins with an IP address,
# and store the data into a dict using the IP address as the key, and the list of lines where it appears as the value.
# Once you've read in the whole file, you can look up any IP address and instantly see its list of lines.
# The dictionary takes in scattered data and makes it into something coherent.


def dictFormatting():
  hash ={}
  hash['cat'] = 'garfield'
  hash['copies'] = 15

  string = 'I want to kill %(cat)s, %(copies)d times' %hash #super WOW!!!
  print(string)


def main():
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gogeta'
  dict['c'] = 'charizard'
  print(dict)
  print(dict['c'])
  dict['g'] = 220;
  print(dict)
  # dict[119]='somePlay'  #how does this works internally, replacing a key type??
  print(dict)
  print(dict.get(119))
  print('a' in  dict)

  for k in dict:
    print(k)
  print('Keys')
  for keys in dict.keys():
    print(keys)

  print(dict.values())

  # fails because keys are not of same type
  sortedKeys = sorted(dict.keys())
  # TypeError: unorderable types: int() < str()
  for k in sortedKeys:
    print(dict[k])

  items = dict.items();
  print(items)

  for k,v in items: print(k,'-->',v)
  dictFormatting()

if __name__ =='__main__':
  main()

import os
def readFile():
  my_file = 'Flows.py'

  #RaceCondition
  if(os.access(my_file, os.R_OK)):
    with open(my_file) as f:  # by the time we come to this line after checking the access, it could happen that we cannot access the file any more
      print(f.read())

  #EAFP Pythonic way
  try:
    f = open(my_file)
  except IOError as e:
    print('Error opening th file')
  else:
    with f :
      print (f.read())


def main():
  readFile()


if __name__ == '__main__':
  main()
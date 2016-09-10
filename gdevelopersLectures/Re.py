# The basic rules of regular expression search for a pattern within a string are:
# 1: the search proceeds from start to end, stopping at first match
# 2: All of the patterns must be matched, not all of the string
# 3: if match = re.search(pat,text) is  successful, match is notNone & match.group is the matching text

import re


def doRE():
  text =  'an example word:cat!!'
  # The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes
  # without change which is very handy for regular expressions
  match = re.search(r'word:\w\w\w',text)
  if match: print(match.group())
  else: print('No match')


def doMoreRE():
    text ='piiiig'
    match = re.search(r'iii',text)
    print(match.group())

    match2 = re.search(r'iaa',text)
    # print(match2.group())
    # here on above line we get AttributeError: 'NoneType' object has no attribute 'group'


    ## . = any char but \n
    match3 = re.search(r'..g',text)
    print(match3.group())

    # \d = digit char,
    match4 = re.search(r'\d\d\d','p123g')
    print(match4.group())

    ## \w = word char, not symbol
    match5 = re.search(r'\w\w\w','@@@123%%$%&*$%abc!!!')
    print(match5.group()) ## prints 123

    match6 = re.search(r'\w\w\w','@@@%%$%&*$%abc!!!')
    print(match6.group()) ## prints abc


def doMultipleRE():
  match = re.search(r'pi+','piiiiiig')
  print(match.group())  ##+ : one or more


  match2 = re.search(r'pi*','piiiiiig')
  print(match2.group())  ##* : 0 or more

  match3 = re.search(r'^p\w+','piiiiiig')
  print(match3.group())  ##^  : starts with

def emailExtractor(text):
  email = re.search(r'\w+@\w+\.\w+',text)
  if email:
    return email

def emailMatcher(text):
  match  = re.search(r'[\w.-]+@[\w.-]+', text)
  if match:
    return match

def main():
  doRE()
  doMoreRE()
  doMultipleRE()
  match  = emailExtractor('some text donkeys idiot123Moonshine@treasure.com we suck at bad examples')
  print(match.group())

  match  = emailExtractor('some text donkeys idiot-123Moonshine@treasure.com we suck at bad examples')
  print(match.group())
  # print(match.group(0))
  # print(match.group(1))
  # print(match.group(2))

if __name__=='__main__':
  main()

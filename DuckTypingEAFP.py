class Duck():
  def quack(self):
    print("Quack qucak")
  def fly(self):
    print('Flap, Flap')

class Person():
  def quack(self):
    print('A person tryoing to quack')
  def fly(self):
    print('A person trying to fly')

def quack_and_fly(thing):
  #NonPythonicway
  if( isinstance(thing, Duck)): # naive solution
    thing.quack()
    thing.fly()
  else:
    if(hasattr(thing,'quack') and callable(thing.quack)): # check if the obj contains attribute and that ist is callable method
      thing.quack()
    thing.fly()

#EAFP (pythonic way)
def quack_and_fly_EAFP(thing):
  try:
    thing.quack()
    thing.fly()
    thing.bark()
  except AttributeError as e:
    print(e)  # logs error when the bark attribute couldnt be found in the thing instance
    #instance has no attribute 'bark'

def dictEAFP():
  person = {'name' : 'jayam', 'age':28,'job':'lol'}
  # Naive non pythonic way
  if 'name' in person and 'age' in person and 'job' in person:
    print(person)
  else:
    print('missing some keys...')

  # Pythonic way EAFP
  try:
    print('name : {0}, job : {1}, age : {2}'.format(person['name'], person['job'], person['age']))
  except KeyError as e:
    print('Missing Key {0}'.format(e))


def listEAFP(index):
  my_list = [1,2,3,4,5]
  ## Nonpythonic way, asking permission
  if len(my_list) > index:
    print(my_list[index])
  else:
    print('List doesnt contains index : {0}'.format(index))

  #EAFP : Easy to Ask Forgiveness then to ask Permission
  # why efficient
  #1 as we are aceessing the object only once, rather than asking permission where we have to access object more than one time
  #2 readable
  #3 better handling for race condition when dealing with files
  try:
    print(my_list[index])
  except IndexError as e:
    print(e)


def main():
  d = Duck()
  p = Person()
  quack_and_fly(d)
  quack_and_fly(p)
  quack_and_fly_EAFP(p)
  quack_and_fly_EAFP(d)
  dictEAFP()
  listEAFP(6)

if __name__ == '__main__':
  main()
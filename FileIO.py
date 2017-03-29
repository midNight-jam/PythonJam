# Naive way
def naiveIO():
  f = open('Slicing.py','r')  # defaults to open the file for reading
  print(f.name)
  print(f.mode) # the mode in which the file was open 'r'
  print(f.read())
  f.close() # if we dont close the file, we can run to leaks, excedding the no of maximum allowed open file descriptors

# Using a Context Maanger
def contextMgrIO():
  # with context mgr will always automatically close the file when the block is finished
  # in case of success or exceptions
  with open('Slicing.py','r') as f:
    f_contents = f.read()
    print(f_contents) # loads all the content in the memory, not effieicnt

  # still access to f var , after the block
  print(f.mode)
  # print(f.read()) #but cant read as the file is closed "ValueError"

# Using a Context Maanger, line by line
def contextMgrIOLine():
  # memory efficient, as it reads only sinlge line at a time
  with open('Slicing.py','r') as f:
    for line in f :
      print(line)


# Using a Context Maanger, controlled by file size
def contextMgrIOControlled():
  with open('Slicing.py','r') as f:
    f_contents = f.read(10) # specifying the no of chars to read
    print(f_contents)

    f_contents = f.read(30)  # picks up from where it left
    print(f_contents)

    f_contents = f.read(1000)  # returns empty string when reached end
    print(f_contents)

# to read big files
def readingHugeFiles():
  with open('Slicing.py') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    print f_contents
    f.seek(0) # moving the cursor back to 0 position

    while len(f_contents) > 0:  # will terminate at end of ffile, beacuse it returns an empty string
      print(f_contents)
      f_contents = f.read(size_to_read)
      print(f.tell()) # print the position of cursor


def writeToFile():
  with open('test.txt','a') as f: # opening in write mode, use 'a' for append mode
    f.write('Testzz') # replcaes the content
    f.seek(0) #writing froma  postiion
    f.write('R') # overrides the char at which seek has set

def copyFile():
  with open('test.txt', 'r') as rf:
    with open('testCopy.txt','w') as wf:  # creates a new file
      for line in rf:
        wf.write(line)


def copyImage():
  # open the files in binary mode
  with open('skull.jpg','rb') as rf:
    with open('copySkull.jpg','wb') as wf:
      chunk_size = 4096 # 4kb
      rf_chunk = rf.read(chunk_size)
      while len(rf_chunk) > 0:
        wf.write(rf_chunk)
        rf_chunk = rf.read(chunk_size)

if __name__ == '__main__':
  # naiveIO()
  # contextMgrIO()
  # contextMgrIOLine()
  # contextMgrIOControlled()
  # readingHugeFiles()
  # writeToFile()
  # copyFile()
  copyImage()
import numpy as np

docs = [["hello","world","hello"],["goodbye","cruel","world"]]
indptr = [0]
indices = []
data = []
vocabulary = {}
for d in docs:
  for term in d:
    index = vocabulary.setdefault(term,len(vocabulary))
    indices.append(index)
    data.append(1)
  indptr.append(len(indices))

print('data',data)
print('indptr',indptr)
print('indices',indices)
print(vocabulary)
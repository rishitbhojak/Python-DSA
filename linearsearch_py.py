# -*- coding: utf-8 -*-
"""LinearSearch.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vQddwWHZLtOy1GAyCgBFCzi6CXbIJSTp
"""

pos = -1
def search(list, n):
  i=0
  while i< len(list):
    if list[i] == n:
      globals()['pos'] = i
      return True
    i=i+1  
  return False
list = [5,8,4,9,6,2]
n=9
if search(list, n):
  print("Found at position no.: " , pos+1)
  print("Found at index: ", pos)
else:
  print("Not Found")


# -*- coding: utf-8 -*-
"""Fibonacci.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZx-ZiewWfCUdLXy-DyFJ1LozW1qyNzo
"""

k = int(input("Enter a no.: "))
def fibo(n):
  if n in [0,1]:
    return n 
  else:
    return fibo(n-1) + fibo(n-2)
if k <=  0:
  print("Enter a Positive integer")
else:
  print("Fibonacci sequence: ")
  for i in range(k):
    print(fibo(i))

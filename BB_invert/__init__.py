import numpy as np

def help():
  print("1) This module contains 5 unknown black box functions, called BB1, ..., BB5. Figure out the following:")
  print("  a) Is BB1 one-to-one?")
  print("  b) _________________?")
  print("  c) _________________?")
  print("2) There are also two functions, f and g, included. Are they inverses? Prove it.")

def BB1(x):
  y = 2**-(x+3)**2
  return y

def BB2(x):
  y = np.sin(x-1) - (x**2)/50
  return y

def BB3(x):
  y = np.sqrt(-x**2+16)
  return y

def BB4(x):
  y = np.sqrt(-(x-2)**2+25)*0.5
  return y

def BB5(x):
  y = x**3 + x**2
  return y

def f(x): #check if invertible with g
  y = (x+2)/3
  return y

def g(x):
  y = 3*x-2
  return y

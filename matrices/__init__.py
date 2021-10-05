import numpy as np

def connection_check():
  print("Successful. This is version from 05Oct2021.")

def problem1_description():
  print("Two hotdogs and a hamburger cost $3.50, and one hotdog and 2 hamburgers cost $4.00. \n We want to know how much and individual hotdog and hamburger cost. \n Start by setting this up as a matrix problem.")
  
def get_matrices():
  A = np.array([[2, 1],[1, 2]])
  b = np.array([[3.5],[4]])
  return A, b

def calc_x(A, b):
  x = np.matmul(np.linalg.inv(A),b)
  return x

def check_answer(x):
  if x.all() == get_answer():
    print('correct')
  else:
    print('wrong')

def get_answer():
  A, b = get_matrices()
  x = calc_x(A,b)
  print(x)
  

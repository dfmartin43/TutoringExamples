import numpy as np

def connection_check():
  print("Successful. This code version from 29Oct2021. This module contains two problems. You can get information on the problems \n using 'problem1_description()' and 'problem2_description()'.")

def problem1_description():
  print("We have some equipment that we'd like to understand better. \n There are three pieces of equipment that can take inputs and give corresponding outputs, but we don't know what exactly they do.")
  print("You can input things into the pieces of equipment and they will give the output. Your job is to model this behavior with some functions.")
  print("The equipment are called E1, E2, and E3. To give an input, you will call the functions: for example, 'output = E1(5)' will give the result \n of inputting the number 5 in equipment 1. You can then print 'output' to see the value.")
 
def problem2_description():
  print("Building on problem 1, we have a more advanced piece of equipment that will require two inputs. \n It is called E4 and you can get outputs using something like 'output = E4(2,3)'.")

def E1(x):
  return x*x+1
  
def E2(x):
  return np.exp(x)
  
def E3(x):  
  return x - 5 + np.random.normal(0, 2, 1)

def E4(x1,x2):
  return x1+x2

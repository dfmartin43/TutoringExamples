import numpy as np

def help():
  print("This module contains high school geometry functions. Below is a list of functions that can be used: \n\narea_of_circle: input radius | returns area of circle")
  print("circ_circle: input radius | returns circumference of circle \narea_of_rect: input length and width | returns area of rectangle \narea_tri: input base and height | returns area of triangle")
  print("hypotenuse: input b and c sides of a triangle | returns the hypotenuse \ncol_rect_prism: input length, width, height | returns volume of prism")
  print("vol_cyl: input radius and height | returns volume of cylinder")
  print("vol_sphere: input radius | returns volume of sphere \nvol_cone: input radius and height | returns volume of cone")
  print("vol_pyr: input length, width, height | returns volume of pyramid")

def area_of_circle(r):
  a = 3.14*(r*r)
  return a

def circ_circle(r):
  c = 2*3.14*r
  return c

def area_tri(b,h):
  a = 1/2*b*h
  return a

def hypotenuse(a,b):
  c = np.sqrt(a*a + b*b)
  return c

def vol_rect_prism(l,w,h):
  v = area_of_rect(l,w)*h
  return v

def area_of_rect(l,w):
  a = l*w
  return a

def vol_cyl(r,h):
  v = area_of_circle(r)*h
  return v

def vol_sphere(r):
  v = 4/3*3.14*(r*r*r)
  return v

def vol_cone(r,h):
  v = 1/3*vol_cyl(r,h)
  return v

def vol_pyr(l,w,h):
  v = 1/3*vol_rect_prism(l,w,h)
  return v

def shape1(a,b):
  temp = a/3*b^2
  return temp

def shape2(a,b):
  temp = a^2*b
  return temp

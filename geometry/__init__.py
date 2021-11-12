import numpy as np

def help():
  print("")

def area_of_circle(r):
  a = 3.14*(r*r)
  return a

def circ_circle(r):
  c = 2*3.14*r
  return c

def area_tri(b,h):
  a = 1/2*b*h
  return a

def hypoteneuse(a,b):
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

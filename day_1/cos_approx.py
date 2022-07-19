#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Amadi Brians C'
__email__ = 'amadibrians@gmail.com'

from math import factorial
from math import pi
import argparse
import numpy as np

def cos_approx(x, accuracy):
    """This function will return an approximate cosine using Taylor series."""
    
    cosyn = sum([((((-1)**n)/factorial(2 * n)) * x **(2 * n)) for n in range(accuracy)])
       
    return cosyn



def parse_args():
  # Create an argument parser:
  parser = argparse.ArgumentParser(description = \
                                   'This code computes the cosine of a value x using Taylor series')

  # in_scalar: scalar value, type float:
  parser.add_argument('-x', \
                      help = 'This is the value of the angle', \
                      type = float)
  # npts: scalar value, type integer, default 5:
  parser.add_argument('-npts', \
                      help = 'This is the accuracy (default = 10)', \
                      type = int, default = 10)
  # actually parse the data now:
  args = parser.parse_args()
  return args
# ------------------------------------------------------
# My Main code:
# ------------------------------------------------------
# parse the input arguments:
args = parse_args()

npts = args.npts
print(npts)
# grab the variable do_this (a boolean, default false):
x = args.x
print(x)

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(x) = ", cos_approx(x, npts))
    print('cospy =', np.cos(x))
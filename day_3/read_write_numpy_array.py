# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 07:03:02 2022

"""

__author__ = 'Amadi Brians C'
__email__ = 'amadibrians@gmail.com'


#%%
"""
Writing and reading numpy file
"""

# Importing the required packages
import numpy as np
import argparse

def read_write_np_array(n, m):
    
    # Generate a random array of dimension n by m
    data_arr = np.random.randn(n, m)

    # Save the data_arr variable into a .npy file
    np.save('test_np_save.npy', data_arr)

    #load the data
    data_arr_loaded = np.load('test_np_save.npy')
    
    #print data_arr_loaded
    print(data_arr_loaded)
    
    #check if the saved array is equal to the loaded array
    print(np.equal(data_arr,data_arr_loaded))
    
    #check if the saved array is equal to the loaded array but prints out a single True value if all elements are equal
    print(np.equal(data_arr,data_arr_loaded).all())

    return
    
def parse_args():
  # Create an argument parser:
  parser = argparse.ArgumentParser(description = \
                                   'This code prints a matrix with a n number of rows and m number of columns')

  # in_scalar: scalar value, type float:
  parser.add_argument('-n', \
                      help = 'This is the number of rows', \
                      type = int)
  # npts: scalar value, type integer, default 5:
  parser.add_argument('-m', \
                      help = 'This is the number of columns', \
                      type = int, default = 10)
  # actually parse the data now:
  args = parser.parse_args()
  return args
# ------------------------------------------------------
# My Main code:
# ------------------------------------------------------
# parse the input arguments:
args = parse_args()

n = args.n
print(n)
# grab the variable do_this (a boolean, default false):
m = args.m
print(m)

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    read_write_np_array(n, m)
    
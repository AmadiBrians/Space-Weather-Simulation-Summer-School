# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:03:22 2022

@author: amadi
"""

__author__ = 'Amadi Brians C'
__email__ = 'amadibrians@gmail.com'

import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import argparse

def read_ascii_file(file_name, index):
    """This function reads an ascii file"""
    with open(file_name) as f:
        
        data_dic = {"year": [],
                     "day": [],
                     "hour": [],
                     "minute": [],
                     "time": [],
                    "data": []}

        
        for line in f:
            tmp = line.split()
            
            #create datetime in each line
            time0 = dt.datetime(int(tmp[0]), 1, 1, int(tmp[2]), int(tmp[3]), 0)\
            + dt.timedelta(days = int(tmp[1]) -1)
            
            data_dic["time"].append(time0)
            data_dic["year"].append(int(tmp[0]))
            data_dic["day"].append(int(tmp[1]))
            data_dic["hour"].append(int(tmp[2]))
            data_dic["minute"].append(int(tmp[3]))
            data_dic["data"].append(int(tmp[index]))
            
            time = np.array(data_dic['time'])
            data = np.array(data_dic['data'])
            
            #time = np.array(data_dic['time'])
            data1 = np.array(data_dic['data'])

        fig, ax = plt.subplots()

        lp = data <-100
        #print(lp)

        ax.plot(time, data, marker = '.', c = 'blue',
                   label = 'All Events', alpha = 0.5)
        ax.plot(time[lp], data1[lp], marker = '+',
                   linestyle = '',
                   c = 'tab:orange',
                   label = '<-100 nT',
                   alpha = 0.6)

        ax.set_xlabel('Year of 2013')
        ax.set_ylabel('SYMH (nT)')
        ax.grid(True)
        ax.legend()
        plt.savefig("test3a.png")

    return data_dic


def parse_args():
  # Create an argument parser:
  parser = argparse.ArgumentParser(description = \
                                   'This code plots the SYMH of a given date')

    # file_directory:
  parser.add_argument('-x', \
                      help = 'This is the File directory', \
                      type = str)

  # index of data to be plotted:
  parser.add_argument('-i', \
                      help = 'This is the index of the line to be plotted', \
                      type = int)

  # actually parse the data now:
  args = parser.parse_args()
  return args

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
# ------------------------------------------------------
# My Main code:
# ------------------------------------------------------
# parse the input arguments:
args = parse_args()

# grab the name or dir of the file:
x = args.x
print(x)

#grab the index of the data
i = args.i
print(i)

#run the function for a given x and i
x = '"C:/Users/amadi/SWSSS/Space-Weather-Simulation-Summer-School/day_2/omni_min_march2013.lst"'
read_ascii_file(x, i)



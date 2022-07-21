#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome to Space Weather Simulation Summer School Day 3

Today, we will be working with various file types, doing some simple data 
manipulation and data visualization

We will be using a lot of things that have been covered over the last two days 
with minor vairation.

Goal: Getting comfortable with reading and writing data, doing simple data 
manipulation, and visualizing data.

Task: Fill in the cells with the correct codes

@author: Peng Mun Siew
"""

#%% 
"""
This is a code cell that we can use to partition our data. (Similar to Matlab cell)
We hace the options to run the codes cell by cell by using the "Run current cell" button on the top.
"""
print ("Hello World")

#%%
"""
Writing and reading numpy file
"""
# Importing the required packages
import numpy as np

# Generate a random array of dimension 10 by 5
data_arr = np.random.randn(10,5)
print(data_arr)

# Save the data_arr variable into a .npy file
np.save('test_np_save.npy', data_arr)

#load
data_arr_loaded = np.load('test_np_save.npy')

print(np.equal(data_arr,data_arr_loaded))
#%%
"""
Writing and reading numpy zip archive/file
"""
# Generate a second random array of dimension 8 by 1
data_arr2 = np.random.randn(8,1)
print(data_arr2)

# Save the data_arr and data_arr2 variables into a .npz file
np.savez('test_savez.npz', data_arr, data_arr2)

#load it
npzfile = np.load('test_savez.npz')

print(npzfile)

print('variable names within this file:', sorted(npzfile.files))

#%%
print(npzfile['arr_0'])

#verification that the loaded data matches the intial data exactly
print((data_arr == npzfile['arr_0']).all())
print((data_arr2 == npzfile['arr_1']).all())
#%%
"""
Error and exception
"""



#%%
"""
Loading data from Matlab
"""


# Import required packages
import numpy as np
from scipy.io import loadmat

dir_density_Jb2008 = r'C:\Users\amadi\SWSSS\Space-Weather-Simulation-Summer-School\day_3\JB2008\2002_JB2008_density.mat'

# Load Density Data
try:
    loaded_data = loadmat(dir_density_Jb2008)
    print (loaded_data)
except:
    print("File not found. Please check your directory")

# Uses key to extract our data of interest
JB2008_dens = loaded_data['densityData']

# The shape command now works
print(JB2008_dens.shape)



#%%
"""
Data visualization I

Let's visualize the density field for 400 KM at different time.
"""
#2131/.,mn -*+ Import required packages
import matplotlib.pyplot as plt

# Before we can visualize our density data, we first need to generate the discretization grid of the density data in 3D space. We will be using np.linspace to create evenly sapce data between the limits.

localSolarTimes_JB2008 = np.linspace(0,24,24)
latitudes_JB2008 = np.linspace(-87.5,87.5,20)
altitudes_JB2008 = np.linspace(100,800,36)
nofAlt_JB2008 = altitudes_JB2008.shape[0]
nofLst_JB2008 = localSolarTimes_JB2008.shape[0]
nofLat_JB2008 = latitudes_JB2008.shape[0]

# We can also impose additional constratints such as forcing the values to be integers.
time_array_JB2008 = np.linspace(0,8759,20, dtype = int)

# For the dataset that we will be working with today, you will need to reshape them to be lst x lat x altitude
JB2008_dens_reshaped = np.reshape(JB2008_dens,(nofLst_JB2008, nofLat_JB2008, nofAlt_JB2008, 8760), order='F') # Fortran-like index order
#%%
#print(localSolarTimes_JB2008)

print(localSolarTimes_JB2008.shape[0])

#%%

import matplotlib.pyplot as plt


# Look for data that correspond to an altitude of 400 KM
alt = 400
hi = np.where(altitudes_JB2008==alt)

# Create a canvas to plot our data on. Here we are using a subplot with 5 spaces for the plots.
fig, axs = plt.subplots(5, figsize=(15, 10*2), sharex=True)

for ik in range (5):
    
    cs = axs[ik].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[ik]].squeeze().T)
    axs[ik].set_title('JB2008 density at 400 km, t = {} hrs'.format(time_array_JB2008[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=18)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    # Make a colorbar for the ContourSet returned by the contourf call.
    cbar = fig.colorbar(cs,ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=18)

#%%

# Look for data that correspond to an altitude of 400 KM
alt = 400
hi = np.where(altitudes_JB2008==alt)

# Create a canvas to plot our data on. Here we are using a subplot with 5 spaces for the plots.
fig, axs = plt.subplots(20, figsize=(15, 10*2), sharex=True)

for ik in range(20):
    cs = axs[ik].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[ik]].squeeze().T)
    axs[ik].set_title('JB2008 density at 400 km, t = {} hrs'.format(time_array_JB2008[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=10)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    # Make a colorbar for the ContourSet returned by the contourf call.
    cbar = fig.colorbar(cs,ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=10)


#%%
alt = 400
hi = np.where(altitudes_JB2008==alt)


# Create a canvas to plot our data on. Here we are using a subplot with 5 spaces for the plots.
fig, axs = plt.subplots(20, figsize=(15, 10*2), sharex=True)

for ik in range(20):
    #NB: JB2008_dens_reshaped is 4d
    cs = axs[ik].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[ik]].squeeze().T)
    axs[ik].set_title('JB2008 density at 400 km, t = {} hrs'.format(time_array_JB2008[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=10)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    # Make a colorbar for the ContourSet returned by the contourf call.
    cbar = fig.colorbar(cs,ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=10)

#%%
"""
Assignment 1

Can you plot the mean density for each altitude at February 1st, 2002?
"""

# First identify the time index that corresponds to  February 1st, 2002. 
#Note the data is generated at an hourly interval from 00:00 January 1st, 2002
#thus feb 1 starts from 31 (no. of days in january) * 24(no. of hours)
time_index = 31*24

#this selects this data from Feb1
dens_data_feb1 = JB2008_dens_reshaped[:,:,:,time_index]

#this line prints out the shape of dens_data_feb1
#print(dens_data_feb1.shape)

#obtain the mean along axis 0 and 1 for all altitudes
JB2008_dens_feb1_alt_mean = dens_data_feb1.mean(axis =(0,1))

#print(alt_mean)
#plt.yscale('log')

#plt.plot(altitudes_JB2008, JB2008_dens_feb1_alt_mean)

plt.semilogy(altitudes_JB2008, JB2008_dens_feb1_alt_mean)
plt.xlabel('Altitude')
plt.ylabel('Log of Density')
plt.grid()

plt.show()

#%%

#This code plots mean density for an altitude of 400 km for a given day (Feb 1st = time_index = 31 * 24)
alt = 400

hi = np.where(altitudes_JB2008 == alt)

#this selects this data from Feb1
dens_data_feb1 = JB2008_dens_reshaped[:,:,hi, time_index]

#this line prints out the shape of dens_data_feb1
#print(dens_data_feb1.shape)

#obtain the mean along axis 0 and 1 for all altitudes
JB2008_dens_feb1_alt_meanz = dens_data_feb1.mean(axis =(1,3))

#print(alt_mean)
#plt.yscale('log')

plt.plot(localSolarTimes_JB2008 , JB2008_dens_feb1_alt_meanz)

#plt.semilogy(localSolarTimes_JB2008, JB2008_dens_feb1_alt_meanz)
plt.xlabel('Time of Day')
plt.ylabel('Density (g/cm3)')
plt.title('JB2008 Model')
plt.grid()

plt.show()
#%%
"""
Data Visualization II

Now, let's us work with density data from TIE-GCM instead, and plot the density field at 310km
"""
# Import required packages
import h5py

loaded_data = h5py.File(r'C:\Users\amadi\SWSSS\Space-Weather-Simulation-Summer-School\day_3\Data\TIEGCM\2002_TIEGCM_density.mat')

#this will print out the keys (variables) of the file
print('Key within database:',list(loaded_data.keys()))

#Note: the data has been processed before now. Hence, we are taking it back to the original data by stating 10**.....
tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T # convert from g/cm3 to kg/m3

#%%
#shape of imported data and its variables
print(tiegcm_dens.shape)
print(loaded_data['altitudes'])
print(np.array(loaded_data['latitudes']).flatten().shape)
print(np.array(loaded_data['localSolarTimes']).flatten().shape)
#%%
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten() #flatten takes off any irrelevant array. E.g (21, 1) becomes (21,)
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0] #21
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0] #24
nofLat_tiegcm = latitudes_tiegcm.shape[0] #36

time_array_tiegcm = np.linspace(0,8760,20, dtype = int)

# Each data correspond to the density at a point in 3D space. 
# We can recover the density field by reshaping the array.
# For the dataset that we will be working with today, you will need to reshape them to be lst x lat x altitude
tiegcm_dens_reshaped = np.reshape(tiegcm_dens,(nofLst_tiegcm,nofLat_tiegcm,nofAlt_tiegcm,8760), order='F')

import matplotlib.pyplot as plt

#i = 100
alt = 310
hi = np.where(altitudes_tiegcm==alt)

# Create a canvas to plot our data on. Here we are using a subplot with 5 spaces for the plots.
fig, axs = plt.subplots(5, figsize=(15, 10*2), sharex=True)

for ik in range (5):
    cs = axs[ik].contourf(localSolarTimes_tiegcm, latitudes_tiegcm, tiegcm_dens_reshaped[:,:,hi,time_array_tiegcm[ik]].reshape(nofLst_tiegcm,nofLat_tiegcm).T)
    axs[ik].set_title('TIE-GCM density at 310 km, t = {} hrs'.format(time_array_tiegcm[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=18)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    # Make a colorbar for the ContourSet returned by the contourf call.
    cbar = fig.colorbar(cs,ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=18)    

#%%

tiegcm_dens_feb1 = tiegcm_dens_reshaped[:,:,:,time_index]
tiegcm_dens_feb1_alt_mean = np.mean(tiegcm_dens_feb1, axis=(0,1))

plt.subplots(1, figsize=(10, 6))
plt.semilogy(altitudes_tiegcm,tiegcm_dens_feb1_alt_mean,linewidth = 2)
plt.xlabel('Altitude', fontsize=18)
plt.ylabel('Density', fontsize=18)
plt.title('Mean Density vs Altitude', fontsize=18)
plt.grid()
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#%%
plt.subplots(1, figsize=(10, 6))
plt.semilogy(altitudes_tiegcm,tiegcm_dens_feb1_alt_mean,linewidth = 2,label='TIE-GCM')
plt.semilogy(altitudes_JB2008,JB2008_dens_feb1_alt_mean,'-.',linewidth = 2,label='JB2008')
plt.xlabel('Altitude', fontsize=18)
plt.ylabel('Density', fontsize=18)
plt.title('Mean Density vs Altitude', fontsize=18)
plt.grid()
plt.legend(fontsize=16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#%%
"""
Data Interpolation (1D)

Now, let's us look at how to do data interpolation with scipy
"""
# Import required packages
from scipy import interpolate

# Let's first create some data for interpolation
x = np.arange(0, 10)
y = np.exp(-x/3.0)

#generate 1d interploant function
interp_func_1D = interpolate.interp1d(x, y)

#new x values to be fed into the interpolation function
xnew = np.arange(0, 9, 0.1)

#feed the new x values into the interpolation
ynew = interp_func_1D(xnew)   # use interpolation function returned by `interp1d`

#plot the new (o) and old(-) values
plt.subplots(1, figsize=(10, 6))
plt.plot(x, y, 'o', xnew, ynew, '-',linewidth = 2)
plt.legend(['Inital Points','Interpolated line'], fontsize = 16)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)
plt.title('1D interpolation', fontsize=18)
plt.grid()
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#%%
x = np.arange(0, 10)
y = np.exp(-x/3.0)

#generate 1d interploant function
interp_func_cubic = interpolate.CubicSpline(x, y)

#new x values to be fed into the interpolation function
xnew = np.arange(0, 9, 0.1)

#feed the new x values into the interpolation
ynew = interp_func_cubic(xnew)   # use interpolation function returned by `interp1d`

#plot the new (o) and old(-) values
plt.subplots(1, figsize=(10, 6))
plt.plot(x, y, 'o', xnew, ynew, '-',linewidth = 2)
plt.legend(['Inital Points','Cubic Interpolated line'], fontsize = 16)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)
plt.title('Cubic interpolation', fontsize=18)
plt.grid()
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)


#%%
"""
Data Interpolation (3D)

Now, let's us look at how to do data interpolation with scipy
"""
# Import required packages
from scipy.interpolate import RegularGridInterpolator

# First create a set of sample data that we will be using 3D interpolation on
def function_1(x, y, z):
    return 2 * x**3 + 3 * y**2 - z

x = np.linspace(1, 4, 11)
y = np.linspace(4, 7, 22)
z = np.linspace(7, 9, 33)

xg, yg ,zg = np.meshgrid(x, y, z, indexing='ij', sparse=True)

sample_data = function_1(xg, yg, zg)

# Generate Interpolant (interpolating function)
interpolated_function_1 = RegularGridInterpolator((x, y, z), sample_data)

# Say we are interested in the points [[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]]
pts = np.array([[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]])

#this array will output y for a given array pts
print('Using interpolated method;', interpolated_function_1(pts))

#pts[:,0] will pick the first numbers in eaach array and that becomes x
#pts[:,1] will pick the first numbers in eaach array and that becomes y
#pts[:,2] will pick the first numbers in eaach array and that becomes z
print('From true function:', function_1(pts[:,0],pts[:,1],pts[:,2]))

#%%
#pts[:,0] will pick the first numbers in eaach array and that becomes x
print(pts[:,0])
#%%
"""
Saving mat file

Now, let's us look at how to we can save our data into a mat file
"""
# Import required packages
from scipy.io import savemat

a = np.arange(20)
mdic = {"a": a, "label": "experiment"} # Using dictionary to store multiple variables
savemat("matlab_matrix.mat", mdic)

#%%
"""
Assignment 2 (a)

The two data that we have been working on today have different discretization grid.
Use 3D interpolation to evaluate the TIE-GCM density field at 400 KM on February 1st, 2002, 
with the discretized grid used for the JB2008 ((nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008).
"""

#%%

from scipy.interpolate import RegularGridInterpolator

time_index = 31*24
tiegcm_function = RegularGridInterpolator((localSolarTimes_tiegcm, latitudes_tiegcm, altitudes_tiegcm), tiegcm_dens_reshaped[:,:,:,time_index], bounds_error=False, fill_value=None)
# bound_error = False - can ask for points outside of the initial range
# fill_value = None - extrapolate based on data for those outside the range

print('TIE-GCM density at lst=20, lat=12, alt=400km:', tiegcm_function((20,12,400)))

#%%





tiegcm_jb2008_grid = np.zeros((24, 20))
for i in range(24):
    for j in range(20):
        tiegcm_jb2008_grid[i, j] = ((localSolarTimes_JB2008[i], latitudes_JB2008[j], 400))
        
if1 = RegularGridInterpolator((localSolarTimes_tiegcm, latitudes_tiegcm, altitudes_tiegcm), tiegcm_dens_reshaped)

pts = np.array([[2, 6], [4, 7]])
print(if1(pts))


#%%
"""
Assignment 2 (b)

Now, let's find the difference between both density models and plot out this difference in a contour plot.
"""





#%%
"""
Assignment 2 (c)

In the scientific field, it is sometime more useful to plot the differences in terms of mean absolute percentage difference/error (MAPE). Let's plot the MAPE for this scenario.
"""






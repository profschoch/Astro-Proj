#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue OCT 15 19:56:07 2020

@author: peterschoch
"""
# fits_manip.py
# -------------------------------------------------------------------------
# This program is designed to import a FITS image.  Slice off the image 
#  portion as an array, and then
#  perform some calculations on the array and output the altered
#  image.
# ------------------------------------------------------------------------- 

import matplotlib.pyplot as plt

from astropy.io import fits
#  This gives us access to all of the astronomy  file opening utilities.


astr_file=fits.open('Moon100327050242.FITS')
# This imports the astronomy photo.

print(astr_file.info())
# This gives a summary of the open file.

image_data=astr_file[0].data
# This removes the headers and just assigns the image as a np array 
# to the variable.

astr_file.close()
#This closes the file.  You MUST do this for FITS files; or,
# you may crash your system.  you have the image data stored in the new array,
# so there is no harm in closing the file now.




plt.figure(figsize=(10,10))
#Sets the image size for output, or you'l get a really small output.
plt.imshow(image_data, cmap='gray', aspect='equal')






plt.figure()
#  This makes sure that the original figure stays on the screen and then the 
#  output of the convolved one will appear below it.


plt.figure(figsize=(10,10))
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.axis('off')

img_crop=image_data[25:400,50:401]
# Looking at the output of the first image, I estimated the bounds to
#  eliminate the black space and just give me the moon.

plt.figure()
plt.figure(figsize=(15,15))
plt.imshow(img_crop, cmap='gray')

plt.figure()
#  This makes sure that the original figure stays on the screen and then the 
#  output of the convolved one will appear below it.



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as py
 
import cv2
''' the above libraray is for reading the images '''
x1=cv2.imread('E1.png')

x2=cv2.imread('E2.png')
x3=cv2.imread('E3.png')
''' the above images are in the grayscale type '''
x1=pd.DataFrame(x1[0:,0:,2])
x2=pd.DataFrame(x2[0:,0:,2])
x3=pd.DataFrame(x3[0:,0:,2])
x1=np.array(x1)

x2=np.array(x2)
x3=np.array(x3)

i=0
j=0
while i<460:
    j=0
    while j<3600:
        x1[i,j]=int(x1[i,j])
        x2[i,j]=int(x2[i,j])
        x3[i,j]=int(x3[i,j])
        j=j+1
    i=i+1    

i=0
j=0
while i<460:
    j=0
    while j<3600:
        if x1[i,j]==255:
            x1[i,j]=int(0)
        else:
            x1[i,j]=int(1)
        j=j+1
    i=i+1    
i=0
j=0        
while i<460:
    j=0
    while j<3600:
        if x2[i,j]==255:
            x2[i,j]=int(0)
            int(x2[i,j])
        else:
            x2[i,j]=int(1)
        j=j+1
    i=i+1    
i=0
j=0
while i<460:
    j=0
    while j<3600:
        if x3[i,j]==255:
            x3[i,j]=int(0)
        else:
            x3[i,j]=int(1)
        j=j+1
    i=i+1   
np.savetxt('test1.csv', x1, delimiter=',', fmt='%s')    
np.savetxt('test2.csv', x2, delimiter=',', fmt='%s')
np.savetxt('test3.csv', x3, delimiter=',', fmt='%s')


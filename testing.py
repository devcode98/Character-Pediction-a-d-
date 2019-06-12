# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:54:43 2018

@author: Devang
"""

from algo_tester import *
''' now we will be importing the image file '''
import cv2
''' the above libraray is for reading the images '''
x1=cv2.imread('sam1.png')
x1=pd.DataFrame(x1[0:,0:,2])
x1=np.array(x1)
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

result1=fitter2.predict(x1)
result2=fitter3.predict(x1)
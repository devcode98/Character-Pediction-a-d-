# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:21:21 2018

@author: Devang
"""

import sys 
import numpy as np
import pandas as pd
import matplotlib.pyplot as py

xa=pd.read_excel('A1.xlsx')
xb=pd.read_excel('B1.xlsx')
xc=pd.read_excel('C1.xlsx')
xd=pd.read_excel('D1.xlsx')
xe=pd.read_excel('E1.xlsx')
merger=[xa,xb,xc,xd,xe]
''' now we will be vreating an output array as in total output'''
x_a=[]
x_b=[]
x_c=[]
x_d=[]
x_e=[]
i=0
while i<2754:
    x_a.append(int(65))
    x_b.append(int(66))
    x_c.append(int(67))
    x_d.append(int(68))
    x_e.append(int(69))
    i=i+1
''' now we will be using the ascii codes '''    
    
tot=pd.concat(merger)
x_tot=x_a + x_b + x_c + x_d + x_e



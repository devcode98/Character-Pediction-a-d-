# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:40:49 2018

@author: Devang
"""

from data_recover import *
from sklearn.linear_model import LinearRegression
x_train=tot
y_train=x_tot
fitter=LinearRegression().fit(x_train,y_train)
from sklearn.linear_model import LogisticRegression
''' now we will be applying the logistic regression as the another method '''
fitter2=LogisticRegression().fit(x_train,y_train)
from sklearn.ensemble import RandomForestClassifier
fitter3=RandomForestClassifier()
fitter3.fit(x_train,y_train)

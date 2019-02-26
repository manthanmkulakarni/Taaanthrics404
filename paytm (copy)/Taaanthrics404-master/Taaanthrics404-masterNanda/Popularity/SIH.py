# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:50:56 2019

@author: ankita1999
"""
#popularity number

#importing libraries
import random
import pandas as pd

#importing dataset
dataset=pd.read_csv(r'C:\Users\ankita1999\Downloads\crowddatasetforsihmodified.csv')

#random popularity number generation
popularitynumber=[]
for i in range(0,500):
    popularitynumber.insert(i,random.randrange(0,101))
df=pd.DataFrame(dataset)
df['Popularity']=popularitynumber

#assumed input
notificationid=200

#function to check whether the product is popular
def popularitycheck():
    global notificationid
    popularity=df.loc[df['Notificationid']==notificationid].iloc[:,10].values
    if popularity>=75:
        return 1
    return 0

#function call
popularitycheck()
     

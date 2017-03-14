#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:24:12 2017

@author: DK
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#importing dataset
dataset=pd.read_csv('/Users/DK/Documents/Machine_Learning/Python-and-R/Machine_Learning_Projects/Reinforcement Learning/UCB/Ads_CTR_Optimisation.csv')

#implementing UCB
N=10000
total_reward=0
d=10
selected_ads=[]
num_of_selected=[0]*d
sum_of_rewards=[0]*d
for n in range(0,N):
    max_sum=0                   #to be reset for each round
    ad=0
    for i in range(0,d):
        if num_of_selected[i]>0:
            delta=math.sqrt((3/2)*(math.log(n+1)/num_of_selected[i]))
            avg_reward=(sum_of_rewards[i]/num_of_selected[i])
            upper_bound=avg_reward+delta
        else:
            upper_bound=1e400
        if max_sum<upper_bound:
            max_sum=upper_bound
            ad=i                #to keep track of the index of the selected ad
    selected_ads.append(ad)
    num_of_selected[ad]+=1
    reward=dataset.values[n,ad]   #n is the row and ad is the column; the entries in the dataset are either 1 or 0
    sum_of_rewards[ad]+=reward
    total_reward+=reward 

#visualisation    
plt.hist(selected_ads)
plt.title('Histogram of Selected Ads')
plt.xlabel('Ads')
plt.ylabel('Number of times each Ad was selected')
plt.show()       
        
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
dataset=pd.read_csv('/Users/DK/Documents/Machine_Learning/Python-and-R/Machine_Learning_Projects/Reinforcement Learning/Thompson Model/Ads_CTR_Optimisation.csv')

#implementing Thompson Model
import random
N=10000
total_reward=0
d=10
selected_ads=[]
num_of_rewards_1=[0]*d
num_of_rewards_0=[0]*d
for n in range(0,N):
    max_random=0                   #to be reset for each round
    ad=0
    for i in range(0,d):
        random_beta=random.betavariate(num_of_rewards_1[i]+1,num_of_rewards_0[i]+1)
        if max_random<random_beta:
            max_random=random_beta
            ad=i                #to keep track of the index of the selected ad
    selected_ads.append(ad)
    reward=dataset.values[n,ad]   #n is the row and ad is the column; the entries in the dataset are either 1 or 0
    if reward==1:
        num_of_rewards_1[ad] += 1
    else:
        num_of_rewards_0[ad] += 1
    total_reward+=reward 

#visualisation    
plt.hist(selected_ads)
plt.title('Histogram of Selected Ads')
plt.xlabel('Ads')
plt.ylabel('Number of times each Ad was selected')
plt.show()       
        
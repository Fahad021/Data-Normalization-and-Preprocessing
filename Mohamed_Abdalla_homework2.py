# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import copy
from scipy.stats import zscore
from scipy.spatial import distance
from scipy.spatial import distance_matrix
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine

data_file = np.genfromtxt('winequality.txt', delimiter=';')
winesamples=data_file[0:10,:]

### Question 1:

## min-max normalized values:
WSnorm1=copy.deepcopy(winesamples)
for i in range(12):
 WSnorm1[:,i]= (winesamples[:,i]-winesamples[:,i].min())/(winesamples[:,i].max()-winesamples[:,i].min())
print("min-max normalized")
print(WSnorm1)

## z-score normalized values:
WSnorm2=zscore(winesamples)
print("z-score normalized")
print(WSnorm2)

## mean subtracted normalized values
WSnorm3=copy.deepcopy(winesamples)
for i in range(12):
 WSnorm3[:,i]= winesamples[:,i]-np.mean(winesamples[:,i])
print("mean subtracted normalized")
print(WSnorm3)

### Question 2:

## using manhatten distance to obtain [nearest,farthest]
dis1= distance_matrix(winesamples,winesamples,p=1)
WSdis1=[[4,9],[6,8],[6,9],[6,8],[0,9],[[0,4],9],[2,9],[8,9],[7,9],[1,8]]
print("using manhatten distance to obtain [nearest,farthest]")
print(WSdis1)

## using euclidean distance to obtain [nearest,farthest]
dis2= distance_matrix(winesamples,winesamples,p=2)
WSdis2=[[4,9],[3,8],[6,9],[6,8],[0,9],[[0,4],9],[2,9],[8,9],[7,9],[1,8]]
print("using euclidean distance to obtain [nearest,farthest]")
print(WSdis2)

## using cosine distance to obtain [nearest,farthest]
dis3= 1-pairwise_distances(winesamples, metric="cosine")
WSdis3=[[4,7],[2,8],[6,7],[2,7],[0,7],[[0,4],7],[2,7],[8,9],[7,9],[6,7]]
print("using cosine distance to obtain [nearest,farthest]")
print(WSdis3)
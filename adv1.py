#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:20:12 2021

@author: antonia
"""

f=open(r'/home/antonia/Documents/adv1.dat','r')
linesf=f.readlines()
data=[]
for x in linesf:
    data.append(float(x.split()[0]))
f.close()
#%%
answer1=0
number=data[0]
for n in data:
    if n>number:
        answer1+=1
    number=n
print(answer1)        
#%%
answer2=0
number=data[0]+data[1]+data[2]
for n in range(1,len(data)-2):
    three_sum=data[n]+data[n+1]+data[n+2]
    if three_sum>number:
        answer2+=1
    number=three_sum
print(answer2)   

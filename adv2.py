#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:20:12 2021

@author: antonia
"""

f=open(r'/home/antonia/Documents/AdventCode/adv2.dat','r')
linesf=f.readlines()
data=[]
for x in linesf:
    data.append(x.split())
f.close()
direction=[]
magnitude=[]
for i in range(0,len(data)):
    direction.append(str(data[i][0]))
    magnitude.append(float(data[i][1]))
#%%
hor_pos=0
depth=0
for n in range(0,len(data)):
    if direction[n]=='forward':
        hor_pos+=magnitude[n]
    if direction[n]=='down':
        depth+=magnitude[n]
    if direction[n]=='up':
        depth-=magnitude[n]
answer1=depth*hor_pos
#%%
hor_pos=0
depth=0
aim=0
for n in range(0,len(data)):
    if direction[n]=='down':
        aim+=magnitude[n]
    if direction[n]=='up':
        aim-=magnitude[n]
    if direction[n]=='forward':
        hor_pos+=magnitude[n]
        depth+=aim*magnitude[n]
answer2=depth*hor_pos
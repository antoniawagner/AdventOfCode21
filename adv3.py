#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:20:12 2021

@author: antonia
"""

f=open(r'/home/antonia/Documents/AdventCode/adv3.dat','r')
linesf=f.readlines()
data=[]
for x in linesf:
    data.append(x.split()[0])
f.close()
#%%
gamma_rate_bin=[]
epsilon_rate_bin=[]
for m in range(0,len(data[0])):
    bin0=0
    bin1=0
    for n in range (0, len(data)):
        if data[n][m]=='0':
            bin0+=1
        else:
            bin1+=1
    if bin0>bin1:
        gamma_rate_bin.append(0)
        epsilon_rate_bin.append(1)
    else:
        gamma_rate_bin.append(1)
        epsilon_rate_bin.append(0)
    gamma_rate = int("".join(str(x) for x in gamma_rate_bin), 2)
    epsilon_rate = int("".join(str(x) for x in epsilon_rate_bin), 2)
answer1=gamma_rate*epsilon_rate
print(answer1)
#%%
oxy_list=data
oxy=0
for m in range(0,len(oxy_list[0])):
    bin0=0
    bin1=0
    oxy_list_m=[]
    if len(oxy_list)==1:
        break
    for n in range (0, len(oxy_list)):
        if oxy_list[n][m]=='0':
            bin0+=1
        else:
            bin1+=1
    if bin0>bin1:
        gamma=0
    else:
        gamma=1
    for n in range (0, len(oxy_list)):
        if oxy_list[n][m]==str(gamma):
            oxy_list_m.append(oxy_list[n])
    oxy_list=oxy_list_m
oxy=int(oxy_list[0],2)


co2_list=data
co2=0
for m in range(0,len(co2_list[0])):
    bin0=0
    bin1=0
    co2_list_m=[]
    if len(co2_list)==1:
        break
    for n in range (0, len(co2_list)):
        if co2_list[n][m]=='0':
            bin0+=1
        else:
            bin1+=1
    if bin0>bin1:
        epsilon=1
    else:
        epsilon=0
    for n in range (0, len(co2_list)):
        if co2_list[n][m]==str(epsilon):
            co2_list_m.append(co2_list[n])
    co2_list=co2_list_m
co2=int(co2_list[0],2)

answer2=oxy*co2
print(answer2)
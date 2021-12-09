#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:20:12 2021

@author: antonia
"""
#%%
with open('/home/antonia/Documents/AdventCode/adv6.dat', 'r') as f:
    linesf=f.read()
    data=([int(num) for num in linesf.split(',')])
#%%
nr_of_days=256
#%%
# =============================================================================
# state=data.copy()
# for day in range(nr_of_days):
#     for fish in range(len(state)):
#         if state[fish]==0:
#             state[fish]=6
#             state.append(8)
#         else:
#             state[fish]-=1
# print(len(state))
# =============================================================================
#%%
z=[data.count(i) for i in range(9)]
for day in range(0,nr_of_days):
    nr_new_cycles=z[0]
    for i in range(0, len(z)-1):
        z[i]=z[i+1]
    z[6]=z[6]+nr_new_cycles
    z[8]=nr_new_cycles
    #print(z)
answer2=sum(z)
print(answer2)
#%%
# =============================================================================
# total_initial_time=[8]*len(data)
# t_0=[total_initial_time[n]-data[n] for n in range(len(data))]
# t=nr_of_days
# tau_0=9
# tau_1=7
# nr_fishes=int(2**((t-tau_0)/tau_1-(t+tau_1)/tau_0))
# print(nr_fishes)
# =============================================================================

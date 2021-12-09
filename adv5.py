#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:20:12 2021

@author: antonia
"""
#%%
dataxy=[]
with open('/home/antonia/Documents/AdventCode/adv5.dat', 'r') as f:
    data=f.read()
    lines=data.split('\n')
    data12=[[entry for entry in line.split(' -> ')] for line in lines if line !='']
    for n in range(0, len(data12)):
        dataxy_line=[]
        for m in range(0,len(data12[n])):
            dataxy_line.append([int(num) for num in data12[n][m].split(',') if num!=''])
        dataxy.append(dataxy_line)
#%%
ver_list=[]
hor_list=[]
for n in range(len(dataxy)):
    if dataxy[n][0][0]==dataxy[n][1][0]: #same x-value
        ver_list.append(dataxy[n])
    if dataxy[n][0][1]==dataxy[n][1][1]: #same y-value
        hor_list.append(dataxy[n])
diag_list=[]
for n in range(len(dataxy)):
    if abs(dataxy[n][0][0]-dataxy[n][1][0])==abs(dataxy[n][0][1]-dataxy[n][1][1]):
        diag_list.append(dataxy[n])
#%%
ver_data_points=[]
for m in range(0,len(ver_list)):
    ver_data_points_list=list(range(min(ver_list[m][0][1],ver_list[m][1][1]),max(ver_list[m][0][1],ver_list[m][1][1])+1))
    for k in range(0, len(ver_data_points_list)):
        ver_data_points.append([ver_list[m][0][0],ver_data_points_list[k]])
#%%
hor_data_points=[]
for m in range(0,len(hor_list)):
    hor_data_points_list=list(range(min(hor_list[m][0][0],hor_list[m][1][0]),max(hor_list[m][0][0],hor_list[m][1][0])+1))
    #print(hor_data_points_list)
    for k in range(0, len(hor_data_points_list)):
        hor_data_points.append([hor_data_points_list[k],hor_list[m][0][1]])
#%%
diag_data_points=[]
for m in range(0,len(diag_list)):
    diag_data_points_x_n=list(range(min(diag_list[m][0][0],diag_list[m][1][0]),max(diag_list[m][0][0],diag_list[m][1][0])+1))
    if diag_list[m][0][0]<diag_list[m][1][0]:
        diag_data_points_x=diag_data_points_x_n
    else:
        diag_data_points_x=diag_data_points_x_n[::-1]
    diag_data_points_y_n=list(range(min(diag_list[m][0][1],diag_list[m][1][1]),max(diag_list[m][0][1],diag_list[m][1][1])+1))
    if diag_list[m][0][1]<diag_list[m][1][1]:
        diag_data_points_y=diag_data_points_y_n
    else:
        diag_data_points_y=diag_data_points_y_n[::-1]
    for k in range(0, len(diag_data_points_x)):
        diag_data_points.append([diag_data_points_x[k],diag_data_points_y[k]])
#%%
data_points=ver_data_points+hor_data_points+diag_data_points
data_points_occuring=[]
for data_point in data_points:
    data_points_occuring.append(data_point) if data_point not in data_points_occuring else data_points_occuring
#%%
occurence_list=[]
for item in data_points_occuring:
    occurence=data_points.count(item)
    if occurence >=2:
        occurence_list.append(occurence)
#%%
answer2=len(occurence_list)
print(answer2)
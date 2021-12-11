import numpy as np
#%%
with open('/home/antonia/Documents/AdventCode/adv11.dat', 'r') as f:
    data=f.read()
    energy_map=[[int(signal) for signal in line] for line in data.split('\n') if line!='']
#%%
steps=0
#for step in range(100): #for part one
flashes=0
flag=True
while flag==True:
    flash_indices=[]
    #substep 1
    for m in range(len(energy_map)):
        for n in range(len(energy_map[m])):
            energy_map[m][n]+=1
            if energy_map[m][n]>9:
                #energy_map[m][n]=0
                flash_indices.append([m,n])
    for [i,j] in flash_indices:
        for k in range(i-1,i+2):
            if k not in [-1,len(energy_map)]:
                for l in range(j-1,j+2):
                    if l not in [-1,len(energy_map[m])]:
                        energy_map[k][l]+=1
                        if energy_map[k][l]>9:
                            flash_indices.append([k,l]) if [k,l] not in flash_indices else flash_indices
    for [r,s] in flash_indices:
        energy_map[r][s]=0
    flashes+=len(flash_indices)
    if len(flash_indices)==100:
        flag=False
    steps+=1 #only for part two
print(steps)
import numpy as np
#%%
with open('/home/antonia/Documents/AdventCode/adv9.dat', 'r') as f:
    data=f.read()
    heightmap=[[int(signal) for signal in line] for line in data.split('\n') if line!='']
#%%
lowest_points=[]
lowest_points_pos=[]
for n in range(len(heightmap)):#rows
    for m in range(len(heightmap[n])):#columns
        adjacents=[]
        if n!=0:
            adjacents.append(heightmap[n-1][m])
        if m!=0:
            adjacents.append(heightmap[n][m-1])
        if n!=len(heightmap)-1:
            adjacents.append(heightmap[n+1][m])
        if m!=len(heightmap[n])-1:
            adjacents.append(heightmap[n][m+1])
        if all(num>heightmap[n][m] for num in adjacents):
            lowest_points.append(heightmap[n][m])
            lowest_points_pos.append([n,m])
print(sum(i+1 for i in lowest_points))
#%%
max_basin=[0]*3
for l in range(len(lowest_points)):
    basin_pos_list=[lowest_points_pos[l]]
    basin_size=0
    k=0
    while k<len(basin_pos_list):
        top=heightmap[basin_pos_list[k][0]-1][basin_pos_list[k][1]]
        left=heightmap[basin_pos_list[k][0]][basin_pos_list[k][1]-1]
        try:
            bottom=heightmap[basin_pos_list[k][0]+1][basin_pos_list[k][1]]
        except:
            IndexError
            bottom=9
        try:
            right=heightmap[basin_pos_list[k][0]][basin_pos_list[k][1]+1]
        except:
            IndexError
            right=9
        if top!=9 and basin_pos_list[k][0]!=0:
            basin_pos_list.append([basin_pos_list[k][0]-1,basin_pos_list[k][1]]) if [basin_pos_list[k][0]-1,basin_pos_list[k][1]] not in basin_pos_list else basin_pos_list
        if bottom!=9:
            basin_pos_list.append([basin_pos_list[k][0]+1,basin_pos_list[k][1]]) if [basin_pos_list[k][0]+1,basin_pos_list[k][1]] not in basin_pos_list else basin_pos_list
        if left!=9 and basin_pos_list[k][1]!=0:
            basin_pos_list.append([basin_pos_list[k][0],basin_pos_list[k][1]-1]) if [basin_pos_list[k][0],basin_pos_list[k][1]-1] not in basin_pos_list else basin_pos_list
        if right!=9:
            basin_pos_list.append([basin_pos_list[k][0],basin_pos_list[k][1]+1]) if [basin_pos_list[k][0],basin_pos_list[k][1]+1] not in basin_pos_list else basin_pos_list
        k+=1
    basin_size=len(basin_pos_list)
    if any(i<basin_size for i in max_basin):
        max_basin[max_basin.index(min(max_basin))]=basin_size
print(np.prod(max_basin))
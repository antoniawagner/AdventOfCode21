import statistics
#%%
with open('/home/antonia/Documents/AdventCode/adv10.dat', 'r') as f:
    data=f.read()
    lines=[line for line in data.split('\n') if line!='']
#%%
chunks=[['(',')'],['[',']'],['{','}'],['<','>']]
points=[3,57,1197,25137]
score=0
corr_line_completion=[]
for line in lines:
    open_chunks=[]
    flag=True
    if flag==True:
        for n in range(len(line)):
            for m in range(len(chunks)):
                if line[n]==chunks[m][0]:
                    open_chunks.append(m)
                if line[n]==chunks[m][1]:
                    if chunks[open_chunks[-1]][1]==line[n]:
                        open_chunks.pop()
                    else:
                        flag=False
                        score+=points[m]
    if flag==True:
        completing_chunks=open_chunks.copy()
        completing_chunks.reverse()
        corr_line_completion.append(completing_chunks)
print(score)
#%%
points2=[1,2,3,4]
score2_list=[]
for line in corr_line_completion:
    score2=0
    for j in range(len(line)):
        score2*=5
        score2+=points2[line[j]]
    score2_list.append(score2)
print(statistics.median(score2_list))
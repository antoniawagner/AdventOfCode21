with open('/home/antonia/Documents/AdventCode/adv6.dat', 'r') as f:
    linesf=f.read()
    data=([int(num) for num in linesf.split(',')])
#%%
nr_of_days=256
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

import sympy as sy
import time
from scipy.optimize import minimize
#%%
#%%
with open('/home/antonia/Documents/AdventCode/adv7.dat', 'r') as f:
    linesf=f.read()
    data=([int(num) for num in linesf.split(',')])
#%%
f1 = lambda x: sum(abs(data[n]-x) for n in range(len(data)))
f2 = lambda x: sum((abs(data[n]-x)**2+(abs(data[n]-x))) /2 for n in range(len(data)))
#%%
x0=0
res1=minimize(f1,x0)
print(f1(round(res1.x[0])))
#%%
start = time.time()
x0=sum(data[n] for n in range(len(data)))/len(data)
res2=minimize(f2,x0)
print(f2(round(res2.x[0])))
end = time.time()
#%%
print('Elapsed time is {} s'.format(end - start))

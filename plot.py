import matplotlib.pyplot as plt
import numpy as np
import pdb
nar=np.array

f1 = open('sigma_table_256.txt','r')
lines = f1.readlines()
f1.close()
mach256=[]
sigma256=[]
for line in lines:
    m,s=nar(line.split('\t'),dtype='float')
    mach256.append(m)
    sigma256.append(s)
mach256=nar(mach256)
f2 = open('sigma_table_1024.txt','r')
lines = f2.readlines()
f2.close()
mach1024=[]
sigma1024=[]
for line in lines:
    m,s=nar(line.split('\t'),dtype='float')
    mach1024.append(m)
    sigma1024.append(s)

plt.clf()
plt.scatter( mach256,sigma256, c='k', label=r'$256^3$')
pfit=np.polyfit(mach256[1:5],sigma256[1:5],1)
#pfit=np.polyfit(mach256,sigma256,1)
plt.plot( mach256, pfit[0]*mach256+pfit[1],c='k')
plt.scatter( mach1024,sigma1024, c='r', label=r'$1024^3$')
plt.legend(loc=0)
plt.xlim(0,8.2)
plt.ylim(0,12)
plt.xlabel('Mach')
plt.ylabel(r'$\sigma_\rho$')
#plt.plot( mach256,sigma256,marker='*')
#plt.plot( mach1024,sigma1024,marker='*')
plt.savefig('resolution.png')

print(lines)

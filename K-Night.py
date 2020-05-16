# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:28:38 2019

@author: osama
"""

x=0
y=0
s=0
M=[64]
G=[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
   
def jump(d):
    if M[s]==0:
        x=x-1*d
        y=y+2*d
    elif M[s]==1:
        x=x-2*d
        y=y+1*d
    elif M[s]==2:
        x=x-2*d
        y=y-1*d
    elif M[s]==3:
        x=x-1*d
        y=y-2*d
    elif M[s]==4:
        x=x+1*d
        y=y-2*d
    elif M[s]==5:
        x=x+2*d
        y=y-1*d
    elif M[s]==6:
        x=x+2*d
        y=y+1*d
    elif M[s]==1:
        x=x+1*d
        y=y+2*d
    
    
    
    

if __name__=='__main__':

    n=8
for x in range(1,n):
    for y in range(1,n):
        G[x][y]=-1
        
        
    for x in range(1,64):
        M[s]=0
    
for s in range(1,64):
    if (x > 0 & x < 8 & y > 0 & y < 8 & G[x][y]==-1):
        G[x][y]=s
    else:
        s=s-1
        jump(-1)
        
while(M[s]==7):
    G[x][y]=-1
    M[s]=0
    s=s-1
    jump(-1)
M[s]=s+1
jump(1)    
        
'''
print is down
'''
for x in range(1,n):
    for y in range(1,n):
        print(G[x][y])
        
   
    
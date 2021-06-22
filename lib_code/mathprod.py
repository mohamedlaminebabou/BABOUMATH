
import numpy as np 
from numba import prange , jit 
import os 
import sys
def sh_b(A):
    t=list(np.asarray(A).shape)
    if len(t)==1:
        return t[0],1
    else:
        return t[0],t[1]
@jit(parallel=True,fastmath=True)
def kroneck(A,B):
    n,m = sh_b(A)
    p,k = sh_b(B)
    return np.array([[A[i,j]*B[s,r] for j in prange(m) for r in prange(k)] for i in prange(n) for s in prange(p)])

@jit(parallel=True,fastmath=True)

def hadamrd(A,B):
    n,m=sh_b(A)
    return np.asarray( [[A[i,j]*B[i,j]  for j in prange(m) ] for i in prange(n) ] )
@jit(parallel=True,fastmath=True)
def khatrirao(a,b):
    return  np.vstack([np.kron(a[:, k], b[:, k]) for k in prange(sh_b(b)[1])]).T

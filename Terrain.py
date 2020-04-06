import array
import random
import sys
import math
import socket
import numpy as np
import random as r

def map(array, size, z):
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(int(np.round((100*(z[i][j]+1))//2)))
        array.append(temp)
    return array
#2D Perlin Noise With Numpy
def perlin(x,y,seed=0):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = x.astype(int)
    yi = y.astype(int)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = fade(xf)
    v = fade(yf)
    # noise components
    n00 = gradient(p[p[xi]+yi],xf,yf)
    n01 = gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = lininterp(n00,n10,u)
    x2 = lininterp(n01,n11,u)
    return lininterp(x1,x2,v)

#linear interpolation
def lininterp(a,b,x):
    return a + x * (b-a)
#6t^5 - 15t^4 + 10t^3
def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3

#grad converts h to the right gradient vector and return the dot product with (x,y)
def gradient(h,x,y):
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h%4]
    return g[:,:,0] * x + g[:,:,1] * y

#initializes terrain
def terrain_generation(size):
    terrain=[]
    lin = np.linspace(0,2,size,endpoint=False)
    x,y = np.meshgrid(4*lin,4*lin) #lin zoom out multiply
    z = perlin(x,y,seed=r.randint(0,1000))
    terrain = map(terrain, size, z)
    return terrain

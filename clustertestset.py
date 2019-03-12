#!/usr/bin/env python
import sys

f = open('testImageReduced','r');
fw = open('clusterResult.txt','w');

def distance(u,v):
    return sum([(x-y)**2 for (x,y) in zip(u,v)])**(0.5)

centroids = []
with open('centroids','r') as f_cent:
    for line in f_cent:
         centroids.append([int (x) for x in line.strip().split(',')])

count = 1;
for line in f:
    line = line.strip()
    coor = [int(x) for x in line.split(',')]
    closestCentroid = 0;
    closestDist = distance(coor,centroids[0]);
    for i in xrange(1,10):
        dist = distance(coor,centroids[i])
        if dist<closestDist:
            closestCentroid = i
            closestDist = dist
    fw.write('image '+str(count)+', '+str(closestCentroid)+'\n')
    count +=1

f.close()
fw.close()

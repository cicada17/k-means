#!/usr/bin/env python
import sys
# f = open('test-images','r');fw = open('mapped','w');
def distance(u,v):
    return sum([(x-y)**2 for (x,y) in zip(u,v)])**(0.5)

centroids = []
with open('centroids','r') as f_cent:
    for line in f_cent:
         centroids.append([int (x) for x in line.strip().split(',')])

# for line in f:
for line in sys.stdin:
    line = line.strip()
    coor = [int(x) for x in line.split(',')]
    closestCentroid = 0;
    closestDist = distance(coor,centroids[0]);
    for i in xrange(1,10):
        dist = distance(coor,centroids[i])
        if dist<closestDist:
            closestCentroid = i
            closestDist = dist
    print str(closestCentroid)+'\t'+line
    # fw.write(str(closestCentroid)+'\t'+line+'\n')
# fw.close()

#!/usr/bin/env python
import sys
# f = open('mapped','r');fw=open('reduced','w');
def distance(u,v):
    return sum([(x-y)**2 for (x,y) in zip(u,v)])**(0.5)

centroids = []
with open('centroids','r') as f_cent:
    for line in f_cent:
         centroids.append([int (x) for x in line.strip().split(',')])

list_assigned_cluster = [];
list_img_coor = [];
# read in data
# for line in f:
for line in sys.stdin:
    assigned_cluster,img_coor = line.strip().split()
    list_assigned_cluster.append(int(assigned_cluster))
    list_img_coor.append([int(x) for x in img_coor.split(',')])

# process separately if there are more than 1 cluster
clusterSet = list(set(list_assigned_cluster))
clusterNum = len(clusterSet)
clusters = [ [list_img_coor[j] for j in xrange(len(list_img_coor)) if (list_assigned_cluster[j]==clusterSet[i])] for i in xrange(clusterNum)]
centroids = [ [0]*784 for i in xrange(clusterNum) ]

# update new centroid
for i in xrange(len(clusters)):
    cluster = clusters[i]
    for k in xrange(784):
        centroids[i][k]=sum([cluster[j][k] for j in xrange(len(cluster))])/len(cluster)
    print ','.join([str(x) for x in centroids[i]])
    # fw.write(','.join([str(x) for x in centroids[i]])+'\n')
# fw.close()

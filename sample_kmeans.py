import random

def distance(u,v):
    return sum([(x-y)**2 for (x,y) in zip(u,v)])**(0.5)

# Initialize variables
dimension = 25;
ImgNum = 60000
steps = 100
Potion = 1;
random.seed(11355);
f = open('trainImageReduced','r')

# Initialize offset list for random access
line_offset = []
offset = 0
for line in f:
    line_offset.append(offset)
    offset += len(line)
f.seek(0)

# Randomly sample a potion of input
coors = [];
for lineNum in random.sample(xrange(ImgNum),int(ImgNum*Potion)):
    f.seek(line_offset[lineNum])
    coor = [int(x) for x in f.readline().strip().split(',')]
    coors.append(coor)

# Randomly assign 10 centroids
centroids = []
for i in random.sample(xrange(len(coors)), 10):
    centroids.append(coors[i])

# Start k-means
for iteration in xrange(steps):
    # assign points to centroid
    clusters = [ [] for i in xrange(10) ]
    for coor in coors:
        closestCentroid = 0;
        closestDist = distance(coor,centroids[0]);
        for j in xrange(1,10):
            dist = distance(coor,centroids[j])
            if dist<closestDist:
                closestCentroid = j
                closestDist = dist
        clusters[closestCentroid].append(coor)
    print [ len(c) for c in clusters ]

    # find new centroid
    summ = [ [] for i in xrange(10) ]
    for i in xrange(len(clusters)):
        cluster = clusters[i]
        cur_sum = 0
        centroids[i]=[0]*dimension
        for k in xrange(dimension):
            centroids[i][k]=sum([cluster[j][k] for j in xrange(len(cluster))])/len(cluster)

        # centroids[i] = [(sum(clusters[i][j][k]) for k in xrange(dimension)) for j in xrange(len(clusters[i]))]
        # for coor in clusters[i]:
        #     sum_dist = sum( [distance(x,coor) for x in clusters[i]] )
        #     if sum_dist>cur_sum:
        #         centroids[i] = coor

    # write result
    with open('SampledCentroids','w') as result:
        for centroid in centroids:
            result.write(','.join([str(x) for x in centroid])+'\n')

f.close()

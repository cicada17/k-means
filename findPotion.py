f = open('clusterResult.txt','r')
tl = open('test-labels.txt','r')

clusters = [ [] for i in xrange(10) ]
for line in f:
    img, clusNum = line.strip().split(',')
    imgNum = int(img.split(' ')[1])
    clusNum = int(clusNum)
    clusters[clusNum].append(imgNum)

for line in tl:
    line = line.strip().split(',')
    imgLabel = [int(x) for x in line]

TotalCorrect = 0;
for i in xrange(10):
    # find major component
    major = -1;
    count = [0] * 10;
    cluster = clusters[i]
    for imgNum in cluster:
        count[imgLabel[imgNum-1]] += 1
    major = count.index(max(count))
    TotalCorrect += max(count)
    accuracy = '{0:.2f}%'.format(max(count)*100.0/len(clusters[i]))
    print i, len(clusters[i]), major, max(count), accuracy
totalsum = sum([len(x) for x in clusters])
print 'Total', totalsum, 'NA', TotalCorrect, TotalCorrect*100.0/totalsum

'''
for i in xrange(10):
    line = ''
    for j in xrange(10):
        line+=(str(clusters[i][j])+'\t')
    print 'Cluster:',i
    print line
'''

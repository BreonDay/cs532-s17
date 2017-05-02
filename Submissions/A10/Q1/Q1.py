#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import operator
count=0
outfile = open ("kValues.txt",'wb')
def dot_product(v1, v2):
    return sum(map(operator.mul, v1, v2))


def vector_cos(v1, v2):
    prod = dot_product(v1, v2)
    len1 = math.sqrt(dot_product(v1, v1))
    len2 = math.sqrt(dot_product(v2, v2))
    return prod / (len1 * len2)


def getdistances(data, vec1):
    distancelist = []

    # Loop over every item in the dataset
    for i in range(len(data)):
        vec2 = data[i]

        # Add the distance and the index
        distancelist.append((vector_cos(vec1, vec2), i))

    # Sort by distance
    distancelist.sort()
    return distancelist

def knnestimate(data, vec1, k=5):
    # Get sorted distances
    dlist = getdistances(data, vec1)
    avg = 0.0
    # Take the average of the top k results
    for i in range(k):
        idx = dlist[i][1]
        avg += idx
    avg = avg / k
    return avg




lines=[]
for line in open("blogdata2.txt"):
    lines.append(line)

blogNames=[]
vectors=[]
words=lines[0].strip().split('\t')[1:]


for line in lines[1:]:
    names=line.strip().split('\t')
    blogNames.append(names[0])
    vectors.append([float(x) for x in names[1:]])
#position of http://ws-dl.blogspot.com/ is 9
#position of http://f-measure.blogspot.com/ is 83
outfile.write ("fmeasure ")
outfile.write ("Web Science ")
print ("f-measure")
print (knnestimate(vectors, vectors[9], 1))
print (knnestimate(vectors, vectors[9], 2))
print (knnestimate(vectors, vectors[9], 5))
print (knnestimate(vectors, vectors[9], 10))
print (knnestimate(vectors, vectors[9], 20))
print ("Web Science")
print (knnestimate(vectors, vectors[83], 1))
print (knnestimate(vectors, vectors[83], 2))
print (knnestimate(vectors, vectors[83], 5))
print (knnestimate(vectors, vectors[83], 10))
print (knnestimate(vectors, vectors[83], 20))
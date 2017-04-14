import clusters 
blognames,words,data=clusters.readfile('blogdata1.txt') # returns blog titles, words in blog (10%-50% boundaries), list of frequency info
clust=clusters.hcluster(data) # returns a tree of foo.id, foo.left, foo.right
clusters.printclust(clust,labels=blognames) # walks tree and prints ascii approximation of a dendogram; distance measure is Pearson's r

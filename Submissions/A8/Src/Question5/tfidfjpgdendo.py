import clusters
blognames,words,data=clusters.readfile('tfidf.txt')
clust=clusters.hcluster(data)
clusters.drawdendrogram(clust,blognames,jpeg='tfidfblogclust.jpg')

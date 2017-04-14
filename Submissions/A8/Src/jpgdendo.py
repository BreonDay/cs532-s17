import clusters
blognames,words,data=clusters.readfile('blogdata1.txt')
clust=clusters.hcluster(data)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

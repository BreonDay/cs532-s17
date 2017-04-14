import clusters

blognames, words, data = clusters.readfile('blogdata1.txt')
kclust=clusters.kcluster(data,k=5)  
k=[blognames[r] for r in kclust[0]]
print str(k) + '\n'

print('k = 10')
kclust = clusters.kcluster(data, k = 10)
k=[blognames[r] for r in kclust[0]]
print str(k) + '\n'

print('k = 20')
kclust = clusters.kcluster(data, k = 20)
k=[blognames[r] for r in kclust[0]]
print str(k)








 

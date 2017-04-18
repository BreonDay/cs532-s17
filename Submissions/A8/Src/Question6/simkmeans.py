import clusters
centroids=[]
blognames, words, data = clusters.readfile('blogdata2.txt')

kclust=clusters.kcluster(data,k=5)  


print ('k=5')
n=0
while(n<5):
    print('[blognames[r] for r in kclust['+str(n)+ ']]')
    s=[blognames[r] for r in kclust[n]]
    n=n+1
    print str(s) + '\n'


kclust = clusters.kcluster(data, k = 10)
print('k = 10')
n=0
while(n<10):
    print('[blognames[r] for r in kclust['+str(n)+ ']]')  
    s=[blognames[r] for r in kclust[n]]
    n=n+1
    print str(s) + '\n'

kclust = clusters.kcluster(data, k = 20)
print('k = 20')
n=0
while(n<20):
    print('[blognames[r] for r in kclust['+str(n)+ ']]')
    s=[blognames[r] for r in kclust[n]]
    n=n+1
    print str(s) + '\n'




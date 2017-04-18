import clusters
blognames,words,data=clusters.readfile('blogdata2.txt')
coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='simblogs2d.jpg')
print('\n')

print("total iterations are:"+str(clusters.getIterations()))

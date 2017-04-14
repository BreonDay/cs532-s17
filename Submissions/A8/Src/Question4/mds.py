import clusters
blognames,words,data=clusters.readfile('blogdata1.txt')
coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')
print('\n')

print("total iterations are:"+str(clusters.getIterations()))

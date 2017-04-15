import sys
import re
searchfile = open("blogs.txt", "r")
outFile=open('uris.txt','wb')
outFile2=open('rssuris.txt','wb')
locations=[]
for line in searchfile:
    if "expref=" in line: locations.append(line)
searchfile.close()
uniqueblogs=set(locations)
blogs=list(uniqueblogs)
for blog in blogs:

    link=re.sub('Location: ', '',blog)
    link2=re.sub('\?expref=next-blog', '',link)
    link3 =re.sub('\^M','',link2)
    uri=link3.replace("\r", "").replace("\n", "")
    outFile.write(uri)
    outFile.write('\n')
    
outFile.write('http://f-measure.blogspot.com/')
outFile.write('\n')
outFile.write('http://ws-dl.blogspot.com/')

for blog in blogs:
    link=re.sub('Location: ','',blog)
    link2 =re.sub('\?expref=next-blog', 'feeds/posts/default?alt=rss',link)
    link3=re.sub('\^M','',link2)
    rss=link3.replace("\r", "").replace("\n", "")
    outFile2.write(rss)
    outFile2.write('\n')

outFile2.write('http://f-measure.blogspot.com/feeds/posts/default?alt=rss')
outFile2.write('\n')
outFile2.write('http://ws-dl.blogspot.com/feeds/posts/default?alt=rss')

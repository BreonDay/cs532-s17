import re
uris=open("uris.txt",'r')
out=open("rssuris.txt",'w')
for  uri in uris:
    rss=re.sub('/ ','.com/feeds/posts/default?alt=rss',uri)
    out.write(rss)
    

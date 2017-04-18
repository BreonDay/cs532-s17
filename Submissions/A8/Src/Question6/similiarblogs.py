import feedparser
import re
import sys
import subprocess
import requests
from BeautifulSoup import *
reload(sys)
sys.setdefaultencoding('utf-8')

outFile=open('similiaruris.txt','wb')
outFile2=open('similiarrss.txt','wb')
rss=""
musicblogrssurls= []
computerscienceurls= []
musicKeywords=["music","techno","rock","rap","dj","song","radio","dancing","dance","pop"]
csKeywords= ["data","science","research","python","java","tech","technology","web","tech","code","coding","c++","program","programming","university","teach","teaching"]


musicCounter=0
csCounter=0

while((  (len(musicblogrssurls)<59) or (len(computerscienceurls)<39)  )):
   try:
      musicCounter=0
      csCounter=0
      global rss
      print("total cs blogs"+str(len(computerscienceurls)))
      print("total music blogs"+str(len(musicblogrssurls)))
      print(len(computerscienceurls)<49)
      print(len(musicblogrssurls)<49)
      r= requests.get('http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117')
      soup=BeautifulSoup(r.text)
      print soup.title.string
      title2=soup.title.string
      title=str(title2)
      #link=soup.find(link)
      link=soup.find('link')['href']
      url=re.sub('\.com/.*','.com/',link)
      rss=re.sub('\.com/','.com/feeds/posts/default?alt=rss',url)
      print link
      print url
      print rss
      #search for key words in title
      for csKeyword in csKeywords:
         if csKeyword in str.lower(title):
            csCounter=+1

      for musicKeyword in musicKeywords:
         if musicKeyword in str.lower(title):
            musicCounter+=1
        # search for keywords in subtitles
      for subTitle in soup(parseOnlyThese=SoupStrainer('title')):
         for csKeyword in csKeywords:
            if csKeyWord in str.lower(subTitle):
               csCounter=+1
         for musicKeyword in musicKeywords:
            if musicKeyword in str.lower(subTitle):
               musicCounter+=1
        #if they have a description  search for keywords here as well
      try:
         metadescription=soup.find('meta',property="og:description")
         desc=metadescription['content']
         description=str(desc)
         print(description)
         for csKeyword in csKeywords:
            if csKeyword in str.lower(description):
               csCounter+=1
         for musicKeyword in musicKeywords:
            if musicKeyword in str.lower(description):
               musicCounter+=1
      except:
         continue
      #search for keywords in body
      print(musicCounter)
      print(csCounter)
      #if the blog is music or cs related find out what the blog focuses more on then add to the rssurl list
      if ((musicCounter or csCounter)>0):
         global computerscienceurls,musicblogrssurls
         if ((csCounter>musicCounter) and (len(computerscienceurls)<39)):
            global rss
            print("added csblog")
            musicCounter=0
            csCounter=0
            computerscienceurls.append(rss)
            outFile2.write(rss)
                
         elif (musicCounter==csCounter):
            print("tied so skipping")
            musicCounter=0
            csCounter=0
         elif ((musicCounter>csCounter) and (len(musicblogrssurls)<59)):
            global rss
            print("added musicblog")
            musicCounter=0
            csCounter=0
            musicblogrssurls.append(rss)
            outFile2.write(rss)

         elif():
            print("doing nothing")
                

   except:
      continue
print(computerscienceurls)
print(musicblogrssurls)
outFile2.write('http://f-measure.blogspot.com/feeds/posts/default?alt=rss')
outFile2.write('\n')
outFile2.write('http://ws-dl.blogspot.com/feeds/posts/default?alt=rss')

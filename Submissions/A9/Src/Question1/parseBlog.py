
import re
import feedparser
import sys

numEntries=0
reload(sys)
sys.setdefaultencoding('utf-8')



d=feedparser.parse('https://www.theguardian.com/books/rss')
summaries= []
titles = []

outFile1= open ('titles2.txt','wb')
outFile2=open('summaries2.txt','wb')
outFile3= open('combinedsumtitle2.txt','wb')
def parsePost(summary,title):
    global numEntries
    print '\n'
    numEntries=numEntries+1

    print numEntries
    print title
    #original comparison
    print summary
    print '\n'
    #removes tags
    replaced2= re.sub('<[^>]*>',' ', summary)
    #removes unnessacary continue reading tag at end
    replaced3= re.sub('   Continue reading...','',replaced2)
    #gets rid of the double spaces the original tag removal could of caused
    replaced4= re.sub('  ',' ',replaced3)
   # print title
    #print replaced4
    #return replaced4

    sumTitle=title+" "+replaced4
    sumTitle2=re.sub("'","\\\\'",sumTitle)
    sumTitle3=re.sub('"','',sumTitle2)
    sumTitle4=re.sub("`",'',sumTitle3)
    print sumTitle4
    return title,replaced4,sumTitle4
    print '\n'



for e in d.entries:
#    numEntries=numEntries+1

    if 'summary' in e:
        summary = e.summary
    else:
        summary = e.description


    parsedtitle, parsedsummary, combinedsumtitle =parsePost(summary,e.title)

    outFile1.write(parsedtitle)
    outFile1.write('\n')
    outFile2.write(parsedsummary)
    outFile2.write('\n')
    outFile3.write(combinedsumtitle)
    outFile3.write('\n')


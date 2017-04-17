#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import re
import sys
import math

reload(sys)

sys.setdefaultencoding('utf-8')


def tf(wordcount,totalwords):

    return (float((wordcount))/(totalwords))



def idf(totalDocuments,numDocsWithWord):

    return(math.log(float((totalDocuments))/float(1+numDocsWithWord),2))

def tfidf(wordcount,totalwords,totalDocuments,numDocsWithWord):
    return (float(tf(wordcount,totalwords)*idf(totalDocuments,numDocsWithWord)))

def getwordcounts(url):

    '''
    Returns title and dictionary of word counts for an RSS feed
    '''
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}
    totalwords=0
    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary

        else:
            summary = e.description

        # Extract a list of words## and count the total words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
            totalwords+=1

    return (d.feed.title, wc,totalwords)


def getwords(html):
    totalwords=0
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    
            
        
    # Convert to lowercase
    return [word.lower() for word in words if word != '']
totaldocs=0
totalwords= {}
apcount = {}
wordcounts = {}
feedlist = [line for line in file('rssuris.txt')]
for feedurl in feedlist:
    try:
        #return the title and the word count from each parsed rss link
        (title, wc,sumwords) = getwordcounts(feedurl)
        #store the word counts and total words by the title they identify as
        wordcounts[title] = wc
        totalwords[title]= sumwords
        #wc.items rreturns key and value dict pair  (word,count) is serving as x,y for two values to be thrown in
        # basically this is saying for every entry in wc see if it appears more then once in the list of docs and add to the count if so 
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
        totaldocs+=1
    except:
        print 'Failed to parse feed %s' % feedurl

# the hack mentioned that needs to be removed
wordlist = []
#apcount.items() returns key value pairs
#so for every pair store in w and bc then do y

for (w, bc) in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.6:
        wordlist.append(w)

#matrix creation
out = file('tfidf.txt', 'w+')
out.write('Blog')

for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')

for (blog, wc) in wordcounts.items():
    print blog
    out.write(blog)
    for word in wordlist:
        if word in wc:
            
           # print("word count is"+str(wc[word]))
           # print("totalwords are"+str(totalwords[wc]))
           # print("totaldocs are"+str(totaldocs))
           # print("word occurences are"+str(apcount[word]))
           # print("tf value is"+str(tf(wc[word],totalwords[blog])))
           # print("idf value is" +str(idf(totaldocs,apcount[word])))
           # print( tfidf( wc[word],totalwords[blog],totaldocs ,apcount[word]))
           
#            print(tf(wc[word],totalwords[blog]))
            tf2=tf(wc[word],totalwords[blog])
            idf2=idf(totaldocs,apcount[word])
            print(str(blog)+" has "+ str(totalwords[blog])+"checking word"+str(word)+"which has a word count of"+str(wc[word]))
            
            print("tf ="+str(tf2))
            print("idf2="+str(idf2))
            tfidf2=float(tf2*idf2)
            print(tfidf2)
            
            out.write('\t%f' %tfidf( wc[word],totalwords[blog],totaldocs ,apcount[word]))
        else:
            out.write('\t0')
    out.write('\n')










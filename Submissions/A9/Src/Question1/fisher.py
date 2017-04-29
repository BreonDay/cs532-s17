# coding: utf-8
import docclass

#open file where titles are stored
outFile1= open ('titles2.txt','r')
#open file where categories are stored
outFile2=open('categories2.txt','r')
#open file where title+summarys are stored
outFile3= open('combinedsumtitle2.txt','r')
outFile4 = open('50predictions.txt','wb')
outFile5 = open('10predictions.txt','wb')
count=1
titles=[]
categories=[]
predictions=[]
amountTrained=0
summaryTitles=[]
trainingCount1=50
trainingCount2=90
maxTrainingData=100
remainingClassifications=0

#populate lists with files

for entry in outFile1:
    titles.append(entry)
for entry in outFile2:
    categories.append(entry)
for entry in outFile3:
    summaryTitles.append(entry)

#summaryTitles
cl=docclass.fisherclassifier(docclass.getwords)
#delete min.db file in project after every run
cl.setdb('mln.db')


#train the first   entries in the summaryTitle txt file
for entry in summaryTitles:

    #train first 50
    #if count<trainingCount1:
    #train first 90
    if count < trainingCount2:
        docclass.mytraining(cl,entry,categories[count])
        count+=1

# classify the remaing x entries
predictionsToDO=maxTrainingData-count
predictionsDone=0
while count<maxTrainingData:
    print count
    prediction=cl.classify(summaryTitles[(count)])
    predictions.append(prediction)
    count+=1
# check the results
while predictionsDone  <predictionsToDO:
    print(predictionsDone)
    print(predictionsToDO)
    print(maxTrainingData-predictionsDone)
    print titles[(maxTrainingData-predictionsDone)-1]
    print predictions[(predictionsDone)]
    predictionsDone+=1

print len(predictions)
for prediction in predictions:
    if len(predictions)==50:
        outFile4.write(prediction)
    elif len(predictions)==10:
        outFile5.write(prediction)



#---------------------------- debug tests---------------------------
#titles= ["Nobody owns the water.","the quick rabbit jumps fences","buy pharmaceuticals now",
 #        "make quick money at the online casino","the quick brown fox jumps"]
#categories=["good","good","bad","bad","good"]

#docclass.sampletrain(cl)
#for title in titles:
  #  print title
    #print categories[count]
   # docclass.testsampletrain(cl,title,categories[count])
    #count+=1
#my train function
#test=cl.fisherprob('money buy','bad')
#test2=cl.classify('quick money')
#test=cl.classify('The Clocks in This House All Tell Different Times by Xan Brooks review – a dark, enchanted debut Set in the aftermath of the first world war, this is a twisted fairytale populated by wounded servicemen, establishment radicals and a ‘discount Aleister Crowley’ It’s 1923. Lucy Marsh and her friend Winifred, mid-teenagers from an enclave of dying pubs and dead industries in north-east London, find themselves effectively sold into prostitution by their families. Once a week in Epping Forest they meet with and service four bizarrely wounded ex‑servicemen who have given arms, legs, hands and faces for their country in the recent world war. Lucy isn’t sure if they’re named after Dorothy’s companions in The Wonderful Wizard of Oz , or if the characters in the story were named after them. The “funny men” seem as decent as they are damaged, puzzled to the point of inarticulacy by the things that have happened to them. But though they’re shy they know what they’ve lost – homes, wives, children, physical comfort, any sense of themselves as welcome in the society that sent them to fight – and they know what they want, at least from Lucy and Winifred. Xan Brooks’ first novel quickly normalises both the bizarreness and the unspoken brutality of the situation. Much of this depends on Lucy’s adaptability: throughout, she treats her clients – and indeed everyone she meets – with a kind of bemused generosity. The reader is less tempted. The funny men subsist on the charity of “the Pink Earl”, an establishment radical, and his vile son Rupert Fortnum-Hyde, whose 5,000-acre estate “rolls out on either side of the river Lea”. Their holdings include “a sugar estate in Jamaica, 12 London townhouses and an ongoing stake in the British South Africa Company”. Despite this, both conceive of themselves somehow as socialists; in addition the son presents himself as ;an experimentalist of human beings, a force for modernity and change. He surrounds himself with a permanent carnival of jazz musicians, confused interwar intellectuals, a “discount Aleister Crowley ” who has somehow failed to monetise the ability to conjure genuine flames from his fingertips, and ;a female north African camel called Edith. Everyone but the camel, including Lucy and Winifred, is plied with vast quantities of cocaine, “a drug for action, a drug for doers”, the “taste of the future” – although their only future is to be abandoned the moment Fortnum-Hyde becomes bored. ')
#print test
#print test2


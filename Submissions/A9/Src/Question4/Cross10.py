# coding: utf-8
import docclass


#open file where titles are stored
outFile1= open ('titles2.txt','r')
#open file where categories are stored
outFile2=open('categories2.txt','r')
#open file where title+summarys are stored
outFile3= open('combinedsumtitle2.txt','r')

titles=[]
categories=[]
summaryTitles=[]
#populate lists with files
for entry in outFile1:
    titles.append(entry)
for entry in outFile2:
    categories.append(entry)
for entry in outFile3:
    summaryTitles.append(entry)



count=0

count2=0
#change this variable every one to get the values 1=0-9 10=90-99
n=10

filename="CrossValidation" + str(n*10)+".txt"
outFile4=open(filename,"wb")
cl=docclass.fisherclassifier(docclass.getwords)
#delete min.db file in project after every run
cl.setdb('mln2.db')

#create cross 10 sublists
summariesToBeClassified=  summaryTitles[((n-1)*10):(n*10)]
sublist2=  summaryTitles[:(n-1)*10]
sublist3=  summaryTitles[(n)*10:]
trainingdata_Entries= sublist2+sublist3

#
categoriesToBeClassified=  categories[((n-1)*10):(n*10)]
sublist5=  categories[:(n-1)*10]
sublist6=  categories[(n)*10:]
trainingdata_Categories= sublist5+sublist6

# train it based on what was given
#for entry in trainingdata_Entries:
#    if count < 90:
#        docclass.mytraining(cl, entry, trainingdata_Categories[count])
#        count += 1
while count < 90:
        docclass.mytraining(cl, trainingdata_Entries[count], trainingdata_Categories[count])
        count += 1
count =0

while count2<10:
    print count2
    print summariesToBeClassified[(count2)]
    prediction = cl.classify(summariesToBeClassified[(count2)])
    outFile4.write(prediction)
    count2+=1

#classify the to be classified
#for test in summariesToBeClassified:
   # print count
    #prediction=cl.classify(test[(count)])
 #   count+=1
   # outFile4.write(prediction)

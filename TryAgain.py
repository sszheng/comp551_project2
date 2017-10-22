# -*- coding: utf-8 -*-
import re
import itertools
import nltk
import csv
from nltk.util import ngrams


def word_grams(words,n):
    s = []
    for ngram in ngrams(words, n):
        s.append(' '.join(str(i.encode('utf-8')) for i in ngram))
    return s


def paraseData_ngram(n,ngramss,class_probability,occur):
    myre = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    with open('train_set_x.csv','rb') as trainx, open('train_set_y.csv','rb') as trainy:
        class_reader=csv.reader(trainx,delimiter=',')
        result_reader=csv.reader(trainy,delimiter=',')
        next(class_reader)
        next(result_reader)
        i=0
        for row1,row2 in itertools.izip(class_reader,result_reader):  
            text_deleteurl = re.sub(r"http\S+","", row1[1])
            text_deletenum=re.sub("\d+","",text_deleteurl)
            text_deleteemoji=myre.sub('',text_deletenum.decode('utf8'))
            l=text_deleteemoji.replace(" ","").lower()
            s=word_grams(l,n)
            lt=int(row2[1])
            class_probability[lt]=class_probability[lt]+1;
            
            for gram in s:
                if not ngramss[lt].has_key(gram):
                   ngramss[lt].update({gram:1})
            else:
                try:
                    
                   ngram_occurrences = ngramss[lt][(gram)]
                   ngramss[lt].update({gram:ngram_occurrences+1})
                except Exception:
                    pass

    #class probability
    total=0
    for x in range(0,5):
        total=total+class_probability[x]
    for x in range(0,5):
        class_probability[x]=float(class_probability[x])/total
        
    #probability of each word
    vocabulary=0
    for x in range(0,5):
        vocabulary=vocabulary+len(ngramss[x])
    for x in range(0,5):
        occur[x]=vocabulary
    for x in range(0,5):
        for key in ngramss[x]:
            occur[x]=occur[x]+ngramss[x][key]

    #probability of each word
    for x in range(0,5):
        for key in ngramss[x]:
            ngramss[x][key]=(float(ngramss[x][key]+1))/occur[x]

def tellme(ngramss,class_probability,occur,n):
        myre = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

        with open('test_set_x.csv','rb') as test, open('nb.csv','wb') as output:
            output.write("Id,Category")
            output.write("\n")
            test_reader=csv.reader(test,delimiter=',')
            next(test_reader)
            i=0
            for row1 in test_reader:  
                test_probability=[]
                for x in range(0,5):
                    test_probability+=[class_probability[x]]
                text_deleteurl = re.sub(r"http\S+","", row1[1])
                text_deleteemoji=myre.sub('',text_deleteurl.decode('utf8'))
                l=text_deleteemoji.replace(" ","").lower()
                s=word_grams(l,n)
                for x in range(0,5):
                    for y in s:
                        if ngramss[x].has_key(y):
                            test_probability[x]=test_probability[x]*ngramss[x][y]
                        else:
                            test_probability[x]=test_probability[x]/float(occur[x])
                maxprob=0
                maxindex=0
                for x in range (0,5):
                    if(test_probability[x]>maxprob):
                        maxprob=test_probability[x]
                        maxindex=x
 
                output.write(str(i))
                output.write(",")
                output.write(str(maxindex))
                output.write("\n")
                i=i+1
            
        
        
n=1
ngramss=[{},{},{},{},{}]
class_probability=[0,0,0,0,0]
occur=[0,0,0,0,0]
paraseData_ngram(n,ngramss,class_probability,occur)
#print ngramss[1]
print class_probability
print occur
tellme(ngramss,class_probability,occur,1)

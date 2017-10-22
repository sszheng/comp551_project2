import csv
import sys
import re
import itertools
import random
import math

reload(sys)
sys.setdefaultencoding('utf8')
sys.maxunicode
prase_data=[]
class_probability=[0,0,0,0,0]
Dicts=[{},{},{},{},{}]

occur_plus_vocabulary=[]
i=0
myre = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

train=[]
result=[]
def parase(train,result):
    with open('train_set_x.csv','rb') as trainx, open('train_set_y.csv','rb') as trainy:
        class_reader=csv.reader(trainx,delimiter=',')
        result_reader=csv.reader(trainy,delimiter=',')
        next(class_reader)
        next(result_reader)
        i=0
        for row1,row2 in itertools.izip(class_reader,result_reader):
            #l=row1[1].replace("...", "")
            #text_deleteurl = re.sub(r"http\S+","", l)
            #text_deletenum=re.sub("\d+","",text_deleteurl)
            #text_deleteemoji=myre.sub('',text_deletenum.decode('utf8'))
            #l=list(text_deleteemoji)
            l=tuple(row1[1].decode('utf8').lower())
            train+=[l]
            result+=[int(row2[1])]

def charProbability(train,result,n,Dicts,occur_plus_vocabulary,start,stop):
    occur=[]
    vocabulary=0
    for k in range(start,stop):
        l=train[k]
        t=result[k]
        for x in range (0,len(l)-n+1):            
            if(l[x:x+n] in Dicts[t]):
               Dicts[t][l[x:x+n]]=Dicts[t][l[x:x+n]]+1
               
            else:
               Dicts[t][l[x:x+n]]=1
    for x in range(0,5):
        vocabulary=vocabulary+len(Dicts[x])
        print len(Dicts[x])
    for x in range(0,5):
        occur+=[0]
        occur_plus_vocabulary+=[0]
            
    for x in range(0,5):
        for key in Dicts[x]:
            occur[x]=occur[x]+Dicts[x][key]
            
    for x in range(0,5):
        occur_plus_vocabulary[x]=occur[x]+vocabulary

    #probability of each word

    for x in range(0,5):
        for key in Dicts[x]:
            Dicts[x][key]=(float(Dicts[x][key]+1))/occur_plus_vocabulary[x]
            if(Dicts[x][key]==0):
               print 'stop at dictsssss'
               sys.exit()
            


def classProbability(class_probability,start,stop,result):
    for row in result:
        class_probability[row]=class_probability[row]+1;
    total=0
    for x in range(0,5):
        total=total+class_probability[x]
    for x in range(0,5):
        class_probability[x]=float(class_probability[x])/total
def cross_validation(Dicts,n,occur_plus_vocabulary,class_probability,start,stop):
    same=0
    notsame=0
    for k in range(start,stop):
        row2=result[k]
        test_probability=[class_probability[0],class_probability[1],class_probability[2],class_probability[3],class_probability[4]]
        l=train[k]

        for x in range(0,5):
            for y in range (0,len(l)-n+1):
                if(l[y:y+n] in Dicts[x]):
                    test_probability[x]=test_probability[x]*Dicts[x][l[y:y+n]]
                   # if(test_probability[x]==0):
                       # print 'stop at dicts'
                        #sys.exit()
                else:
                    test_probability[x]=test_probability[x]/float(occur_plus_vocabulary[x])
                    #if(test_probability[x]==0):
                       # print 'stop at occurs'
                        #sys.exit()
        #if (test_probability[0]==0):t=t+1
        maxprob=test_probability[0]
        maxindex=0
        for x in range (0,5):
            if(test_probability[x]>maxprob):
                maxprob=test_probability[x]
                maxindex=x
        if(l==()):maxindex=random.choice([1,2,3])
                
        if(maxindex==row2):
            same=same+1
        else:
            notsame=notsame+1
    print same
    print notsame
    print float(same)/(same+notsame)
        
def tellme(Dicts,n,occur_plus_vocabulary,class_probability):
        same=0
        notsame=0
        with open('test_set_x.csv','rb') as test, open('nb.csv','wb') as output, open('lo.csv','rb') as trainy:
            
            output.write("Id,Category")
            output.write("\n")
            test_reader=csv.reader(test,delimiter=',')
            result_reader=csv.reader(trainy,delimiter=',')
            next(test_reader)
            next(result_reader)
            i=0
            t=0
            for row1,row2 in itertools.izip(test_reader,result_reader):
                test_probability=[class_probability[0],class_probability[1],class_probability[2],class_probability[3],class_probability[4]]
                #l=row1[1].replace("...", "")
              #  text_deleteurl = re.sub(r"http\S+","", l)
               # text_deletenum=re.sub("\d+","",text_deleteurl)
               # text_deleteemoji=myre.sub('',text_deletenum.decode('utf8'))
               # l=tuple(text_deleteemoji.lower())
                l=tuple(row1[1].decode('utf8').lower())
                for x in range(0,5):
                    for y in range (0,len(l)-n+1):
                        if(l[y:y+n] in Dicts[x]):
                            test_probability[x]=test_probability[x]*Dicts[x][l[y:y+n]]
                            if(test_probability[x]==0):
                                print 'stop at dicts'
                                #sys.exit()
                        else:
                            test_probability[x]=test_probability[x]/float(occur_plus_vocabulary[x])
                            if(test_probability[x]==0):
                                print 'stop at occurs'
                                #sys.exit()
                if (test_probability[0]==0):t=t+1
                maxprob=test_probability[0]
                maxindex=0
                for x in range (0,5):
                    if(test_probability[x]>maxprob):
                        maxprob=test_probability[x]
                        maxindex=x
                if(row1[1]==''):maxindex=random.choice([1,2,3])
                        
                if(maxindex==int(row2[1])):
                    same=same+1
                else:
                    notsame=notsame+1
                output.write(str(i))
                output.write(",")
                output.write(str(maxindex))
                output.write("\n")
                i=i+1
        print t
        print same
        print notsame
        print float(same)/(same+notsame)


parase(train,result)
charProbability(train,result,1,Dicts,occur_plus_vocabulary,0,len(result))
#paraseData_ngram(1,Dicts,occur_plus_vocabulary)
classProbability(class_probability,0,len(result),result)
tellme(Dicts,1,occur_plus_vocabulary,class_probability)

#cross_validation(Dicts,1,occur_plus_vocabulary,class_probability,0,len(result))




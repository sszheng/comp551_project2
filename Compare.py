import csv
import sys
import re
import itertools
import random

reload(sys)
sys.setdefaultencoding('utf8')
sys.maxunicode
prase_data=[]
class_probability=[]
Dicts=[]

occur_plus_vocabulary=[]
#f=open('myfile.txt','w')
i=0
myre = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')


def tellme():
        same=0
        notsame=0
        with open('nbs.csv','rb') as test, open('library_logistic_output.csv','wb') as output, open('train_set_y.csv','rb') as trainy:
            output.write("Id,Category")
            output.write("\n")
            test_reader=csv.reader(test,delimiter=',')
            result_reader=csv.reader(trainy,delimiter=',')
            next(test_reader)
            next(result_reader)
            i=0
            for row1,row2 in itertools.izip(test_reader,result_reader):  
                if(int(row1[1])==int(row2[1])):
                    same=same+1
                else:
                    output.write(row1[0])
                    output.write(",")
                    output.write((row1[1]))
                    output.write(",")
                    output.write(row2[1])
                    output.write("\n")
                    notsame=notsame+1
                    
                i=i+1
        print same
        print notsame
        print float(same)/(same+notsame)
tellme()








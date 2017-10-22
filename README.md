# comp551_project2
-Overview
This file is about instruction for how to run Naive.py. By defualt, we use unigram and we train all the train set to get the Model. 
We produce a nb.csv to produce prediction for all test data in 'test_set_x.csv'

How to use Naive.py
       you can just run python Naive.py to have an nb.csv file for the result for test_set_x.py 
       If you want to change test or train file, by just replace 'train_set_x.csv' and 'train_set_y.csv' and 'test_set_x.csv' in the file.

Function descriptions in details:
parase(train,result):
       This function is write to parse the raw train data.
       train, result are two list defined in Naive.py to store train data input and train data result
       here train is implemented as a list of tuple in order to be used in the dictionary, result is implemented as a list of int.
       parase(train,result) will by defualt open 'train_set_x.csv' as raw train data and by default open 'train_set_y.csv' as raw result data.
       You can change theses two file in the parase function to change train input and trian result.
       
gramProbability(train,result,n,Dicts,occur_plus_vocabulary,start,stop):
       This function calculate all char probability p(x|y) using formular p(x|y)=(times of gram x occurs in class y+1) \(vocabulay+total times of all grams occur in y )
       train result are two list descripted as in parase(train, result)
       n is indicated as number of grams. If n is a 1, then it will be unigram. If 2 is indicated as number 2-gram......
       Dicts is a [{}{}{}{}{}] to stored key as tuple gram and value as p(x|y) for all 5 languages.
       occur_plus_vocabulary is a [int,int,int,int,int] to store the number of vocabulary+ocabulay+total times of all grams occur in y for different languages.
       start is a int where you want to start to use the train data.
       stop is a int where you want to stop to use the train data.
       for example, if you want to use train set from 0 to half, you can write start as 0 and stop as half of the train data length
       
classProbability(class_probability,start,stop,result):
       class_probability is an [float,float,float,float,float] to store the probability of the each class occurence in train set
       
cross_validation(Dicts,n,occur_plus_vocabulary,class_probability,start,stop):

tellme(Dicts,n,occur_plus_vocabulary,class_probability):
       predict the result for test set.
       Dicts is the dictionary we gathering from the train set. n is the n-gram.
       If you want to try different test set, you can change the name in hte with open(......)
       
       
   
       


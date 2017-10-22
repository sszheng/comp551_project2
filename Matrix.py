import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import sys  


train_x = []
with open("newfile.txt","r") as input_file:
    for row in input_file:
        train_x.append(row)

vec = TfidfVectorizer(decode_error='ignore',analyzer='char')
vec.fit_transform(train_x)
idf = vec.idf_
defidf_dic= dict(zip(vec.get_feature_names(), idf))
for x in defidf_dic:
    print(x,defidf_dic[x])
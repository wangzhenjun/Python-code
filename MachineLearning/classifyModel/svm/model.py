#-*- coding:utf-8 -*-
import numpy as np
from sklearn import svm,tree

trainPath = "./KaggleEvergreenData/train.csv"
testPath = "./KaggleEvergreenData/test.csv"


#caculate
def accuracy(predict,actual):
    acc=[]
    for i in range(len(predict)):
        if predict[i]==actual[i]:
            acc.append(1)
        else:
            acc.append(0)
    return acc


#svmClassifier
clf = svm.SVC()
clf = clf.fit(trainX,trainY)
predict = clf.predict(testX)

svmCorrect = accuracy(predict.tolist(),testY.tolist())
svmAccuracy = sum(svmCorrect)*1.0/len(testY)
print "Accuracy of svm is:\t",svmAccuracy

#DecisionTree Classifier
dtclf = tree.DecisionTreeClassifier()
dtclf = dtclf.fit(trainX,trainY)
predict = dtclf.predict(testX).tolist()

dtCorrect = accuracy(predict,testY.tolist())

dtAccuracy = sum(dtCorrect)*1.0/len(dtCorrect)
print "Accuracy of DecisionTree is:\t",dtAccuracy

#feature standard
from sklearn import preprocessing
trainX = preprocessing.scale(trainX)
testX = preprocessing.scale(testX)

print trainX
#svm classify of feature standard
svmclfOfstandard = svm.SVC()
svmclfOfstandard = svmclfOfstandard.fit(trainX,trainY)
predict = svmclfOfstandard.predict(testX)
svmCorrectOfstandard = accuracy(predict.tolist(),testY.tolist())
svmAccuracyOfstandard = sum(svmCorrect)*1.0/len(testY)
print "Accuracy of svmOfstandard is:\t",svmAccuracyOfstandard



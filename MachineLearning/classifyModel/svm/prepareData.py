#-*- coding:utf-8 -*-

import os
import random
import csv

dataPath = "E:\\DataSet\\Kaggle.StumbleUpon evergreen\\train.tsv"
trainPath = "./KaggleEvergreenData/train.csv"
testPath = "./KaggleEvergreenData/test.csv"
#read data
def readData(path):
    dataSet = []
    label = []
    fr = open(dataPath)
    fr.readline()
    for i in fr.readlines():
        temp = []
        info = i.strip().split('\t')
        info = map(lambda x:x.replace("\"",""),info)
        temp.append(float(info[5]))
        for t in info[5:-1]:
            if t == '?':
                temp.append(0.0)
            else:
                temp.append(float(t))
        temp.append(int(info[-1]))
        dataSet.append(temp)
    return dataSet

#splite data to trainData,testData
def splitData(data,M=8):
    trainData = []
    testData = []
    for i in data:
        if random.randint(0,9)>=M:
            testData.append(i)
        else:
            trainData.append(i)
    return trainData,testData


#write data to csv
def writeTocsv(path,data):

    filecsv = file(path,'wb')
    writer = csv.writer(filecsv)
    writer.writerows(data)
    filecsv.close()

data  = readData(dataPath)
train,test = splitData(data,M=8)

writeTocsv(trainPath,train)
writeTocsv(testPath,test)



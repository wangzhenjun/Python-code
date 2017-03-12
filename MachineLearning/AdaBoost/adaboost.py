# _*_coding:utf-8

from numpy import *

def loadSimpleData():
    dataMat = matrix([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,2.]])
    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return dataMat,classLabels

if __name__ == '__main__':
    dataMat,classLabels = loadSimpleData()
    print dataMat
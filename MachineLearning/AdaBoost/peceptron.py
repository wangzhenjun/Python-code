import numpy as np
import matplotlib.pyplot as plt

def load_data():
    data = [[3,3],[4,3],[1,1]]
    xArray = np.array([3,3,4,3,1,1])
    xArray = xArray.reshape((3,2))
    yArray = np.array([1,1,-1])
    return data,xArray,yArray

class pictrue:
    def __init__(self,data,w,bias):
        self.data = data
        self.w = w
        self.bias = bias
        plt.figure(1)
        plt.title('Plot1',size=14)
        plt.xlabel('x-axis',size=14)
        plt.ylabel('y-axis',size=14)
        plt.scatter(self.data[0][0],self.data[0][1],s=50)
        plt.scatter(self.data[1][0],self.data[1][1],s=50)
        plt.scatter(self.data[2][0],self.data[2][1],marker='x',s=50)

        xdata = np.linspace(0,5,100)
        ydata = self.expresion(xdata)
        plt.plot(xdata,ydata,color='r',label='y1 data')
    def expresion(self,x):
        y = (-self.bias-self.w[0]*x)/self.w[1]
        return y
    def show(self):
        plt.show()
class perceptron:
    def __init__(self,x,y,a=1):
        self.x = x
        self.y = y
        self.w = np.array([0,0])
        self.b = 0
        self.a = 1
    def sign(self,w,b,x):
        y = np.dot(w,x)+b
        return int(y)
    def train(self):
        flag = True
        length = len(self.x)
        while flag:
            count = 0
            for i in range(length):
                tmpY = self.sign(self.w,self.b,self.x[i,:])
                if tmpY*self.y[i]<=0:
                    tmp = self.y[i]*self.x[i,:]*self.a
                    self.w = self.w+tmp
                    self.b = self.b+self.y[i]*self.a
                    count+=1
            if count == 0:
                flag = False
        return self.w,self.b

data,xArray,yArray = load_data()
mypreceptron = perceptron(x=xArray,y=yArray)
weights,bias = mypreceptron.train()
print weights,bias
mypictrue = pictrue(data,weights,bias)
mypictrue.show()

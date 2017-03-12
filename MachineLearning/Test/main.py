import matplotlib.pyplot as plt
import math
x = 1.50
X = []
Y = []
for i in xrange(500):
    X.append(i);
    x = x-0.01*4*math.pow(x,3)
    Y.append(x)
plt.plot(X,Y,color = 'r',)
plt.show()

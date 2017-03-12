#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([[1,2],
                    [2,1],
                    [2,3],
                    [3,5],
                    [1,3],
                    [4,2],
                    [7,3],
                    [4,5],
                    [11,3],
                    [8,7]
                    ])
y_train = np.array([7,8,10,14,8,13,20,16,28,26])
x_test = np.array([[1,4],
                   [2,2],
                   [2,5],
                   [5,3],
                   [1,5],
                   [4,1]
                   ])
alpha = 0.001
a = np.random.normal()
print a
b = np.random.normal()
c = np.random.normal()
def h(x):
    return a*x[0]+b*x[1]+c
for i in range(1000):
    sum_a = 0.0
    sum_b = 0.0
    sum_c = 0.0
    for x, y in zip(x_train,x_test):
        for xi in x:
            sum_a = sum_a + alpha * (y-h(x)) * xi
            sum_b = sum_b + alpha * (y-h(x)) * xi
            #sum_c = sum_c = alpha * (y-h(x)) * xi
    print sum_a
    a = a + sum_a
    b = b + sum_b
    c = c + sum_c

print a#,'\t',b,'\t',c

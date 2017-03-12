import sys
import os
# path = "D:\\Users\\wzhj\\MachineLearning\\recogImage\\libsvm-master\\python"
# os.chdir(path)

from svm import *
from svmutil import *


y, x = [1,-1], [{1:1, 2:1}, {1:-1,2:-1}]
prob  = svm_problem(y, x)
param = svm_parameter('-t 0 -c 4 -b 1')
model = svm_train(prob, param)
yt = [1]
xt = [{1:1, 2:1}]
p_label, p_acc, p_val = svm_predict(yt, xt, model)
print(p_label)

y, x = svm_read_problem('train1.txt')
yt, xt = svm_read_problem('test1.txt')
model = svm_train(y, x )
print('test:')
p_label, p_acc, p_val = svm_predict(yt[200:202], xt[200:202], model)
print(p_label)
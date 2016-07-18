# -*- coding: utf-8 -*-
import numpy as np
import chainer
from chainer import Function, Variable, optimizers
from chainer import Link, Chain
import chainer.functions as F
import chainer.links as L


#5次元のベクトルを入力して、そのベクトルがYes(1)かNo(0)かの2値分類
#3層パーセプトロン
model =  Chain(Hidden_Layer=L.Linear(5,30),Output_Layer=L.Linear(30,2))
#最適化アルゴリズム：SGD
optimizer = optimizers.Adam()
optimizer.setup(model)

p = np.array([0.2,0.5,0.1,0.2,0.1],dtype=np.float32)
Input = np.array([p],dtype=np.float32)
X = Variable(Input)
print X
print X.data
print X.data[0][1]

Answer = np.array([1],dtype=np.int32)
T = Variable(Answer)

for roop in range(1000):
    optimizer.zero_grads()
    u1 = model.Hidden_Layer(X)
    h = F.relu(u1)
    u2 = model.Output_Layer(h)
    y = F.softmax(u2)
    print y.data
    loss = F.softmax_cross_entropy(u2,T)
    loss.backward()
    optimizer.weight_decay(0.5)
    optimizer.update()

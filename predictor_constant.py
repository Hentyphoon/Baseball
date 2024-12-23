import pybaseball as pyball
import numpy as np
 # add MBGD and GDB depending on T and n to optimize runtime
def step_size(x):
  return x

def sigmoid(x,w):
  z = x@w
  return 1/(1+(e^(-z)))
  
def sum(x,w,y):
  sum = 0
  for i in range(len(x)):
    sig = sigmoid(x[i],w[i])
    sum += (sig - y[i]) * x[i]
  return sum
  
def mle_predictor(x,y,step_size,T):
  n, d = X[:,1:].shape
  w = np.random.randn(d+1)
  for t in T:
    w -= step_size*sum(x,w,y)

  return w
  

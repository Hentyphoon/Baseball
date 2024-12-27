import pybaseball as pyball
import numpy as np
from pybaseball import statcast_batter
from datetime import datetime
import pandas as pd

def collect_data():
 today = datetime.today().strftime('%Y-%m-%d')
 data = pyball.statcast(start_date=2025-01-01, end_date=today)
 length = len(data)//2
 train_data = data[:length]
 test_data = data[length:]
 return train_data, test_data
 
def step_size(x):
    return x

def sigmoid(x, w):
    z = x @ w 
    return 1 / (1 + np.exp(-z))


def compute_gradient(x, w, y):
    gradient = np.zeros(w.shape) 
    for i in range(len(x)):
        sig = sigmoid(x[i], w)
        gradient += (sig - y[i]) * x[i]  
    return gradient


def mle_predictor(x, y, step_size, T):
    n, d = x.shape  
    w = np.random.randn(d+1)  

    for t in range(T):  
        gradient = compute_gradient(x, w, y)
        w -= step_size * gradient 

    return w


def main():
    train_data, test_data = collect_data()
    x = 
    y = 
    w = mle_predictor(x,y,step_size, T)

if __name__ == "__main__":
    main()

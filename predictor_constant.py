import pybaseball as pyball
import numpy as np
from pybaseball import statcast_batter
from datetime import datetime
import pandas as pd

def collect_data():
 today = datetime.today().strftime('%Y-%m-%d')
 data = pyball.statcast(start_date=2025-01-01, end_date=today)
 length = len(data)
 X
 
 
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
    np.random.seed(42)  
    X = np.random.rand(100, 3) 
    Y = (X[:, 0] + X[:, 1] > 1).astype(int)  
    step = step_size(0.01)  
    epochs = 100 
    weights = mle_predictor(X, Y, step, epochs)

    print("Trained Weights:", weights)

if __name__ == "__main__":
    main()

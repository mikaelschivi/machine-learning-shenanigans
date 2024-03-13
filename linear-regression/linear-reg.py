#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from create_data import Set 
from create_data import DATASET_SIZE

def error_gradient(m_now, b_now, data, learningRate):
    m_grad = 0
    b_grad = 0

    n = DATASET_SIZE
    for i in range(n):
        x = data.iloc[i].hsize
        y = data.iloc[i].price

        # partial derivative of 1/n * sum( (y_i - y'_i') ** 2 ) in relation to m and b
        m_grad += -(2/n) * x * (y - (m_now * x + b_now))
        b_grad += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_grad * learningRate
    b = b_now - b_grad * learningRate

    return m, b

if __name__ == '__main__':
    # Set()
    dataset = pd.read_csv('data.csv')
    
    # y' = m * x + b
    m = 94.64031056101999 # starting M
    b = 0.14306927828237517 # starting B
    L = 0.000000001 # learning rate
    epochs = 10000 # iterations

    for i in range(epochs):
        if i % 100 == 0: 
            print(f"iteration: {i}")
            print(f"m: {m} b:{b}")
        m, b = error_gradient(m, b, dataset, L)
    print(f"\nm: {m} b:{b}")
    
    # while(True):
    #     try:
    #         ip = int(input("square meterage of home: "))
    #         print(f'- average price: ${(m * ip + b)*100:,.2f}')
    #     except:
    #         break

    plt.scatter(dataset.hsize, dataset.price, color="black")
    plt.plot( list(range(0, 2300)), [m * x + b for x in range(0, 2300)], color="red")
    plt.show()
    
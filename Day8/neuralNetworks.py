import numpy as np

input_array = np.array([[0,0,1],[1,1,1], [1,0,1], [0,1,1]])

output_array = np.array([0,1,1,0])

synaptic_weights = np.random.uniform(-1,1,3)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*1(1-sigmoid(x))


for i in range(5):
    output_init = np.dot(input_array,synaptic_weights)
    output = sigmoid(output_init)
    error = output_array - output
    total_gradient = np.dot(input_array.T, error*sigmoid_derivative(output_init))
    synaptic_weights += total_gradient



import numpy as np

def neural_net(input_data):
    # Initialize weights and biases
    num_features = input_data.shape[1]
    weights = np.random.randn(num_features) / np.sqrt(num_features)
    biases = np.zeros(1)

    # Forward propagation
    # ...

    out = np.dot(weights.T, input_data) + biases

    # Return the output
    # ...
    return out

def forward(input_data):
    # Forward propagation
    # ...

def backprop():
    # Backpropagation
    # ...

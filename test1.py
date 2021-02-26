import numpy as np

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

training_inputs = np.array([
    [1,0,1],
    [0,0,0],
    [1,1,1],
    [0,1,0],
])  

training_outputs = np.array([[0,0,1,0]]).T
synaptic_weights = 2 * np.random.random((3,1)) - 1

for _ in range(10000):
    outputs = sigmoid( np.dot(training_inputs, synaptic_weights) )
    err = training_outputs - outputs
    adjustments = np.dot( training_inputs.T, err * (outputs * (1 - outputs)) )
    synaptic_weights += adjustments

# Test
new_input = np.array([0,0,0])
output = sigmoid( np.dot( new_input, synaptic_weights) )

print( "New situation:" )
print("Yes" if np.round(output) else "No")

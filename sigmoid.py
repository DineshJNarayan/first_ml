import numpy as np
import class_neuralnetwork as cn

input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

# Computing the dot product of input_vector and weights_1
first_indexes_mult = input_vector[0] * weights_1[0]
second_indexes_mult = input_vector[1] * weights_1[1]
dot_product_1 = first_indexes_mult + second_indexes_mult
print(f"The dot product 1 is: {dot_product_1}")
dot_product_2 = np.dot(input_vector, weights_2)
print(f"The dot product 2 is: {dot_product_2}")

# Wrapping the vectors in NumPy arrays
input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2

prediction = make_prediction(input_vector, weights_1, bias)
print(f"The prediction result is: {prediction}")

# Changing the value of input_vector
input_vector = np.array([2, 1.5])
prediction = make_prediction(input_vector, weights_1, bias)
print(f"The prediction result is: {prediction}")

target = 0
mse = np.square(prediction - target)
print(f"Prediction: {prediction}; Error: {mse}")

derivative = 2 * (prediction - target)
print(f"The derivative is {derivative}")
# Updating the weights
weights_1 = weights_1 - derivative
prediction = make_prediction(input_vector, weights_1, bias)
error = (prediction - target) ** 2
print(f"Prediction: {prediction}; Error: {error}")

#learning_rate = 0.1
#neural_network = cn.NeuralNetwork(learning_rate)
#neural_network.predict(input_vector)
## please use 'conda activate test_env' before running script 'python3 simple_neural.py' -> 11-01-2022

import numpy as np
import class_neuralnetwork as cn
from matplotlib import pyplot

input_vectors = np.array    (
    [
        [3, 1.5],
        [2, 1],
        [4, 1.5],
        [3, 4],
        [3.5, 0.5],
        [2, 0.5],
        [5.5, 1],
        [1, 1],
    ]
)

targets = np.array([0, 1, 0, 1, 0, 1, 1, 0])
learning_rate = 0.1
neural_network = cn.NeuralNetwork(learning_rate)
training_error = neural_network.train(input_vectors, targets, 10000)

pyplot.plot(training_error)
pyplot.xlabel("Iterations")
pyplot.ylabel("Error for all training instances")
pyplot.show()
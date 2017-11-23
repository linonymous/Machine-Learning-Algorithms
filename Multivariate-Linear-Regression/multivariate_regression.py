from gradient_step import gradient_step
from cost_function import cost_function
from hypothesis import hypothesis
import numpy as np

def init_theta(num_features):
    list_of_zeroes = [0] * num_features
    return list_of_zeroes

def gradient_descent_runner(input_x, output_y, theta, num_iterations, learning_rate):
    for i in range(num_iterations):
        for index in range(len(output_y)):
            data = np.array([1, input_x[index]])
            theta = gradient_step(data, output_y[index], theta, learning_rate, len(output_y))
    return theta

data = np.loadtxt("train.csv",delimiter=",")
input_x = data[:,0]
input_y = data[:,1]
theta = init_theta(2)
theta = gradient_descent_runner(input_x, input_y, theta, num_iterations=2000, learning_rate=0.0001)
print theta

test = np.loadtxt("train.csv",delimiter=",")
input_x = data[:,0]
input_y = data[:,1]
print np.array([1, input_x[0]])
print hypothesis(np.array([1, input_x[0]]),theta)
from gradient_step import gradient_step
from cost_function import cost_function
from hypothesis import hypothesis
import numpy as np

def init_theta(num_features):
    list_of_zeroes = [0] * num_features
    return list_of_zeroes

def gradient_descent_runner(input_x, output_y, theta, num_iterations, learning_rate):
    for i in range(num_iterations):
        for index in len(output_y):
            theta = gradient_step(input_x[index], output_y[index], theta, learning_rate)
    return theta

from hypothesis import hypothesis
import numpy as np
def gradient_step(input_x, output_y, theta, learning_rate, data_size):
    t_theta = theta
    for i in range(len(theta)):
        theta[i] = t_theta[i] - learning_rate * 1/data_size  *(hypothesis(input_x, t_theta) - output_y) * input_x[i]
    return theta
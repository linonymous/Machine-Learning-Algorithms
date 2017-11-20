from gradient_step import gradient_step
from cost_function import cost_function
from hypothesis import hypothesis
import numpy as np

def init_theta(num_features):
    list_of_zeroes = [0] * num_features
    return list_of_zeroes
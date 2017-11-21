from hypothesis import hypothesis

def gradient_step(input_x, output_y, theta, learning_rate):
    t_theta = theta
    for i in len(theta):
        if i == 0:
            theta[i] = t_theta[i] - learning_rate * (hypothesis(input_x, t_theta) - output_y)
        else:
            theta[i] = t_theta[i] - learning_rate * (hypothesis(input_x, t_theta) - output_y) * input_x[i]
    return theta
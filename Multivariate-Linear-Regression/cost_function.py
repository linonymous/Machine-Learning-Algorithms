from hypothesis import hypothesis

def cost_function(input_x, output_y, theta):
    # input x is the array of one dimensional array
    err = 0
    index = 0
    for tupl in input_x:
        err += (hypothesis(tupl, theta) - output_y[index]) **2
        index += 1
    return (1.0/2.0) * len(output_y) * float(err)
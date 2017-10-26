from random import choice
from numpy import array, dot, random

def step(x):
    if x<0:
        return 0
    else:
        return 1

data = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1, 1]), 1),
]
w = random.rand(3)
print w
errors = [] #array of errors
eta = 0.2 #learning rate
n = 100 #number of iterations
#tup, x = choice(data)
#print tup
#a = dot(w, tup)
#print a

for i in xrange(n):
    x, expected = choice(data)
    result = dot(w, x)
    error = expected - step(result)
    errors.append(error)
    w += eta * error * x

for x, _ in data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, step(result)))
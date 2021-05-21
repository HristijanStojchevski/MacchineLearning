import numpy as np


# def get_large_data():
#     with open('dataA.csv') as data:
#         lines = data.readlines()
#     instances = [instance[:-1].split(',') for instance in lines]
#     return instances
#

def generate_data(n):
    rand_dots = np.random.rand(n, 2)
    dat = []
    print("entered")
    i = 0
    for dot_rand in rand_dots:
        x = dot_rand[0]
        y = dot_rand[1]
        sin = np.sin(6*x)
        y_func = (sin/6) + 0.6
        if y <= y_func:
            cl = 'd'
        else:
            cl = 'u'
        dat.append([x, y, cl])
    print("Finished")
    return dat

import numpy as np


# def get_dataset():
#     with open('dataB.csv') as data:
#         lines = data.readlines()
#     instances = [instance[:-1].split(',') for instance in lines]
#     return instances


def generate_chess_data(n):
    rand_dots = np.random.rand(n, 2)
    d = []
    for dots in rand_dots:
        _x = dots[0]
        _y = dots[1]
        if _x <= 0.25:
            if _y <= 0.25:
                # 0,0
                d.append([_x, _y, 1])
            elif _y <= 0.5:
                # 0,25
                d.append([_x, _y, 0])
            elif _y <= 0.75:
                # 0,5
                d.append([_x, _y, 1])
            else:
                # 0,75
                d.append([_x, _y, 0])
        elif _x <= 0.5:
            if _y <= 0.25:
                # 25,0
                d.append([_x, _y, 0])
            elif _y <= 0.5:
                # 25, 25
                d.append([_x, _y, 1])
            elif _y <= 0.75:
                # 25,50
                d.append([_x, _y, 0])
            else:
                # 25,75
                d.append([_x, _y, 1])
        elif _x <= 0.75:
            if _y <= 0.25:
                # 50,0
                d.append([_x, _y, 1])
            elif _y <= 0.5:
                # 50,25
                d.append([_x, _y, 0])
            elif _y <= 0.75:
                # 50,50
                d.append([_x, _y, 1])
            else:
                # 50,75
                d.append([_x, _y, 0])
        else:
            if _y <= 0.25:
                # 75,0
                d.append([_x, _y, 0])
            elif _y <= 0.5:
                # 75,25
                d.append([_x, _y, 1])
            elif _y <= 0.75:
                # 75,50
                d.append([_x, _y, 0])
            else:
                # 75,75
                d.append([_x, _y, 1])
    return d


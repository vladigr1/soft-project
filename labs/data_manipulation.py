import numpy as np

def avg_filter(filter_size):
    return lambda ldata : np.sum(ldata)//filter_size

def filter(data,func, filter_size):
    if len(data) % 3 != 0:
        raise Exception("data doesn't divide to filter_size")
    return [func(data[i*3: (i+1)*3]) for i in range(len(data) // filter_size ) ]
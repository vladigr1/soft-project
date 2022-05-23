import numpy as np

def avg_filter(filter_size):
    return lambda ldata : np.sum(ldata)/filter_size

def max_filter(filter_size):
    return lambda ldata : np.max(ldata)

def filter(data,func, filter_size):
    if len(data) < filter_size - 1:
        raise Exception("Not enough data")
    return [func(data[i- filter_size + 1 : i+1]) for i in range(filter_size-1, len(data) ) ]
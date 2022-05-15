import numpy as np
import pandas as pd
from functools import reduce
import operator

def distance_vec(data, sderived, lbasics, fit_model):
    derived_values = data[sderived].to_numpy()
    basic_values = data[lbasics]
    pred_row = np.array(fit_model.predict(basic_values).round(2))

    max_val = pred_row[:].max(1).reshape((-1,1)) # max likelhood sections
    (pred_i, pred_j) = np.where(pred_row == max_val) # get list indexes
    pred = list(map(lambda x: pred_j[x], set(pred_i)))
    
    return pd.DataFrame(

        {
            "derived": derived_values,

            "pred": pred,

            "dist": np.abs(derived_values-pred),
        }

    )

def accuracy(distance_vec):
    return reduce(operator.add, distance_vec['dist'],0)
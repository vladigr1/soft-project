import numpy as np
import pandas as pd
from functools import reduce
import operator
from algorithms import pred_vec

def distance_vec(data, sderived, lbasics, fit_model):
    derived_values = data[sderived].to_numpy()
    pred = pred_vec(fit_model, data, sderived, lbasics)
    
    return pd.DataFrame(

        {
            "derived": derived_values,

            "pred": pred,

            "dist": np.abs(derived_values-pred),
        }

    )

def accuracy(distance_vec):
    return reduce(operator.add, distance_vec['dist'],0)
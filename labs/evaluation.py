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


def evaluation_graph(data, sderived, lbasics, amount_of_days, regression_alg):
    amount_of_days = 15
    size_data = len(data.index)
    x = []
    y = []
    for i in range(size_data-amount_of_days+1):
        cur_data = data.iloc[i:i+amount_of_days,:]
        if len(x) == 7:
            break
        try:
            (fit_model, param_in_model, cur_pvalue) = regression_alg(cur_data, sderived, lbasics)
            if param_in_model == []:
                raise Exception('lbasics is empty')
        except:
            continue
        ac = accuracy(distance_vec(cur_data, sderived, param_in_model, fit_model))
        x.append(cur_pvalue)
        y.append(ac)
    return x,y


    
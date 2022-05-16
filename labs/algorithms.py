import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

from pandas.api.types import CategoricalDtype
from copy import copy

from statsmodels.miscmodels.ordinal_model import OrderedModel
np.seterr(divide='ignore', invalid='ignore')



def categories_derived(pd_derivied):
    # generate shalow copy to not destory values
    pd_derivied = copy(pd_derivied)
    derived = list(set(pd_derivied.to_numpy()))
    if  len(derived) < 5 :
        raise Exception("can't category derived, not enough unique values.")
    derived.sort()
    step = len(derived)//5 # 5 categories

    boundaries = np.array([derived[i] for i in range(step,4*step+1,step)])
    #print(f'boundaries: {boundaries}')
    for i,val in enumerate(pd_derivied):
        if boundaries[3] <= val:
            pd_derivied[i] = 5
            continue
        category = np.argmax(val < boundaries ) + 1
        #print(f'{val} {category}')
        pd_derivied[i] = category
    
    cat_type = CategoricalDtype(categories=[1, 2, 3, 4, 5], ordered=True)
    return pd_derivied.astype(cat_type)


def load_data(csv_path):
    data_diam = pd.read_csv(csv_path, dtype =  np.double)
    cat_derivied = categories_derived(data_diam['amount of sleep'])
    data_diam['amount of sleep'] = cat_derivied
    return data_diam


def pred_vec(mod_fit, data, sderived, lbasics):
    basic_values = data[lbasics]
    pred_row = np.array(mod_fit.predict(basic_values).round(2))
    max_val = pred_row[:].max(1).reshape((-1,1)) # max likelhood sections
    (pred_i, pred_j) = np.where(pred_row == max_val) # get list indexes
    pred = list(map(lambda x: pred_j[x], set(pred_i)))
    return pred


def ttest(mod_fit, data, sderived, lbasics):
    derived_values = data[sderived].to_numpy()
    pred = pred_vec(mod_fit, data, sderived, lbasics)
    # Calculate the T-test for the means of two independent samples of scores.
    (tvalue, pvalue) = ttest_ind(derived_values, pred)

    return pvalue


def generateOLR(data, sderived, lbasics):
    # generate logistic regression
    mod_prob = OrderedModel(data[sderived],
                            data[lbasics],
                            distr='logit')
    
    return mod_prob.fit(method='bfgs' ,disp = False) # Don't print report


def stepwise_regression(data, sderived, lbasics, in_threshold, out_threshold):
    param_in_model = []
    param_not_in_model = copy(lbasics)

    while True:
        bchange = False
        # add

        for param in param_not_in_model:
            temp_basics = param_in_model + [param]
            fit_model = generateOLR(data, sderived, temp_basics)
            pvalue = ttest(fit_model, data, sderived, temp_basics)
            if pvalue < in_threshold:
                cur_model = fit_model
                param_in_model.append(param)
                param_not_in_model.remove(param)
                print(f'add-params: {param_in_model}, pvalue: {pvalue}')
                bchange = True
                break

        if bchange == True:
            continue

        # remove
        for param in param_in_model:
            temp_basics = copy(param_in_model)
            temp_basics.remove(param)
            fit_model = generateOLR(data, sderived, temp_basics)
            pvalue = ttest(fit_model, data, sderived, temp_basics)
            if pvalue > out_threshold:
                cur_model = fit_model
                param_in_model.remove(param)
                param_not_in_model.append(param)
                print(f'remove-params: {param_in_model}, pvalue: {pvalue}')
                bchange = True
                break

        if bchange == False:
            break
    if not param_in_model:
        raise Exception("Stepwise_reggresion couldn't pick a parameter.")
    return (cur_model, param_in_model)
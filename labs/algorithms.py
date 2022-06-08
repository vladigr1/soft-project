import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

from pandas.api.types import CategoricalDtype
from copy import copy

from statsmodels.miscmodels.ordinal_model import OrderedModel
np.seterr(divide='ignore', invalid='ignore')

from data_manipulation import filter

def generate_boundary(pd_derivied, num_categories = 5):
    derived = list(set(pd_derivied.to_numpy()))
    if  len(derived) < num_categories :
        raise Exception("can't category derived, not enough unique values.")
    derived.sort()
    step = len(derived)//num_categories

    boundaries = np.array([derived[i] for i in range(step,(num_categories-1)*step+1,step)])
    return boundaries

def categories_derived_with_boundaries(pd_derivied, boundaries, num_categories = 5):
    # generate shalow copy to not destory values
    pd_derivied = copy(pd_derivied)
    #print(f'boundaries: {boundaries}')
    for i,val in enumerate(pd_derivied):
        if boundaries[num_categories-2] <= val: # in num_cat = 5 bound = (2,3,4,5)
            pd_derivied[i] = num_categories - 1
            continue
        category = np.argmax(val < boundaries )
        #print(f'{val} {category}')
        pd_derivied[i] = category
    
    cat_type = CategoricalDtype(categories=[i for i in range(0,num_categories)], ordered=True)
    return pd_derivied.astype(cat_type)


def categories_derived(pd_derivied, num_categories = 5):
    boundaries = generate_boundary(pd_derivied, num_categories)
    return categories_derived_with_boundaries(pd_derivied, boundaries, num_categories)

def load_form(csv_path):
    #clean csv of form
    data_diam = pd.read_csv(csv_path, dtype =  np.double)
    data_diam = data_diam.drop([0])
    data_diam = data_diam.drop(data_diam.columns[[0]], axis=1)
    data_diam = pd.DataFrame(data_diam.values, columns=data_diam.columns)

    cat_derivied = categories_derived(data_diam.iloc[:,0])
    data_diam.iloc[:,0] = cat_derivied
    return data_diam

def load_data(csv_path, sderived , num_categories = 5):
    data_diam = pd.read_csv(csv_path, dtype =  np.double)
    cat_derivied = categories_derived(data_diam[sderived], num_categories)
    data_diam[sderived] = cat_derivied
    return data_diam

def load_data_with_fiters(csv_path, sderived, lfilters, filter_size):
    data_diam = pd.read_csv(csv_path, dtype =  np.double)
    return filter_data(data_diam, sderived, lfilters, filter_size)

def filter_data(data_diam, sderived, lfilters, filter_size):
    lparams = list(data_diam.columns.values)
    size_sample = data_diam.shape[0]

    data = np.empty((size_sample-filter_size+1, len(lparams)), dtype=np.double)
    for i, param in enumerate(lparams):
        if lfilters[i] == None:
                data[:,i] = data_diam.iloc[filter_size-1:,i]
                continue
        data[:,i] = filter(data_diam[param].values, lfilters[i],filter_size)
    
    df = pd.DataFrame(data, columns=lparams)
    cat_derivied = categories_derived(df[sderived])
    df[sderived] = cat_derivied
    return df


def pred_vec(mod_fit, data, sderived, lbasics):
    # pred base of mean
    basic_values = data[lbasics]
    pred_row = np.array(mod_fit.predict(basic_values))
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


def stepwise_regression(data, sderived, lbasics, in_threshold = 0.5, out_threshold = 0.05):
    param_in_model = []
    param_not_in_model = copy(lbasics)

    min = 1
    for param in param_not_in_model:
            temp_basics = param_in_model + [param]
            fit_model = generateOLR(data, sderived, temp_basics)
            pvalue = ttest(fit_model, data, sderived, temp_basics)
            if pvalue < min:
                cur_model = fit_model
                cur_pvalue = pvalue
                parm_min = param

    param_in_model.append(parm_min)
    param_not_in_model.remove(parm_min)

    counter = 2*(len(lbasics) + 1)
    while True:
        bchange = False
        # add

        for param in param_not_in_model:
            temp_basics = param_in_model + [param]
            fit_model = generateOLR(data, sderived, temp_basics)
            pvalue = ttest(fit_model, data, sderived, temp_basics)
            if pvalue < in_threshold:
                cur_model = fit_model
                cur_pvalue = pvalue
                param_in_model.append(param)
                param_not_in_model.remove(param)
                #print(f'add-params: {param}, pvalue: {pvalue}')
                bchange = True
                counter = counter - 1
                break
        
        if (counter == 0):
             break
        if bchange == True:
            continue

        # remove
        if len(param_in_model) == 1:
            break
        for param in param_in_model:
            temp_basics = copy(param_in_model)
            temp_basics.remove(param)
            fit_model = generateOLR(data, sderived, temp_basics)
            pvalue = ttest(fit_model, data, sderived, temp_basics)
            if pvalue < out_threshold:
                cur_model = fit_model
                cur_pvalue = pvalue
                param_in_model.remove(param)
                param_not_in_model.append(param)
                #print(f'remove-params: {param}, pvalue: {pvalue}')
                bchange = True
                counter = counter - 1
                break
        
        if (counter == 0):
             break
        if bchange == False:
            break
    if not param_in_model:
        raise Exception("Stepwise_reggresion couldn't pick a parameter.")
    return (cur_model, param_in_model, cur_pvalue)

def best_subset(data, sderived, lbasics, cur_params=[], index=0):
    if index == len(lbasics):
        if cur_params == []:
            return (None, [], 1)
        fit_model = generateOLR(data, sderived, cur_params)
        pvalue = ttest(fit_model, data, sderived, cur_params)
        return (fit_model, cur_params, pvalue)
    
    (fit_model_with_i, cur_params_with_i, pvalue_with_i) = best_subset(data, sderived, lbasics,cur_params+[lbasics[index]], index+1)
    (fit_model_without_i, cur_params_without_i, pvalue_without_i) = best_subset(data, sderived, lbasics,cur_params, index+1)
    if pvalue_with_i < pvalue_without_i:
        return (fit_model_with_i, cur_params_with_i, pvalue_with_i) 
    else:
        return (fit_model_without_i, cur_params_without_i, pvalue_without_i)

def filter_lbasic_with_spearman(data, sderived, lbasics, pracentage_to_keep=0.7):
    from scipy.stats import spearmanr
    num_lparam = round(pracentage_to_keep * len(lbasics))

    # data[parm])[1] - pvalue
    cor_basic = [(parm, spearmanr(data[sderived], data[parm])[1]) for parm in lbasics]

    cor_basic.sort(key = lambda x: x[1])
    # param[0] - param str
    return [param[0] for param in cor_basic[:num_lparam]]

def best_subset_with_spearman(data, sderived, lbasics, pracentage_to_keep=0.7):
    lparam_after_spearman = filter_lbasic_with_spearman(data, sderived, lbasics, pracentage_to_keep)
    return best_subset(data, sderived, lparam_after_spearman)

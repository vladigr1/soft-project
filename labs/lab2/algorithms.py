import numpy as np
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
    print(f'boundaries: {boundaries}')
    for i,val in enumerate(pd_derivied):
        if boundaries[3] <= val:
            pd_derivied[i] = 5
            continue
        category = np.argmax(val < boundaries ) + 1
        #print(f'{val} {category}')
        pd_derivied[i] = category
    
    cat_type = CategoricalDtype(categories=[1, 2, 3, 4, 5], ordered=True)
    return pd_derivied.astype(cat_type)

def ttest(mod_fit, data, sderived, lbasics):
    derived_values = data[sderived].to_numpy()
    basic_values = data[lbasics]
    pred_row = mod_fit.predict(basic_values).round(2)
    pred = np.where(pred_row == 1)[1] # get list indexes    

    # Calculate the T-test for the means of two independent samples of scores.
    (tvalue, pvalue) = ttest_ind(derived_values, pred)

    return pvalue

def generateOLR(data, sderived, lbasics):
    # generate logistic regression
    mod_prob = OrderedModel(data[sderived],
                            data[lbasics],
                            distr='logit')
    
    return mod_prob.fit(method='bfgs' ,disp = False) # Don't print report
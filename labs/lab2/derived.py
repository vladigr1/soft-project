import numpy as np
from pandas.api.types import CategoricalDtype
from copy import copy

def categories_derived(pd_derivied):
    # generate shalow copy to not destory values
    pd_derivied = copy(pd_derivied)
    derived = list(set(pd_derivied.to_numpy()))
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

     
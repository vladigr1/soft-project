import pandas as pd
import numpy as np
import sys
sys.path.insert(0, "./labs")
from labs.algorithms import categories_derived, stepwise_regression



class Report:
    def __init__(self,*args) -> None:
        if len(args) == 1:
            data_categroies = self._load_form(args[0])

            sderived = str(data_categroies.columns[0])
            lbasics = list(data_categroies.columns)
            lbasics.remove(sderived)

            # TODO: algorithem base on config
            (fit_model, param_in_model, cur_pvalue) = stepwise_regression(data_categroies, sderived, lbasics)
            self._listHeaders = list(fit_model.params.index)
            self._listValues =  list(fit_model.params.values)
            self._num_basic_param = len(param_in_model)
            
        elif len(args) == 2:
            self._listHeaders = args[0]
            self._listValues = args[1]
            self._num_basic_param = -1
        else:
            raise Exception("Wrong amoung of paramater fo construction")

    def _load_form(self,csv_path):
        #clean csv of form
        data_diam = pd.read_csv(csv_path)
        values = data_diam.values
        values = values[1:,1:]
        values = np.array(values, dtype=np.double)
        data_diam = pd.DataFrame(values, columns=data_diam.columns[1:])

        cat_derivied = categories_derived(data_diam.iloc[:,0])
        data_diam.iloc[:,0] = cat_derivied
        return data_diam
    
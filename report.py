import enum
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, "./labs")
from labs.algorithms import categories_derived, stepwise_regression, filter_data
from labs.evaluation import distance_vec, accuracy
from os import listdir
from os.path import isfile, join
import pickle
from functools import reduce
from config import filter_size,Configuration, lfilter_lambdas, lfilter_name, regression_alg
from param import lparms

report_folder = './Data/Report/'

class Report:
    def __init__(self, form_path) -> None:
        config = Configuration.load()
        mfilters = {
            lparms[i].title(): lfilter_lambdas[config.lindex_filters_for_parm[i]] 
         for i in range(len(lparms)) 
        }
        self.data_categroies = self._load_form_with_lfilters(form_path, mfilters)

        sderived = str(self.data_categroies.columns[0])
        lbasics = list(self.data_categroies.columns)
        lbasics.remove(sderived)

        reg = regression_alg[config.index_alg]
        (self.fit_model, self.param_in_model, self.cur_pvalue) = reg(self.data_categroies, sderived, lbasics)
        self.num_basic_param = len(self.param_in_model)
        self.generate_summary()
        


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

    def _load_form_with_lfilters(self,csv_path,mfilters):
        withoutFilters = reduce(lambda a,b: a & (b is None), mfilters, True )
        if withoutFilters == True:
            return self._load_form(csv_path)
        #clean csv of form
        data_diam = pd.read_csv(csv_path)
        values = data_diam.values
        values = values[1:,1:]
        values = np.array(values, dtype=np.double)
        data_diam = pd.DataFrame(values, columns=data_diam.columns[1:])
        lfilters = [mfilters[param] for param in  data_diam.columns] 
        return filter_data(data_diam, data_diam.columns[0],lfilters , filter_size)

    def generate_summary(self):
        self.listHeaders = list(self.fit_model.params.index)
        self.listValues =  list(np.exp(self.fit_model.params.values))

    def save_to_file(self, report_name):
        with open(report_folder + report_name, 'wb') as file:
            pickle.dump(self, file)

    def load(report_name):
        with open(report_folder + report_name, 'rb') as file:
            return pickle.load(file)
    
    def lReports_names():
        return [f.split('.')[0] for f in listdir(report_folder) if isfile(join(report_folder, f))]


class FullReport(Report):
    def __init__(self, report) -> None:
        self.listHeaders = report.listHeaders
        self.listValues = report.listValues
        self.cur_pvalue = report.cur_pvalue
        self.data_categroies = report.data_categroies
        self.fit_model = report.fit_model
        self.param_in_model = report.param_in_model

    def generate_summary(self):
        self.listHeaders = list(self.fit_model.params.index)
        self.listValues =  list(self.fit_model.params.values)
        self.listHeaders.append('p-value')
        self.listValues.append(self.cur_pvalue)
        self.listHeaders.append('accuracy')
        self.listValues.append(accuracy(
            distance_vec(self.data_categroies, self.data_categroies.columns[0],
             self.param_in_model,self.fit_model)))


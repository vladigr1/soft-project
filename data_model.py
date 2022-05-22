import json
from types import SimpleNamespace
from param import Parameter
from os import listdir
from os.path import isfile, join, basename
import numpy as np
import pandas as pd
import pickle

class DataModel:
    def __init__(self,name : str, derivied_parameter : Parameter, basic_parameeters : list, num_days : int) -> None:
        self._derivied_parameter = derivied_parameter
        self._basic_parameeters = basic_parameeters
        self._num_days = num_days
        self._id  = name

    # setter and getter
    def derivied_parameter(self, t = None):
        if t != None:
            self._derivied_parameter = t
        return self._derivied_parameter  
    def basic_parameeters(self, t = None):
        if t != None:
            self._basic_parameeters = t
        return self._basic_parameeters
        
    def set_id(self):
        self._id  = self._derivied_parameter.title()[0:2]
        for bp in self._basic_parameeters:
            self._id  += bp.title()[0:2]
        self._id  += str(self._num_days)
    
    def save_to_file(self, path = "./Data/DataModel/"):
        with open(path + str(self._id), 'wb') as file:
            pickle.dump(self, file)

    def create_form(self, num_of_days, path='.'):
        num_params = len(self._basic_parameeters) + 1
        data = np.array(num_params*num_of_days*[np.nan])
        data = data.reshape((num_of_days,num_params))
        df = pd.DataFrame(data=data, columns= [param.title() for param in self._basic_parameeters] + [self._derivied_parameter.title()])
        df.to_csv(path + self._id())
        

    def to_DataFrame(self):
        return pd.DataFrame(columns=[self._derivied_parameter.title()]+[param.title() for param in self._basic_parameeters])


    def model_name_to_data_model(model_name : str):
        return DataModel.load("./Data/DataModel/" + model_name)

    def load(path : str):
        with open(path, 'rb') as file:
            return pickle.load(file)

    def lDataModels_names(path = "./Data/DataModel/"):
        return [f.split('.')[0] for f in listdir(path) if isfile(join(path, f))]


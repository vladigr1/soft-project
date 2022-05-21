import json
from types import SimpleNamespace
from param import Parameter
from os import listdir
from os.path import isfile, join, basename
import numpy as np
import pandas as pd

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
    
    def save_to_json(self, path = "./Data/DataModel/"):
        data_model_as_json =  json.dumps(self, default=lambda o: o.__dict__,
        sort_keys=True, indent=4)
        with open(path + str(self._id) + '.json', 'w' ) as file:
            file.write(data_model_as_json)

    def create_form(self, num_of_days, path='.'):
        num_params = len(self._basic_parameeters) + 1
        data = np.array(num_params*num_of_days*[np.nan])
        data = data.reshape((num_of_days,num_params))
        df = pd.DataFrame(data=data, columns= [param.title() for param in self._basic_parameeters] + [self._derivied_parameter.title()])
        df.to_csv(path + self._id())

    def to_DataFrame(self):
        return pd.DataFrame(columns=[self._derivied_parameter.title()]+[param.title() for param in self._basic_parameeters])


    def model_name_to_data_model(model_name : str):
        return DataModel.json_file_to_data_model("./Data/DataModel/" + model_name + '.json')

    def json_file_to_data_model(path : str):
        # Parse JSON into an object with attributes corresponding to dict keys.
        with open(path, 'r') as file:
            sn_res = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
            derivied_parameter = Parameter(sn_res._derivied_parameter._title, sn_res._derivied_parameter._unit)
            basic_parameeters = []
            for bp in sn_res._basic_parameeters:
                basic_parameeters.append(Parameter(bp._title, bp._unit))

            res = DataModel(basename(path), derivied_parameter, basic_parameeters, sn_res._num_days)
            return res

    def lDataModels_names(path = "./Data/DataModel/"):
        return [f.split('.')[0] for f in listdir(path) if isfile(join(path, f))]


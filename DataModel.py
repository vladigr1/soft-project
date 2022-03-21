#%%
import json
from types import SimpleNamespace
from Parameter import *
import random
class DataModel:
    def __init__(self, derivied_parameter : Parameter, basic_parameeters : list, num_days : int) -> None:
        self._derivied_parameter = derivied_parameter
        self._basic_parameeters = basic_parameeters
        self._num_days = num_days
        self.set_id()
        
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

    def json_file_to_data_model(path : str):
        # Parse JSON into an object with attributes corresponding to dict keys.
        with open(path, 'r') as file:
            sn_res = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
            derivied_parameter = Parameter(sn_res._derivied_parameter._title, sn_res._derivied_parameter._unit)
            basic_parameeters = []
            for bp in sn_res._basic_parameeters:
                basic_parameeters.append(Parameter(bp._title, bp._unit))

            res = DataModel(derivied_parameter, basic_parameeters, sn_res._num_days)
            return res


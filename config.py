from param import lparms
import pickle

import sys
sys.path.insert(0, "./labs")
import labs.data_manipulation as dm

lfilter_name = ['', 'avg', 'max']
filter_size = 2
lfilter_lambdas = [None, dm.avg_filter(filter_size), dm.max_filter(filter_size)]



lalg_name = ['stepwise OLR']

config_path = './Data/Config/config'

class Configuration:
    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.index_alg = 0
            self.lindex_filters_for_parm = len(lparms)*[0]
        elif len(args)== 2:
            self.index_alg = args[0]
            self.lindex_filters_for_parm = args[1]
        else:
            raise Exception('Wrong number of params!')
            

    def save_to_file(self):
        with open(config_path, 'wb') as file:
            pickle.dump(self, file)

    def load():
        try:
            with open(config_path, 'rb') as file:
                return pickle.load(file)
        except OSError:  # parent of IOError, OSError *and* WindowsError where available
            return Configuration()

import pytest
from data_model import DataModel
from param import parms
import os

def setup_module(module):
    print("setup")
    global dm
    dm = DataModel('Test', parms[0], [parms[1], parms[2]],14)
    global dm_path
    dm_path = "./Data/DataModel/" + str(dm._id) + '.json'

def test_assert():
   assert(True)

def test_DataModel_id_kept_the_same():
    dm1 = DataModel('Test', parms[0], [parms[1], parms[2]],14)
    assert(dm1._id == dm._id)
    dm2 = DataModel('Test2', parms[0], [parms[1], parms[2]],15)
    assert(dm2._id != dm._id)

def test_DataModel_save_to_json():
    if os.path.isfile(dm_path):
        os.remove(dm_path)
    dm.save_to_json()
    assert(os.path.isfile(dm_path))

    dm1 = DataModel.json_file_to_data_model(dm_path)
    assert(dm1, 'DataModel')
    assert(dm1, dm)




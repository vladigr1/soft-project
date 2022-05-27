import pytest
from sqlalchemy import false
from data_model import DataModel
from param import lparms
import os

def setup_module(module):
    print("setup")
    global dm
    dm = DataModel('Test', lparms[0], [lparms[1], lparms[2]],14)
    global dm_path
    dm_path = "./Data/DataModel/" + str(dm._id)

def test_assert():
   assert(True)

def test_DataModel_id_kept_the_same():
    #tests that the id will be as it needed
    dm1 = DataModel('Test', lparms[0], [lparms[1], lparms[2]],14)
    assert(dm1._id == dm._id)
    dm2 = DataModel('Test2', lparms[0], [lparms[1], lparms[2]],15)
    assert(dm2._id != dm._id)

def test_DataModel_save_to_json():
    # tests that the file saves the files actaully will be with pickle
    if os.path.isfile(dm_path):
        os.remove(dm_path)
    dm.save_to_file()
    assert(os.path.isfile(dm_path))

def test_DataModel_load():
    #tests that saves the DataModel
    if os.path.isfile(dm_path) == false:
        dm.save_to_file()
    loaded = DataModel.load(dm_path)
    assert(dm._id == loaded._id)




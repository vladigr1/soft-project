import pytest
import pandas as pd
import numpy as np

def test_assert():
    # test that assert works
    res = np.array([True, True])
    assert(np.all(res))

def test_categories():
    # test that the derived regulate the results to start from zero
    from algorithms import categories_derived
    data = pd.Series([1,2,3,4,5], dtype=np.int64)
    result = categories_derived(data)
    expected = pd.Series([0,1,2,3,4])
    assert all(result.values == expected.values)

    # tests that the bounds work when we have 5 categories
    data = pd.Series([1,2,3,4,5,6,7], dtype=np.int64)
    result = categories_derived(data) # boundaries: [2 3 4 5]
    expected = pd.Series([0,1,2,3,4,4,4])
    original = pd.Series([1,2,3,4,5,6,7], dtype=np.int64)
    assert all(data.values == original.values) # test that data didn't change
    assert all(result.values == expected.values) # test correctness
    
    # assert that it creates the bounders as needed when we do not need to increase step
    data = pd.Series([1,2,3,4,5,6,7,8], dtype=np.int64)
    result = categories_derived(data) # boundaries: [2 3 4 5]
    expected = pd.Series([0,1,2,3,4,4,4,4])
    original = pd.Series([1,2,3,4,5,6,7,8], dtype=np.int64)
    assert all(data.values == original.values) # test that data didn't change
    assert all(result.values == expected.values) # test correctness

    # assert that it creates the bounders as needed when we do need to increase step
    data = pd.Series([1,2,3,4,5,6,7,8,9,10], dtype=np.int64)
    result = categories_derived(data) # boundaries: [3 5 7 9]
    expected = pd.Series([0,0,1,1,2,2,3,3,4,4])
    original = pd.Series([1,2,3,4,5,6,7,8,9,10], dtype=np.int64)
    assert all(data.values == original.values) # test that data didn't change
    assert all(result.values == expected.values) # test correctness
    
    # check that the data will be normlized and with unsorted
    data = pd.Series([9,6,10,8,7,8], dtype=np.int64)
    result = categories_derived(data) # boundaries: [7 8 9 10]
    expected = pd.Series([3,0,4,2,1,2])
    original = pd.Series([9,6,10,8,7,8], dtype=np.int64)
    comp = result.values == expected.values
    assert all(data.values == original.values) # test that data didn't change
    assert all(result.values == expected.values) # test correctness

    data = pd.Series([1,2,2,4,5], dtype=np.int64)
    raise_exception = False
    try:
        result = categories_derived(data) # boundaries: [7 8 9 10]
    except:
        raise_exception = True
    assert raise_exception
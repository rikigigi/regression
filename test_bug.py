import numpy as np
def test_array_with_nan(num_regression):
    data1 = np.load('test_b.npy')
    num_regression.check({"gk": data1.flatten()})

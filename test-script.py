import numpy as np
import scipy.sparse

a = np.zeros((2, 2))
b = scipy.sparse.csc_matrix([[10.0, 45.0], [45.0, 285.0]])
print repr(a)
print repr(b)
# okay?
a + b
# error?
a + b

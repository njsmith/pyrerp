import warnings
warnings.filterwarnings("error", module="^testmod")
del warnings

import numpy as np
from scipy import sparse
a = np.zeros((2, 2))
b = sparse.csc_matrix([[10.0, 45.0], [45.0, 285.0]])
print repr(a)
print repr(b)
a + b
a += b

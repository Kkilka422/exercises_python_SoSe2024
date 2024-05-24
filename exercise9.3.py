import numpy as np

M = np.eye(5, dtype="int")
#np.identity()

M[3:, :2] = 2
M[:2, 3:] = 3
print(M)

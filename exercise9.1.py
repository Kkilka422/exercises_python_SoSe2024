import numpy as np


a = np.arange(1, 13)

a_3D = a.reshape(3, 2, 2)
#print(a_3D.ndim)
#print(a.ndim)
#print(a.shape)
#print(a_3D.shape)
#print(a_3D.size)
#print(a.size)
print(a_3D.dtype)
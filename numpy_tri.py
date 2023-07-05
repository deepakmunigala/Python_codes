import numpy as np

print(np.tri(4))
# [[1. 0. 0. 0.]
#  [1. 1. 0. 0.]
#  [1. 1. 1. 0.]
#  [1. 1. 1. 1.]]

print(type(np.tri(4)))
# <class 'numpy.ndarray'>

print(np.tri(4).dtype)
# float64

print(np.tri(4, dtype=int))
# [[1 0 0 0]
#  [1 1 0 0]
#  [1 1 1 0]
#  [1 1 1 1]]

print(np.tri(4, dtype=int).dtype)
# int64

print(np.tri(4, k=1))
# [[1. 1. 0. 0.]
#  [1. 1. 1. 0.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

print(np.tri(4, k=-1))
# [[0. 0. 0. 0.]
#  [1. 0. 0. 0.]
#  [1. 1. 0. 0.]
#  [1. 1. 1. 0.]]

print(np.tri(3, 4))
# [[1. 0. 0. 0.]
#  [1. 1. 0. 0.]
#  [1. 1. 1. 0.]]

print(np.tri(3, 4, k=-1))
# [[0. 0. 0. 0.]
#  [1. 0. 0. 0.]
#  [1. 1. 0. 0.]]

print(np.tri(4).T)
# [[1. 1. 1. 1.]
#  [0. 1. 1. 1.]
#  [0. 0. 1. 1.]
#  [0. 0. 0. 1.]]

print(np.tri(3, 4).T)
# [[1. 1. 1.]
#  [0. 1. 1.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

print(np.tri(4, k=1).T)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [0. 1. 1. 1.]
#  [0. 0. 1. 1.]]

print(np.tri(4, k=-1).T)
# [[0. 1. 1. 1.]
#  [0. 0. 1. 1.]
#  [0. 0. 0. 1.]
#  [0. 0. 0. 0.]]
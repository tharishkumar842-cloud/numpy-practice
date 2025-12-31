import numpy as np

mat = np.array([
    [3, 6, 9],
    [2, 4, 8],
    [5, 10, 15]
])
print(mat.sum(axis=1))
print(mat.sum(axis=0))
print(mat.max(axis=1))
print(mat.min(axis=0))

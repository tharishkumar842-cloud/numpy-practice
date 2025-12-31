import numpy as np

mat = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(mat)
print(mat.shape)
print(mat[0][1])
rows=mat.shape[0]
cols=mat.shape[1]
print("rows:",rows)
print("cols:",cols)
print(mat[0])
print(mat[:,-1])








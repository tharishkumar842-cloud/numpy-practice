import numpy as np

mat = np.array([
    [12, 5, 7],
    [3, 15, 2],
    [8, 4, 10]
])
mat[mat>10]=100
mat[mat<5]=0
print(mat)

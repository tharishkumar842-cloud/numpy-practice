import numpy as np

mat = np.array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

print("First row:", mat[0])
print("Last row:", mat[-1])
print("Second column:", mat[:, 1])
print("Last column:", mat[:, -1])

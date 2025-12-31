import numpy as np

mat = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("First row:", mat[0])
print("First column:", mat[:,0])
print("Second row:", mat[1])
print("Last column:", mat[:,-1])
print("Row sums:", mat.sum(axis=1))
print("Column sums:", mat.sum(axis=0))
print("Max of each row:", mat.max(axis=1))
print("Min of each column:", mat.min(axis=0))

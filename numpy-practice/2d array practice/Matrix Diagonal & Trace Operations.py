import numpy as np
mat = np.array([
    [5, 2, 3],
    [1, 6, 4],
    [7, 8, 9]
])
print("Main Diagonal:", np.diag(mat))
print("Trace of Matrix:", np.trace(mat))
print("secondary diagonal sum:",mat[::-1].diagonal().sum())

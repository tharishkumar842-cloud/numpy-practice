import numpy as np

mat = np.array([
    [2, 9, 4],
    [7, 1, 5],
    [6, 3, 8]
])

print(np.array(mat[mat > 5]))      # values greater than 5
print(np.array(mat[mat % 2 == 0])) # even values

mat[mat < 5] = 0   # replace values less than 5 with 0
mat[mat > 7] = 99  # replace values greater than 7 with 99

print(mat)

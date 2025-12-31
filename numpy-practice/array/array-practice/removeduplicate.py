import numpy as np
arr = np.array([10, 5, 8, 3, 12, 7])
print(len(np.array(arr[arr>6])))
print(np.where(arr==12))
print(np.array(arr[arr%2==0]))
arr1=np.array(arr*2)
print(arr1)
print(np.unique(arr))
import numpy as np
arr = np.array([10, 5, 8, 3, 12, 7])

print(len(arr))
print(arr[0])
print(arr[-1])
arr=np.append(arr,15)
arr=np.insert(arr,2,4)
arr=np.array(arr[arr!=8])
print(arr)


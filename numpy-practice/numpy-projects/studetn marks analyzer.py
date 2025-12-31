import numpy as np

marks = np.array([45, 67, 89, 23, 78, 90])
print(marks)
print("highest mark is:",marks.max())
print("lowest mark is:",marks.min())
print("average mark is:",np.mean(marks))
print("marks in ascending order:",np.sort(marks))
print("marks in descending order:",np.sort(marks)[::-1])

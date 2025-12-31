import numpy as np
temps = np.array([32.5, 34.0, 30.2, 29.8, 35.6, 33.1, 31.4])
print(temps)
print("highest temperature",temps.max())
print("lowest temperature:",temps.min())
print("average temperature:",np.mean(temps))
formula=temps*9/5+32
print(formula)
print("ascending order:",np.sort(temps))
print("descending order:",np.sort(temps)[::-1])

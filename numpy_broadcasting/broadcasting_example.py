import numpy as np

arr_2d = np.array([
[10,20,30],
[40,50,60],
[70,80,90],
])

arr_1d = np.array([10,20,30])

print(arr_1d.shape) # (3,)
print(arr_2d.shape) # (3, 3)

print(arr_2d + arr_1d)
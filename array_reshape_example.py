import numpy as np

arr_2 = np.array([
[10,20,30],
[40,50,60],
[70,80,90],
[75,85,95],
])

print(arr_2.shape) # (4, 3)

#print(arr_2.reshape(2,6))

print(arr_2.reshape(3,4))

# flattening the array
print(arr_2.reshape(12))
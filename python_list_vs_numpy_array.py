a = [1,2,3,4]
b = [5,6,7,8]

c = a+b
print(c) # [1, 2, 3, 4, 5, 6, 7, 8]

result = []

for i in range(len(a)):
    result.append(a[i]+b[i])

print("List:")
print(result)



import numpy as np
arr_a = np.array([1,2,3,4])
arr_b = np.array([5,6,7,8])
arr_c = arr_a + arr_b # add
print("array addition:")
print(arr_c)
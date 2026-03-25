import numpy as np

arr = np.array([1,2,3,4]) # 1D array 

#print(arr.shape) # (4,)

# 2D
arr_2 = np.array([
[10,20,30],
[40,50,60],
[70,80,90],
[75,85,95],
])
# print(arr_2.shape) # (4, 3)


# print(arr.ndim)
# print(arr_2.ndim)

# print(arr.size)
# print(arr_2.size)

# print(arr.dtype)
# print(arr_2.dtype)


# indexing and slicing

arr_2 = np.array([
[10,20,30],
[40,50,60],
[70,80,90],
[75,85,95],
])

#print(arr_2[0,1])

#print(arr_2[0:3,2])
#print(arr_2[0:3,-1]) # -1 is to access last item 

#print(arr_2[1:4,:])

arr_2 = np.array([
[10,20,30],
[40,50,60],
[70,80,90],
[75,85,95],
])

print(np.sum(arr_2,axis=0)) # column wise
print(np.sum(arr_2,axis=1)) # row wise

# np.mean(arr)
# np.max(arr)
# np.min(arr)
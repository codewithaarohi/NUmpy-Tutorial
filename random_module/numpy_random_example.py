
import numpy as np

#print(np.random.rand(10)) # 0-1 unfiromly distributed # 1D

#print(np.random.rand(3,4))

#print(np.random.randn(10)) # values close to 0, negative numbers gaussian distribution (normal distribution) mean = 0, std =1

#print(np.random.randn(4,5))

#print(np.random.randint(0,10))

#print(np.random.randint(0,10, size=(6,))) #1D

#print(np.random.randint(0,10, size=(4,3))) #1D


#np.random.seed(42)
#print(np.random.randint(0,10, size=(3,4)))

# shuffle
arr = np.array([1,2,3,4,5,6])
np.random.shuffle(arr)
#print(arr)

# without shuffle function
import numpy as np

# 0 = Not Spam, 1 = Spam
data = np.array([0, 0, 0, 0, 1, 1, 1, 1])
# Split (first 75% train, rest test)
train = data[:6]
test = data[6:]
print("Train:", train)
print("Test:", test)

'''
Train: [0 0 0 0 1 1]
Test: [1 1]
'''


# with shuffle function
import numpy as np

# 0 = Not Spam, 1 = Spam
data = np.array([0, 0, 0, 0, 1, 1, 1, 1])

np.random.shuffle(data)
# Split (first 75% train, rest test)
train = data[:6]
test = data[6:]
print("Train:", train)
print("Test:", test)


'''
# without shuffle
Train: [0 0 0 0 1 1]
Test: [1 1]

# with shuffle fnction
Train: [1 1 0 0 1 0]
Test: [0 1]
'''
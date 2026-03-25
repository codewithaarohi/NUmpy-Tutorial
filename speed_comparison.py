import time

import numpy as np

size = 10000000

list_a = list(range(size)) # []
list_b = list(range(size))

start = time.time()

result = []
for i in range(len(list_a)):
    result.append(list_a[i]+list_b[i])

#print("List:")
#print(result)

end = time.time()

print("List addition",end-start)


arr_a = np.array(list_a)
arr_b = np.array(list_b)

start = time.time()
result = arr_a + arr_b
end= time.time()
print("Array calculation: ", end-start)
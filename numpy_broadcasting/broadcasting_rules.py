
a.shape = (4, 3)  # 4 rows and 3 columns
b.shape = (3,) # 3 elements in a single row 

# Rule 1:
# compare from right side ( align them from right side)
a → (4, 3)
b →    (3)

a.shape = (4, 3)
b.shape = (1, 3)
# broadcasting will work in this scenerio

# Rule 1: Same number
# 3 vs 3 → OK

# Rule 2: One is 1
# 1 vs 3 → OK (1 will stretch)

# Rule 3:
'''
For example:
a.shape = (4, 3)
b.shape = (2,)

Align:
(4, 3)
(1, 2)'''
# 3 vs 2  (not equal, not 1)  ERROR 
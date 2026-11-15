"""
NumPy (Numerical Python) : It is a powerful library in Python for numerical computing.
Memory efficiency is more, speed -> very fast , math operations -> very powerful

"""
import numpy as np
""" 
#1D
a = np.array([1, 2, 3, 4, 5])
print(a) # [1 2 3 4 5]

#2D
b = np.array([[1, 2], [3, 4]])
print(b) # [[1 2]
          #[3 4]]

#ARRAY PROPERTIES
print(a.shape) # (5,)
print(b.shape) # (2, 2)
print(a.dtype) # data type -> int64
print(a.ndim) # num of dimestions : 1

# Array of zeros
zeros = np.zeros((2, 3))  # 2x3 matrix
print(zeros)

# Array of ones
ones = np.ones((3, 2))
print(ones)

# Random numbers
rand_arr = np.random.rand(2, 3)
print(rand_arr) #[[0.18952378 0.98795332 0.47655531]
                #[0.69091077 0.57960976 0.54027337]]

# Array with a range of values
range_arr = np.arange(0, 10, 2)
# from 0 to 10 (step 2)
print(range_arr)
# Array with evenly spaced values
linspace_arr = np.linspace(0, 1, 5)
print(linspace_arr) # 5 points between 0 and 1

"""
# Element-wise operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# Basic Statistics
data = np.array([1, 2, 3, 4, 5])

print(np.mean(data))
print(np.max(data))
print(np.min(data))
print(np.sum(data))
print(np.std(data))


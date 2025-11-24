import numpy as np

# arr = np.arange(12)
# print("Array:", arr)

# print("\n--- Basic Properties ---")
# print("Shape    :", arr.shape)
# print("Size     :", arr.size)
# print("ndim     :", arr.ndim)
# print("dtype    :", arr.dtype)

# matrix = arr.reshape(3, 4)
# print("\nReshaped to 3x4:\n", matrix)

# print("\nMatrix shape :", matrix.shape)
# print("Matrix ndim  :", matrix.ndim)
# print("Matrix size  :", matrix.size)
# print("Matrix dtype :", matrix.dtype)




# m = np.arange(1, 26).reshape(5,5)
# print(m[1:2, :])

arr3 = np.arange(1, 21)
print(arr3[arr3 > 12])
print(arr3[(arr3 < 10) & (arr3%2 == 0)])
print(arr3[arr3%3 != 0])
print(arr3[(arr3 >= 5) & (arr3 <= 15)])



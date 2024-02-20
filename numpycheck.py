import numpy as np
x = range(16)
x = np.reshape(x,(4,4))
print(x)
# indexing
print(x[0]) # first row data
print(x[:,0])  # first column data (all values in row)
print(x[0,0])
print(x[:2,0:3])

import numpy as np

"""
a = np.arange(1,7);
print(a);
print(a.shape);
b = reshape((2,3));
print(b);
print(b.shape);
"""

a = np.arange(1,7);
b = a[np.newaxis, :];
print(b);
print(b.shape);

b = a[:, np.newaxis];
print(b);
print(b.shape);

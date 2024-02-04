import numpy as np

l = [1,2,3];
n = np.array([1,2,3]);

print(l);
print(n);

l = l + [4];
n = n + np.array([4]);

print(l);
print(n);

l = l * 2;
n = n *2;

print(l);
print(n);

n = np.sqrt(n);
print(n);

n = np.log(n);
print(n);

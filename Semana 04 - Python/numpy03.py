import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([2,4,6,8,10])

print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[::2])
print(a1>3)
print(a1[a1>3])

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
names[first_letter_j]

print(a1%4)
print(a1%4==0)
print(a1[a1%4==0])

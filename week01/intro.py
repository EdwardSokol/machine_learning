# -*- coding: utf-8 -*-
import numpy as np

from utils import pretty_print

X = np.random.normal(loc=1, scale=10, size=(5, 2))
print('X', X)

pretty_print()

m = np.mean(X, axis=0)
print('m', m)

std = np.std(X, axis=0)
print('std', std)

X_norm = ((X - m) / std)
print('X_norm', X_norm)

pretty_print()

Z = np.array([[4, 5, 2],
              [1, 9, 3],
              [5, 1, 1],
              [3, 3, 3],
              [9, 9, 9],
              [4, 7, 1]])

r = np.sum(Z, axis=1)
print(np.nonzero(r > 10))

pretty_print()

A = np.eye(3)
B = np.eye(3)
print('A', A)
print('B', B)

AB = np.vstack((A, B))
print('AB', AB)

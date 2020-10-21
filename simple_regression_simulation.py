# %%
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
import random
import numpy as np


x_vector = [ 3, 5, 34, -14]
x12 = x_vector[0]
mean = np.average(x_vector)

# standard deviation
σ = 2

# x vector
u = norm.rvs(0, σ)

p_min_y = norm.cdf(0.2, 0, 1);
p_max_y = norm.cdf(0.8, 0, 1);

b_2 = 2
# probabilty variable
X = 0.4
b_1 = 0.4

## I don't know how to adgust b1 and b2.

#%%

# %%
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
import random
import numpy as np


## GOD STEP
exp = math.exp(1);

# β0
β1 = 0
# β1
β2 = random.uniform(math.log(exp) * 20/19, math.log(exp) * 80/79)

# 標準偏差
σ = 1

# 標本の大きさ
n = 4
x = norm.rvs(0, σ, size=n)
x12 = x[0]

y = β1 + β2*x12

## HUMAN STEP

# ロジスティック関数を定義
β2_candidates = []

for i in range(9):
    y = random.uniform(math.log(exp) * 20/19, math.log(exp) * 80/79)
    β2_candidates.append(y)


y_array  = []
for i in β2_candidates:
    y_array.append(x12 * i)

y_array
plt.plot(β2_candidates, y_array)

## make dots


#%%

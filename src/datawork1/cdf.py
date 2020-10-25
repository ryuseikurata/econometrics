import god_step as god
import numpy as np
from scipy.stats import norm

# %%
def cdf(y_vector):
    result = 0
    for y in y_vector:
        # X = bx = y - u
        X = y - god.getRisual()
        result += norm.cdf(X, god.getMean(), god.getSigma())


    return np.log(result)

# %%

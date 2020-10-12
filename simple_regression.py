# %%
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats.stats import describe
import wooldridge  # wooldridgeのデータ・パッケージ
from statsmodels.formula.api import ols  # 回帰分析のパッケージ
from see import see  # 属性を調べるパッケージ
from numba import njit  # シミュレーションの計算を高速化する

df = wooldridge.data('wage1')
df = df.loc[:, ['wage', 'educ']]

# 分散共分散行列(共分散 0,1, wageの分散00 educの分散が11)
mat_wage_educ = np.cov(df['wage'], df['educ'])
cov_wage_educ = mat_wage_educ[0, 1]

var_wage = mat_wage_educ[0, 0]
var_educ = mat_wage_educ[1, 1]

mean_wage = df['wage'].mean()
mean_educ = df['educ'].mean()

b1hat = cov_wage_educ / var_educ
b0hat = mean_wage - b1hat * mean_educ


formula = 'wage ~ educ'
mod = ols(formula, data=df)
res = mod.fit()
n = res.nobs
k = res.df_model
SST = res.centered_tss
SSE = res.ess
SSR = res.ssr

決定係数 = res.rsquared
修正済み決定係数 = res.rsquared_adj
決定係数
# %%

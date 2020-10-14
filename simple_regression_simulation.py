# %%
from scipy.stats import norm
import pandas as pd
from statsmodels.formula.api import ols  # 回帰分析のパッケージ
# 定数項
b0 = 1.0
# 説明変数の係数
b1 = 1.0
# 誤差項の標準偏差
su = 1.0

# 標本の大きさ
n = 30

x = norm.rvs(4, 1, size=n)
u = norm.rvs(0, su, size=n)
y = b0 + b1*x + u

df_sim = pd.DataFrame({'X': x, 'Y': y})

formula = 'X ~ Y'
res_sim = ols(formula, data=df_sim).fit()
res_sim.params
# %%

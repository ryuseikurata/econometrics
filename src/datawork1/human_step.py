# %%
import god_step as god
import matplotlib.pyplot as plt
import cdf as cdf

b2_candidates = [-20,-10, -5, -3, 2, 4, 6, 8, 9, 99 ]

result_array_logliklihood = []

for i in b2_candidates:
    y_vector = god.getOutcome(i)

    y_1_vector = []
    y_0_vector = []
    ## βxを求めるためにはX=(b1  + b2x)
    ## X=b1+b2x=y-u

    for y in y_vector:
        if y > 0:
            y_1_vector.append(y)
        else:
            y_0_vector.append(y)


    y_0_result = cdf.cdf(y_0_vector)
    y_1_result = cdf.cdf(y_1_vector)

    result_array_logliklihood.append(y_0_result+ y_1_result)

plt.plot(b2_candidates, result_array_logliklihood)
plt.xlabel('B2')
plt.ylabel('Log Liklihood')



print(result_array_logliklihood)
plt.show()
# %%









# %%

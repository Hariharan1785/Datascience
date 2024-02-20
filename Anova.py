import math
import numpy as np
import scipy.stats as ss
import pandas as pd

x = [29.1, 29.7, 28.9, 27.1, 25.7, 28.9, 29.9, 27.1, 29.3, 25.2, 29.5, 27.8, 29.8, 28.4, 26.0, 29.4, 26.4, 27.3]
pop_mean = 25

sample_mean = np.mean(x)
print("Sample Mean =", sample_mean)
sample_sd = np.std(x)
print("Sample Standard Deviation =", sample_sd)
std_error = sample_sd / math.sqrt(len(x))
print("Standard Error =", std_error)

## t-value
t_val = (pop_mean - sample_mean) / std_error
print("T Value/Score =", t_val)
P_Ho_normal = ss.norm.cdf(t_val)
print("P value =", P_Ho_normal)
if P_Ho_normal < 0.05:
    print("We reject Null Hypothesis and accept Alternative Hypothesis")
else:
    print("We fail to reject Null Hypothesis")

######### ANOVA ############
link="D:\\Users\\USER\\Downloads\\onewayAnova_data.csv"
data = pd.read_csv(link)
f_val, p_val = ss.f_oneway(data['A'],data['B'],data['C'],data['D'])
print("P-Val = ",p_val)
print("F-Val = ",f_val)

x = [29.1, 29.7, 28.9, 27.1, 25.7, 28.9, 29.9, 27.1, 29.3, 25.2, 29.5, 27.8, 29.8, 28.4, 26.0, 29.4, 26.4, 27.3]
import math
import numpy as np
import scipy.stats as ss
import pandas as pd

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

t_stats = ss.t.cdf(t_val, df=len(x) - 1)
print("T-Test =", t_stats)
#####################
# z-value
z_val = (sample_mean - pop_mean) / std_error
# observed (sample_mean) - expected (pop_mean)
print("Z Value/Score = ", z_val)
P_Ho_z = ss.norm.cdf(z_val)
print("Probability (P_Ho) =", P_Ho_z)

######### ANOVA ############
#link = "C:\\Users\\USER\\Downloads\\onewayAnova_data.csv"
#data = pd.read_csv(link)
#f_val, p_val = ss.f_oneway(data['A'], data['B'], data['C'], data['D'])
#print("P-Val = ", p_val)
#print("F-Val = ", f_val)

####### CHI SQUARED Test #######
# data = [[50,10,20,20],[150,30,60,60]]
data = [[20, 6, 30, 44], [180, 34, 50, 36]]
chi_sta, p, df, expected = ss.chi2_contingency(data)
print("P value =", p)
print("Degree of Freedom =", df)
print("Expected value\n", expected)
print("Chi Squared value =", chi_sta)
alpha = 0.05
if p > alpha:
    print("Null Hypothesis is retained: No relationship between colors and personality type")
else:
    print("Null Hypothesis is rejected: Colors impact personality type")

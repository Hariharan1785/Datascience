x =[2.8,3.9,6.9,4.8,2.7,5.8,3.8,8.9,9.7,4.8,2.6,1.6,8.7,6.8,9.9,9.8,9.3]
import math
import numpy as np
import scipy.stats as ss
import pandas as pd

pop_mean = 25
print("Population_Mean",pop_mean)
sample_mean = np.mean(x)
print("Sample Mean =",sample_mean)
sample_sd = np.std(x)
print("Sample Standard Deviation =",sample_sd)
std_error = sample_sd / math.sqrt(len(x))
print("Standard Error =", std_error)

## t- value Calculated
T_Value = (pop_mean - sample_mean) / std_error
print("T Value/Score =",T_Value)
P_Ho_normal = ss.norm.cdf(T_Value)
print("P Value =",P_Ho_normal)
if P_Ho_normal < 0.05 :
    print("We Reject Null Hypothesis and Accept Alternative Hypothesis")
else:
    print("We Fail to reject Null Hypothesis")

## T Statistics Calculation

t_stats = ss.t.cdf(T_Value, df=len(x) - 1)
print("T_Statistics =", t_stats);
###########################################################################

## Z_VALUE CALCULATION
Z_VALUE = (sample_mean - pop_mean) / std_error

# Observed(sample_mean) - expected (pop_mean)
print("Z Value/Score =", Z_VALUE)
P_Ho_z = ss.norm.cdf(Z_VALUE)
print("Probability (P_Ho) =", P_Ho_z)

###############################################################################
######### ANOVA Test ############
#link = "C:\\Users\\USER\\Downloads\\onewayAnova_data.csv"
#data = pd.read_csv(link)
#f_val, p_val = ss.f_oneway(data['A'], data['B'], data['C'], data['D'])
#print("P-Val = ", p_val)
#print("F-Val = ", f_val)

####### CHI SQUARED Test ########################################################
# data = [[50,10,20,20],[150,30,60,60]]
data = [[20, 6, 30, 44], [180, 34, 50, 36]]
chi_sta, p, df, expected = ss.chi2_contingency(data)
print("P value =", p)
print("Degree of Freedom =", df)
print("Expected value\n", expected)
print("Chi Squared value =", chi_sta)
alpha = 0.05
if p > alpha:
    print("Null Hypothesis is Accepted..Alternate Hypothesis Rejected: No relationship between colors and personality type")
else:
    print("Null Hypothesis is rejected --- Alternate Hypothesis Accepted: Colors impact personality type")


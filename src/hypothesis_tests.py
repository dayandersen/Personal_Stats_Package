import numpy as np
import src.general as gl
from scipy import stats
import math

# NOTE All 1 tailed t-tests are currently upper tailed
# TODO Change 1 tailed t-test to allow for lower tailed i.e. u < m0 

# 1.0 Two Sample T-Test
def two_sample_t_val_calc(dataset1, dataset2):
    mean1 = np.average(dataset1)
    mean2 = np.average(dataset2)

    variance1 = gl.variance_calc(dataset1)
    variance2 = gl.variance_calc(dataset2)

    return ((mean1 - mean2) / math.sqrt(
        variance1/np.size(dataset1)
    + variance2/np.size(dataset2)))

# NOTE Currently assumes the variance of the two datasets is the same and both are from normal distributions
# NOTE Calculates the one tail t-test value if tail == 1, and two tail if tail == 2
# NOTE If df (degrees of freedom) is not passed in it assumes that degrees of freedom is the size of the two datasets - 2
# NOTE Null hypothesis is that the two Samples have identical variances
# NOTE Returns True if we reject null hypothesis and False if we fail to reject

def two_sample_t_test(dataset1, dataset2, alpha, df, tail):
    degrees_free = 1

    if df == -1:
        degrees_free = np.size(dataset1) + np.size(dataset2) - 2
    
    else:
        degrees_free = df

    t = two_sample_t_val_calc(dataset1, dataset2) 
    crit_val = 1
    
    if (tail == 2):
        crit_val = stats.t.ppf((1-alpha)/2, degrees_free)
    else:
        crit_val = stats.t.ppf(1-alpha, degrees_free)

    print("I am the crit "+str(crit_val))

    return (abs(t) > abs(crit_val))

# ! t = Mean of group x - Mean of group y
# ! over the sqrt of
# ! std_devx squared over number of observations in x
# ! plus std_devy squared over number of observations in y


# 1.1 One Sample T-Test
def one_sample_t_val_calc(dataset, test_mean):
    sample_mean = np.average(dataset)
    sample_std_dev = gl.std_deviation_calc(dataset)
    
    return ((sample_mean - test_mean) /
            (sample_std_dev / math.sqrt(dataset.size())))


# Null hypothesis is that the sample mean is the same as the test_mean 
# True means we reject null hypothesis and False means we fail to reject

def one_sample_t_test(dataset, test_mean, alpha, tail):
    t_val = one_sample_t_val_calc(dataset, test_mean)
    crit_val = 0
    if (tail == 2):
       crit_val = stats.t.ppf((1-alpha)/2, (dataset.size()-1))
    else:
        crit_val = stats.t.ppf(1-alpha, (dataset.size()-1))

    return (abs(t_val) > abs(crit_val)) 

# 2. f-test

# def f_test():


# ! f = explained variance / unexplained variance

# ! explained variance = 
# ! sum i=1 to K 
# ! of number of observations in ith group (ni)
# ! times the sample mean in the ith group (ybari)
# ! minus the overall mean of the data (ybar)
# ! squared
# ! over (K-1) where K is the number of groups

# ! unexplained variance = 
# ! sum i = 1 to K
# ! of sum of j = 1 to ni
# ! of the jth observation in the ith 
# ! minus the sampel mean in the ith group 
# ! squared
# ! over (N-K) where N is total number of observations

# 3. z-test
# 4. Tukey-test
# 5. ANOVA
# 6. Pearson's chi-squared test
# 7. G-test
# 8. Pearson correlation coefficient

def pearson_coeff_calc(dataset1, dataset2):
    return (gl.covariance_calc(dataset1, dataset2) 
            /  (gl.std_deviation_calc(dataset1) 
              * gl.std_deviation_calc(dataset2)))

# 11. Hausman test
# 22. Wu-Haussman test
# 12. Dickey Fuller test
# 15. Pearson test
# 16. Fisher test
# 17. Spearman test
# 22. Principal component analysis + Factor analysis


# *Tests for variable correlation*


# *Tests for Heteroskedacity*
# 9. White test for heteroskedacity
# 10. Park test
# 18. Breusch Pagan test
# 19. Goldfeld–Quandt test

# *Tests for Autocorrelation*
# 13. Ljung-Box Q Test
# 14. Breusch Godfrey test
# 20. Durbin Watson test

# *Tests for non-linearity of data*

# *Tests for multicolinearity*
# 21. Variance inflation factor

import numpy as np
import general as gl
import math

# TODO List of tests I should add
# 1. t-test
def t_val_calc(data_set1, data_set2):
  mean1 = np.average(data_set1)
  mean2 = np.average(data_set2)

  variance1 = gl.variance_calc(data_set1)
  variance2 = gl.variance_calc(data_set2)

  return ((mean1 - mean2) / 
  math.sqrt(
    variance1/np.size(data_set1)
  + variance2/np.size(data_set2)))

def t_test(data_set1, dataset_2, alpha, df):

# ! t = Mean of group x - Mean of group y
# ! over the sqrt of
# ! std_devx squared over number of observations in x
# ! plus std_devy squared over number of observations in y
#

# 2. f-test

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

def pearson_coeff_calc(data_set1, data_set2):
    return (gl.covariance_calc(data_set1, data_set2) 
            /  (gl.std_deviation_calc(data_set1) 
              * gl.std_deviation_calc(data_set2)))

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

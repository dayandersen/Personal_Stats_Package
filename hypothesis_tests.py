import numpy as numpy
import general as gl

# TODO List of tests I should add
# 1. t-test
# 2. f-test
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

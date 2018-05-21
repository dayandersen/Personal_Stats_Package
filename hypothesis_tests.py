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
    import ols_calc
    return (ols_calc.covariance_calc(data_set1, data_set2) 
            /  (ols_calc.std_deviation_calc(data_set1) 
              * ols_calc.std_deviation_calc(data_set2)))

# 11. Hausman test
# 12. Dickey Fuller test
# 15. Pearson test
# 16. Fisher test
# 17. Spearman test

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


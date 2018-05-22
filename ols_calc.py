import numpy as np
import math
import hypothesis_tests as test
import general


# TODO
# * This file should only contain different types of regressions
# * For instance Multi Linear regression
# * Generalized Least squares regression
# * Weighted regression
# * Pooled OLS regression
# * Fixed effects estimators
# * Random effects estimators
# * ETC
# ! Need to move anything that is not involved in the above to another file

def main():
    # dependent_data   = np.array([1.0, 3.0, 5.0, 8.0], np.float64)
    dependent_data   = np.array([115, 120, 120, 160, 145, 175, 160, 185, 210], np.float64)
    
    # independent_data = np.array([[1.0,2.0,4.0],
    #                              [1.0,4.0,6.0],
    #                              [1.0,7.0,8.0],
    #                              [1.0,11.0,10.0]], np.float64)
    independent_data=np.array([[1,61], [1,62], [1,63], [1,65], [1,68],
                               [1,69], [1,70], [1,72], [1,75]], np.float64)
 
    # coeff_matrix = multiple_ols(independent_data, dependent_data)
    # print(coeff_matrix)
    # residuals = residuals_calc(coeff_matrix, independent_data, dependent_data)
    # print(residuals)

    # ssr = ssr_calc(residuals)

    # sigma_sqr = ssr/(len(dependent_data)-2)

    # print(sigma_sqr)
    column_specifier = 1
    # print(covariance_calc(independent_data[:,column_specifier], dependent_data))
    # print(std_deviation_calc(dependent_data))
    # print(variance_calc(dependent_data))
    print(test.pearson_coeff_calc(independent_data[:,column_specifier], dependent_data))
    

def multiple_ols(independent_data, dependent_data):

    independent_data_trans = independent_data.transpose()
    x_xtrans_product = np.matmul(independent_data_trans, independent_data)
    x_xtrans_product_inv = np.linalg.inv(x_xtrans_product)
    xtrans_y_product = np.matmul(independent_data_trans, dependent_data)
    coeff_matrix = np.matmul(x_xtrans_product_inv, xtrans_y_product)

    return coeff_matrix


# def mean_absolute_error(data):
# def correlation_calc():
# def estimate_variance():

#TODO 
# def generalized_least_squares():
# def weighted_least_squares():
# def least_squares_AR_errors():
# def robust_least_squares():
# def ARIMA_calc():
# def VAR_calc():


main()
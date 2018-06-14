import numpy as np
import math
import src.hypothesis_tests as h_test
import src.general

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
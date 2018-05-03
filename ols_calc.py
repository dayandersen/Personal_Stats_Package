import numpy as np

def main():
    dependent_data   = np.array([1.0, 3.0, 5.0, 8.0], np.float64)
    independent_data = np.array([[1.0,2.0,4.0],
                                 [1.0,4.0,6.0],
                                 [1.0,7.0,8.0],
                                 [1.0,11.0,10.0]], np.float64)
    # independent_data = np.array([[1.0,2.0],
    #                              [1.0,4.0],
    #                              [1.0,7.0],
    #                              [1.0,11.0]], np.float64)
 
    coeff_matrix = multiple_ols(independent_data, dependent_data)
    print(coeff_matrix)
    residuals = residuals_calc(coeff_matrix, independent_data, dependent_data)
    print(residuals)
    

def multiple_ols(independent_data, dependent_data):

    independent_data_trans = independent_data.transpose()

    x_xtrans_product = np.matmul(independent_data_trans, independent_data)

    x_xtrans_product_inv = np.linalg.inv(x_xtrans_product)

    xtrans_y_product = np.matmul(independent_data_trans, dependent_data)

    coeff_matrix = np.matmul(x_xtrans_product_inv, xtrans_y_product)

    return coeff_matrix

def residuals_calc(coeff_matrix, independent_data, dependent_data):

    residuals = np.zeros(len(dependent_data), np.float64, 'C')

    curr_estimate = 0.0

    for i in range(0,len(dependent_data)-1):

        for j in range(0,len(independent_data[0])-1):
            
            curr_estimate += coeff_matrix[j] * independent_data[i][j]

        residuals[i] = dependent_data[i] - curr_estimate

    return residuals




# def mean_squared_error():

# def variance():

# def covariance():


main()
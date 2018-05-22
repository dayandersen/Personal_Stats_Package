import numpy as np


def residuals_calc(coeff_matrix, independent_data, dependent_data):

    residuals = np.zeros(len(dependent_data), np.float64, 'C')
    curr_estimate = 0.0

    for i in range(0,len(dependent_data)):
        for j in range(0,len(independent_data[0])):
            
            curr_estimate += coeff_matrix[j] * independent_data[i][j]

        residuals[i] = dependent_data[i] - curr_estimate
        curr_estimate = 0.0

    return residuals


def ssr_calc(residuals):

    ssr = 0.0

    for i in residuals:
        ssr += (i*i)

    return ssr


def mean_squared_error(actual, predicted):

    mse = 0.0

    for i in range(len(actual)):
        mse +=  ((actual[i] - predicted[i]) * (actual[i] - predicted[i]))

    mse = mse * (1 / len(actual))

    return mse


def variance_calc(dataset):

    avg = np.average(dataset)
    variance = 0.0

    for i in dataset:
        variance += ((i - avg) * (i - avg))

    variance = variance * (1.0 / len(dataset))

    return variance

# NOTE: This calculates the population covariance for two datasets

def covariance_calc(dataset_1, dataset_2):
    
    covariance = 0.0
    avg_ds_1 = np.average(dataset_1)
    avg_ds_2 = np.average(dataset_2)
    
    for i in range(len(dataset_1)):
        covariance += ((dataset_1[i] - avg_ds_1) * (dataset_2[i] - avg_ds_2))

    covariance = covariance * (1.0 / len(dataset_1))

    return covariance

def std_deviation_calc(dataset):
    variance = variance_calc(dataset)
    return math.sqrt(variance)

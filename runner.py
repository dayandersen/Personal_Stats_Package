import numpy as np
import ols_calc
import hypothesis_tests as h_test

def main():
    dependent_data   = np.array([115, 120, 120, 160, 145, 175, 160, 185, 210], np.float64)
    independent_data = np.array([[1,61], [1,62], [1,63], [1,65], [1,68],
                                 [1,69], [1,70], [1,72], [1,75]], np.float64)
    column_specifier = 1
    # independent_data = np.array([[1.0,2.0,4.0],
    #                              [1.0,4.0,6.0],
    #                              [1.0,7.0,8.0],
    #                              [1.0,11.0,10.0]], np.float64)

main()
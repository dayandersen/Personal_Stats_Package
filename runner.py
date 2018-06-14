import sys
# sys.path.append('src')
import src.ols_calc
import numpy as np
import src.general as gl
import src.hypothesis_tests as h_test
from scipy import stats

def main():
    dependent_data   = np.array([115, 120, 120, 160, 145, 175, 160, 185, 210], np.float64)
    independent_data = np.array([[1,61], [1,62], [1,63], [1,65], [1,68],
                                 [1,69], [1,70], [1,72], [1,75]], np.float64)
    column_specifier = 1
    
    N = 50
    np.random.seed(0)
    #Normally distributed data with mean = 0 and var = 1
    a = np.random.normal(0,1,size=N)
    np.random.seed(2)
    #Normally distributed data with with mean = 2 and var = 1
    b = np.random.normal(2,1,size=N)

    t_two_samp = h_test.two_sample_t_val_calc(a,b)
    t_result_two_samp = h_test.two_sample_t_test(a, b, .95, -1, 2)

    print("t = " + str(t_two_samp))
    print("Two Tailed T-Test : Reject null hypothesis? " + str(t_result_two_samp))

    t_one_samp = h_test.one_sample_t_val_calc(a, 2)
    t_result_one_samp = h_test.one_sample_t_test(a, 2, .95, 2)

    print("t = " + str(t_one_samp))
    print("One Tailed T-Test : Reject null hypothesis? " + str(t_result_one_samp))

    print("F-Test : Reject null hypothesis?"h_test.f_test(a,b,.95,1))

    # independent_data = np.array([[1.0,2.0,4.0],
    #                              [1.0,4.0,6.0],
    #                              [1.0,7.0,8.0],
    #                              [1.0,11.0,10.0]], np.float64)

main()
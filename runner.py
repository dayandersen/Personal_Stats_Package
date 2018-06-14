import sys
import src.ols_calc
import numpy as np
import src.general as gl
import src.hypothesis_tests as h_test
import src.grapher as graph
from scipy import stats

def main():
    dependent_data   = np.random.normal(0.0,7.0,1000)
    independent_data_noconst = np.random.rand(1000,6)
    independent_data_const = np.insert(independent_data_noconst,0,1,axis=1)
    ols_coeff = src.ols_calc.multiple_ols(independent_data_const,dependent_data)
    print("Coefficients for regression were calculated to be\n" + str(ols_coeff))
    
    N = 50
    np.random.seed(0)
    #Normally distributed data with mean = 0 and var = 1
    a = np.random.normal(0,1,size=N)
    np.random.seed(2)
    #Normally distributed data with with mean = 2 and var = 1
    b = np.random.normal(2,1,size=N)

    print("The data for the tests below")
    print("set A is normally distributed, has mean 0, variance 1, size 50 \n"+str(a))
    print("set B is normally distributed has mean 2, variance 1, size 50 \n"+str(b))

    t_two_samp = h_test.two_sample_t_val_calc(a,b)
    t_result_two_samp = h_test.two_sample_t_test(a, b, .95, -1, 2)

    print("t = " + str(t_two_samp))
    print("Two Tailed T-Test testing if mean between two sets is the same at 95% confidence. \nReject null hypothesis? " + str(t_result_two_samp))

    t_one_samp = h_test.one_sample_t_val_calc(a, 2)
    t_result_one_samp = h_test.one_sample_t_test(a, 2, .95, 2)

    print("t = " + str(t_one_samp))
    print("One Tailed T-Test testing if mean is 2 at 95% confidence. \nReject null hypothesis? " + str(t_result_one_samp))

    print("F-Test : Reject null hypothesis? "+str(h_test.f_test(a,b,.95,1)))

    graph.graph(ols_coeff,dependent_data,independent_data_const)

main()
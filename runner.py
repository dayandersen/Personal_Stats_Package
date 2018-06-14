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
    #Normally distributed data with mean = 0 and var = 1
    a = np.random.normal(0,1,size=N)
    #Normally distributed data with with mean = 2 and var = 1
    b = np.random.normal(2,1,size=N)

    t = h_test.two_sample_t_val_calc(a,b)
    p = h_test.two_sample_t_test(a, b, .95,-1, 2)

    print("t = " + str(t))
    print("p = " + str(p))

    # independent_data = np.array([[1.0,2.0,4.0],
    #                              [1.0,4.0,6.0],
    #                              [1.0,7.0,8.0],
    #                              [1.0,11.0,10.0]], np.float64)

main()
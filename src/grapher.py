import matplotlib.pyplot as plt
import numpy as np

def graph(equation, dependent, independent):
    
    fitted_vals = []

    for i in independent:
        curr_val = 0
        for j in range(len(i)):
            curr_val += i[j]*equation[j]
        fitted_vals.append(curr_val)
    fig = plt.figure()
    plt.plot(fitted_vals,dependent,'bo')
    fig.suptitle('Example of graphing fitted values',fontsize=14)
    plt.xlabel('fitted',fontsize=10)
    plt.ylabel('actual',fontsize=10)
    plt.show()
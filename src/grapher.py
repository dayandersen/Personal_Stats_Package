import matplotlib.pyplot as plt
import numpy as np

def graph(equation, independent, **kwargs):
    
    dependent = kwargs.get('dependent', None)
    
    if (dependent):
        plt.scatter(independent, dependent)

    plt.plot(independent, equation)
    plt.plot()
    plt.show()
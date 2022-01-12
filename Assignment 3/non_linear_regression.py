import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def non_linear_regression_plot(df):
    from scipy.optimize import curve_fit
    from sklearn.metrics import r2_score
    y = list(df['$-r_{urea}$'])
    x=list(df['$C_{urea}$'])
    def non_linear(C,Vm,Km):
        return (Vm*C)/(Km+C)
    constants =curve_fit(non_linear,x,y)
    Vmax = constants[0][0]
    Km = constants[0][1]
    fit = []
    for i in x:
        fit.append(non_linear(i,Vmax,Km))
    r_squared = r2_score(y, fit)
    print('The R square value is ',r_squared)
    print('\n')
    print('The respective value for Vmax and km are',Vmax,' and ',Km)
    plt.plot(x, y, '.',label='Measurement value')
    plt.plot(x,fit,'-',label='Fitted curve')
    plt.xlabel('$C_{urea}$')
    plt.ylabel('$-r_{urea}$')
    plt.legend('Measurement value')
    plt.legend(loc='best')
    plt.title('Nonlinear Regression to Determine Michaelis-Menten Kinetics Parameters ')
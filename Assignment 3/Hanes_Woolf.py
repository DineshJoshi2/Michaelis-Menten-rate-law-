import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def Hanes_Woolf_plot(df):
    mpl.style.use(['ggplot'])
    #df.plot(kind='line',figsize=(15, 5), rot=0)
    plt.figure(figsize=(10,5)) 
    x=df['$C_{urea}$']/df['$-r_{urea}$']
    y=df['$C_{urea}$']
    #g=[df.iloc[0,1]/2 for i in range(len(df))]
    plt.plot(x,y)
    plt.xlabel('$C_{urea}$')
    plt.ylabel('$C_{urea}$/$-r_{urea}$')
    plt.title('Hanes Woolf Plot')
    #plt.plot(x,g)
    #plt.yticks(np.arange(0, df.iloc[0,1]+0.5, step=df.iloc[0,1]/2))
    #plt.yticks(np.arange(-0.03, 0.2))
    #idx = np.argwhere(np.diff(np.sign(y - g))).flatten()
    plt.annotate(' slope = 1/$V_{max}$',  # s: str. Will leave it blank for no text
               xy=(0.13, 0.125),  # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(0.15, 0.125),  # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',  # will use the coordinate system of the object being annotated
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))
    plt.annotate('1/$V_{max}$ ',  # s: str. Will leave it blank for no text
               xy=(10, 0.925926),  # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(80, 0.925926),  # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',  # will use the coordinate system of the object being annotated
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))

    plt.text(0.12, 0.025, 'y intercept = $K_m$/$V_{max}$')
    #plt.text(0.025, 0.01, '$K_M$')
    #print('Intersecton point is ',(y[idx][1],x[idx][1]))
    slope, intercept = np.polyfit(x,y,1)
    print('The of slope the plot is ',slope,', hence the value for Vmax is ',1/slope)
    print('\n')
    print('The intercept at the Y axis is ', intercept,', hence the value for Km is ',intercept*(1/slope))
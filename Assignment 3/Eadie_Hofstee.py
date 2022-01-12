import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def Eadie_Hofstee_plot(df):
    mpl.style.use(['ggplot'])
    #df.plot(kind='line',figsize=(15, 5), rot=0)
    plt.figure(figsize=(10,5)) 
    x= df['$-r_{urea}$']/df['$C_{urea}$']
    y=df['$-r_{urea}$']
    #g=[df.iloc[0,1]/2 for i in range(len(df))]
    plt.plot(x,y)
    plt.ylabel('$-r_{urea}$')
    plt.xlabel('$-r_{urea}$/$C_{urea}$')
    plt.title('Eadie Hofstee Plot')
    #plt.plot(x,g)
    #plt.yticks(np.arange(0, df.iloc[0,1]+0.5, step=df.iloc[0,1]/2))
    #plt.xticks(np.arange(0, 0.2, step=0.02))
    #idx = np.argwhere(np.diff(np.sign(y - g))).flatten()
    plt.annotate(' slope = -$K_M$',  # s: str. Will leave it blank for no text
               xy=(18, 0.8),  # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(23, 0.8),  # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',  # will use the coordinate system of the object being annotated
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))
    #plt.annotate('1/$V_{max}$ ',  # s: str. Will leave it blank for no text
    #           xy=(10, 0.925926),  # place head of the arrow at point (year 2012 , pop 70)
    #             xytext=(80, 0.925926),  # place base of the arrow at point (year 2008 , pop 20)
    #             xycoords='data',  # will use the coordinate system of the object being annotated
    #             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))

    plt.text(10, 0.6, 'Y intercept = $V_{max}$')
    #plt.text(0.025, 0.01, '$K_M$')
    #print('Intersecton point is ',(y[idx][1],x[idx][1]))
    slope, intercept = np.polyfit(x,y,1)
    print('The of slope the plot is ',slope,' and the value for Km is',-slope)
    print('\n')
    print('The intercept at the Y axis is ', intercept, 'therefore the value for Vmax is ', intercept)
    
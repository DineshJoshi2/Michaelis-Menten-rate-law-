import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def Lineweaver_Burk_plot(df):
    mpl.style.use(['ggplot'])
    #df.plot(kind='line',figsize=(15, 5), rot=0)
    plt.figure(figsize=(10,5)) 
    x= 1/df['$C_{urea}$']
    y=1/df['$-r_{urea}$']
    #g=[df.iloc[0,1]/2 for i in range(len(df))]
    plt.plot(x,y)
    plt.xlabel('1/$C_{urea}$')
    plt.ylabel('-1/$r_{urea}$')
    plt.title('Lineweaver Burk plot')
    #plt.plot(x,g)
    #plt.yticks(np.arange(0, df.iloc[0,1]+0.5, step=df.iloc[0,1]/2))
    #plt.xticks(np.arange(0, 0.2, step=0.02))
    #idx = np.argwhere(np.diff(np.sign(y - g))).flatten()
    plt.annotate(' slope = $K_M$/$V_{max}$',  # s: str. Will leave it blank for no text
               xy=(300, 7),  # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(350, 7),  # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',  # will use the coordinate system of the object being annotated
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))
    #plt.annotate('1/$V_{max}$ ',  # s: str. Will leave it blank for no text
    #          xy=(10, 0.925926),  # place head of the arrow at point (year 2012 , pop 70)
    #             xytext=(80, 0.925926),  # place base of the arrow at point (year 2008 , pop 20)
    #             xycoords='data',  # will use the coordinate system of the object being annotated
    #             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))

    plt.text(200, 2, 'Y intercept = 1/$V_{max}$')
    #plt.text(0.025, 0.01, '$K_M$')
    #print('Intersecton point is ',(y[idx][1],x[idx][1]))
    slope, intercept = np.polyfit(x,y,1)
    print('The slope of the plot is ',slope)
    print('\n')
    print('The intercept at the Y axis is ', intercept)
    print('\n')
    print('The Value for Vmax is',1/intercept)
    print('\n')
    print('The Value for Km is ',slope*(1/intercept))
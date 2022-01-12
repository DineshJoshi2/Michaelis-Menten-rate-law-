import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def Michaelis_Menten_plot(df):
    mpl.style.use(['ggplot'])
    #df.plot(kind='line',figsize=(15, 5), rot=0)
    plt.figure(figsize=(10,5)) 
    x= df['$C_{urea}$']
    y=df['$-r_{urea}$']
    g=[df.iloc[0,1]/2 for i in range(len(df))]
    plt.plot(x,y)
    plt.ylabel('-$r_{urea}$')
    plt.xlabel('$C_{urea}$')
    plt.title('Michaelis Menten plot')
    #plt.plot(x,g)
    idx = np.argwhere(np.diff(np.sign(y - g))).flatten()
    plt.yticks(np.arange(0, df.iloc[0,1]+0.5, step=df.iloc[0,1]/2))
    plt.xticks(np.arange(0, df.iloc[0,0], step=x[idx][1]))
    plt.annotate(' ',  # s: str. Will leave it blank for no text
                 xy=(x[idx][1], 0),  # place head of the arrow at point (year 2012 , pop 70)
                 xytext=(0, df.iloc[0,1]/2),  # place base of the arrow at point (year 2008 , pop 20)
                 xycoords='data',  # will use the coordinate system of the object being annotated
                 arrowprops=dict(arrowstyle='->', connectionstyle='angle,angleA=180,angleB=-90,rad=0', color='red', lw=2))

    #plt.text(0.18, 1.08, '$V_{max}$')
    #plt.text(0.025, 0.01, '$K_M$')
    print('Intersecton point is ',(y[idx][1],x[idx][1]))
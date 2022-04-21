import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
import numpy as np


def demand_curve(c,Q,y,pb):
    demand = (c.log(Q)-(-4.507+0.841*y+0.2775*pb))/(-0.397)
    return demand



def supply_curve_long_run(c,Q,N,X,pf,t):
    supply  = ((1 - 0.631)*c.log(N*Q+X) - (2.030 - 0.146*pf + 0.0184*t))/(0.221)
    return supply




def supply_curve_short_run(c,Q,N,X,pf,t,Q_fitted):
    supply = (((c.log(N*Q+X)-(2.030-0.146*pf+0.0184*t+0.631*c.log(N*Q_fitted+X)))) / 0.221)   
    return supply




def equate_q(y,pb,N,X,pf,t):
    Q = sp.symbols("Q")
    eq = sp.Eq(demand_curve(sp, Q, y, pb), supply_curve_long_run(sp, Q, N, X, pf, t))
    sol = sp.nsolve(eq,40)
    return float(sol)





def plot_year(df,year):


    #obtaining the relevant variables for year:
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['QPRODA']/1439-d['Q']*d['POP']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    

    
    #obtaining equilibrium quantity:
    Q_fitted=equate_q(y,pb,N,X,pf,t) 
    

    #plotting the functions:
    Q = np.linspace(0.1,100,100)
    plt.plot(Q,np.exp(demand_curve(np,Q,y,pb))*cpi, color = 'green', label = 'Etterspørsels kurve')
    plt.xlabel('Enheter')
    plt.ylabel('Pris')
    plt.ylim(0,400)

    Q = np.linspace(0.1,80,100)
    plt.plot(Q,np.exp(supply_curve_long_run(np,Q,N,X, pf, t))*cpi, color = 'brown', label = 'Langsiktig tilbud kurve')
    plt.xlabel('Enheter')
    plt.ylabel('Pris')
    plt.ylim(0,400)


    Q = np.linspace(0.1,80,100)
    plt.plot(Q,np.exp(supply_curve_short_run(np,Q,N,X,pf,t,Q_fitted))*cpi, color = 'blue', label = 'Kortsiktig tilbud kurve')
    plt.xlabel('Enheter')
    plt.ylabel('Pris')
    plt.ylim(0,400)
    plt.legend(frameon = False)
    
    plt.show()



def plot_year1(df,year):

    Q = sp.symbols('y, pb, N, X, pf, t')

    #obtaining the relevant variables for year:
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['QPRODA']/1439-d['Q']*d['POP']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    

    
    #obtaining equilibrium quantity:
    Q_fitted=equate_q(y,pb,N,X,pf,t) 
    
    Q = np.linspace(0.1, 100, 100)+.05
    #plotting the functions
    plt.plot(Q,np.exp(demand_curve(np,Q,y,pb))*cpi,  color = 'green', label = 'Etterpørsel kurve')
    plt.plot(Q,np.exp(demand_curve(np,Q+0.5,y,pb))*cpi,  color = 'purple', label = 'Etterpørsel kurve')
    plt.plot(Q,np.exp(demand_curve(np,Q,y+0.5,pb))*cpi,  color = 'brown', label = 'Etterpørsel kurve')
    plt.plot(Q,np.exp(demand_curve(np,Q,y,pb+0.5))*cpi,  color = 'black', label = 'Etterpørsel kurve')
    plt.plot(Q,np.exp(supply_curve_long_run(np,Q,N,X,pf,t))*cpi,  color = 'red', label = 'Langsiktig tilbud')
    plt.plot(Q,np.exp(supply_curve_short_run(np,Q,N,X,pf,t,Q_fitted))*cpi,  color = 'blue', label = 'Kortsiktig tilbud')
    plt.xlabel('Enheter')
    plt.ylabel('Pris')
    plt.ylim(0, 400)
    plt.legend(frameon = False)
    plt.title("")

    
    plt.show()
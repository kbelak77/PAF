#Napišite program u kojem korisnik definira iznos početne brzine v0 u m/si kut otklona θ u stupnjevima. 
#Neka program crta x − y, x − t i y − t graf za prvih 10 sekundi gibanja u dvije dimenzije. Diferencijalne jednadžbe
#rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.
import numpy as np
import matplotlib.pyplot as plt

def kosi_hitac(v0, kut_st):

    t=np.arange(0,10, 0.001)
    kut_rad= kut_st*np.pi/180

    brzine_y=np.zeros((len(t), 1))
    brzine_y[0]=float(v0*np.sin(kut_rad))
    list_y=np.zeros((len(t), 1))

    brzine_x=np.zeros((len(t), 1))
    brzine_x[0]=v0*np.cos(kut_rad)
    list_x=np.zeros((len(t), 1))
    v0_x=float(v0*np.cos(kut_rad))

    for j in range(len(t)-1):
        brzine_y[j+1]=brzine_y[j] - 9.81*0.001
        list_y[j+1]=list_y[j] + brzine_y[j]*0.001
        if list_y[j]<0:
            break
        xx=list_x[:j]
        yy=list_y[:j]

    for i in range(len(t)-1):
        list_x[i+1]=list_x[i] + v0_x*0.001

        
    plt.subplot(1, 3 ,1)
    plt.plot(xx,yy)
    plt.title('x-y graf')
    plt.xlabel('$x[m]$')
    plt.ylabel('$y[m]$')

    plt.subplot(1, 3 ,2)
    plt.plot(t,list_x)
    plt.title('x-t graf')
    plt.xlabel('$t[s]$')
    plt.ylabel('$x[m]$')

    plt.subplot(1, 3 ,3)
    plt.plot(t,list_y)
    plt.title('y-t graf')
    plt.xlabel('$t[s]$')
    plt.ylabel('$y[m]$')

    plt.show()

kosi_hitac(25, 80)




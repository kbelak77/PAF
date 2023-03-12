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

        list_x[j+1]=list_x[j] + v0_x*0.001
        if list_y[j]<0:
            break
        xx=list_x[:j]
        yy=list_y[:j]
        tt=t[:j]

        
    fig, axs = plt.subplots(2, 2)

    axs[0,0].plot(xx, yy)
    axs[0,0].set_title("x-y graf")
    axs[0,0].set_xlabel('$x[m]$')
    axs[0,0].set_ylabel('$y[m]$')

    axs[0, 1].plot(tt, xx)
    axs[0, 1].set_title('x-t graf')
    axs[0,1].set_xlabel('$t[s]$')
    axs[0,1].set_ylabel('$x[m]$')

    axs[1, 0].plot(tt, yy)
    axs[1, 0].set_title('y-t graf')
    axs[1,0].set_xlabel('$t[s]$')
    axs[1,0].set_ylabel('$y[m]$')

    plt.show()

kosi_hitac(25, 75)




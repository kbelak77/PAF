#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t
#i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte
#numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np
import matplotlib.pyplot as plt

def jednoliko(F, m):
    t=np.arange(0,10,0.001) #checkpointovi mjerenja 
    akc=np.zeros((len(t), 1))
    brz=np.zeros((len(t), 1))
    xevi=np.zeros((len(t),1))
    a=akc[0]=round(float(F/m), 3)

    for i in range(len(t)-1): 
        akc[i+1]=akc[i]
        brz[i+1]=float(brz[i]+ a*0.001)
        xevi[i+1]=float(xevi[i] + brz[i]*0.001)

   
    fig, axs = plt.subplots(2, 2)

    axs[0,0].plot(t, xevi)
    axs[0,0].set_title('x-t')
    axs[0,0].set_xlabel('$t[s]$')
    axs[0,0].set_ylabel('$x[m]$')

    axs[0,1].plot(t, brz)
    axs[0,1].set_title('v-t')
    axs[0,1].set_xlabel('$t[s]$')
    axs[0,1].set_ylabel('$v[m/s]$')

    axs[1,0].plot(t, akc)
    axs[1,0].set_title('a-t')
    axs[1,0].set_xlabel('$t[s]$')
    axs[1,0].set_ylabel('$a[m/s^2]$')

    plt.show()

jednoliko(-150,60)

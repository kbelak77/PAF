#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t
#i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte
#numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):
    t=np.arange(0,10,0.001) 
    akc=np.zeros((len(t), 1))
    brz=np.zeros((len(t), 1))
    xevi=np.zeros((len(t),1))
    a=akc[0]=round(float(F/m), 3)

    for i in range(len(t)-1): 
        akc[i+1]=akc[i]
        brz[i+1]=float(brz[i]+ a*0.001)
        xevi[i+1]=float(xevi[i] + brz[i]*0.001)

   
    plt. subplot(1, 3 ,1)
    plt.plot(t, xevi)
    plt.title('x-t')
    plt.xlabel('$t[s]$')
    plt.ylabel('$x[m]$')

    plt. subplot(1, 3 ,2)
    plt.plot(t, brz)
    plt.title('v-t graf')
    plt.xlabel('$t[s]$')
    plt.ylabel('$v[m/s]$')

    plt. subplot(1, 3 ,3)
    plt.plot(t, akc)
    plt.title('a-t graf')
    plt.xlabel('$t[s]$')
    plt.ylabel('$a[m/s^2]$')

    plt.show()

jednoliko_gibanje(-150,60)

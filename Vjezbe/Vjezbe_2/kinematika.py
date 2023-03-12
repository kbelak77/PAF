#Napišite svoj modul "kinematika.py" koji će sadržavati funkcije jednoliko_gibanje() i kosi_hitac(). Neka
#funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, iznos brzine, kut
#otklona, masa, vrijeme, ...) i neka crtaju iste grafove kao i u prošlim zadatcima.

import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):
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




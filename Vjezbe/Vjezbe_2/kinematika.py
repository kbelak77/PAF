#Napišite svoj modul "kinematika.py" koji će sadržavati funkcije jednoliko_gibanje() i kosi_hitac(). Neka
#funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, iznos brzine, kut
#otklona, masa, vrijeme, ...) i neka crtaju iste grafove kao i u prošlim zadatcima.

import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, ts):
    t=np.arange(0,ts,0.001) 
    akc=np.zeros((len(t), 1))
    brz=np.zeros((len(t), 1))
    xevi=np.zeros((len(t),1))
    a=akc[0]=round(float(F/m), 3)

    for i in range(len(t)-1): 
        akc[i+1]=akc[i]
        brz[i+1]=float(brz[i]+ a*0.001)
        xevi[i+1]=float(xevi[i] + brz[i]*0.001)

    plt.subplot(1, 3 ,1)
    plt.plot(t, xevi)
    plt.title('x-t')
    plt.xlabel('$t[s]$')
    plt.ylabel('$x[m]$')

    plt.subplot(1, 3 ,2)
    plt.plot(t, brz)
    plt.title('v-t graf')
    plt.xlabel('$t[s]$')
    plt.ylabel('$v[m/s]$')

    plt.subplot(1, 3 ,3)
    plt.plot(t, akc)
    plt.title('a-t graf')
    plt.xlabel('$t[s]$')
    plt.ylabel('$a[m/s^2]$')
    
    
    plt.show()


def kosi_hitac(v0, kut_st, ts):

    t=np.arange(0,ts, 0.001)
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




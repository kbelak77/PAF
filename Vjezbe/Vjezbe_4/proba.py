import particle as prt
import numpy as np
import matplotlib.pyplot as plt

#Zadatak 2
#Za česticu početne brzine v0 = 10 m/s i kuta otklona θ = 60 nacrtajte graf ovisnoti relativne pogreške
# numeričkog riješenja o vrijednosti vremenskog koraka ∆t

dts=[]
dt=0.001
while dt<=0.1:
    dts.append(dt)
    dt+=0.0001
greske=np.zeros(len(dts))

for i in range(len(dts)):
    t= dts[i]
    p1=prt.Particle(0,0,10,60,t)
    greske[i] = ((abs(p1.analit() - p1.range())*100)/p1.analit())

plt.plot(np.asarray(dts), greske)
plt.title('Apsolutna relativna greška dometa projektila')
plt.ylabel('Apsolutna relativna greška [%]')
plt.xlabel('dt [s]')
plt.show()
#Napišite program linregress.py za određivanje modula torzije Dt aluminijske šipke ako znamo da vrijedi
#M = Dt · φ. Parametri su nam zadani kao M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] Nm,
#φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] rad. 
import numpy as np
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
lista=[]
for i in range(len(M)):
    for j in range(len(M)):
        a=M[i]*fi[j]
        lista.append(a) #lista svih mogucih komb xy

#sred vrijedn x (kut)       
x=0
for el in fi:
    x+=el
sred_fi=x/len(fi)

#sred vrijednost umnoska xy
b=0        
for el in lista:
    b+=el
sred=b/(len(lista))

modul= sred/((sred_fi)**2)

c=0
for ell in M:
    c+=ell
sred_y=c/(len(M))

greska= np.sqrt((1/len(M)) * ( (sred_y**2 / sred_fi**2) - modul**2 ))

plt.scatter(fi, M, color = 'red')
plt.plot(np.asarray(fi), np.asarray(fi)*modul)
plt.xlabel('$\phi$ [rad]')
plt.ylabel('M [N/m]')
plt.title('D= {} +/- {}'.format(round(modul, 10),round(greska, 10)))
plt.show()




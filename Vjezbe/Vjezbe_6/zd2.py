#Razvijenom modulu dodajte metodu koja za zadane početne uvjete numerički računa period titranja. 
#Ispitajte preciznost metode u ovisnosti o veličini koraka ∆t.
import Harmonic as har
import matplotlib.pyplot as plt
import numpy as np

times = [0.05, 0.01, 0.001]
lista_x = []
lista_t = []

for el in times:
    h= har.Harmonic_Oscilator(50, -10, 10, el, 150)
    a, b, c, d = h.Oscilations() #a, v, x, t
    lista_x.append(c)
    lista_t.append(d)
k = 0
size = 0.9
txt= 'dt = {}'
for i in range(len(times)):
    c = times[i]
    k+= 10
    lista_1 = lista_t[i]
    lista_2 = lista_x[i]
    plt.scatter(lista_1[0::k], lista_2[0::k], s = size, label = txt.format(c))
    size+=0.9

def f1(d):
    return h.Amplituda()*(np.sin((2*np.pi*d)/h.Period_ana() - np.pi/2))
d = np.asarray(d)
plt.plot(d, f1(d), c = 'r', lw = 0.6, label = 'analitičko')
plt.legend(loc = 'lower right')
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.show()
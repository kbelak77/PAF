import Harmonic as har
import matplotlib.pyplot as plt

h1 = har.Harmonic_Oscilator(50, 0, 10, 0.01, 150, 20)
a, b, c, d = h1.Oscilations() #a, v, x, t
#plt.plot(b,a)
#plt.show()

#Koristeći razvijeni modul nacrtajte x − t, v − t i a − t graf za neke proizvoljno odabrane početne parametre.
plt.figure(1)
plt.plot(d, a)
plt.title('Graf a/t')
plt.figure(2)
plt.plot(d, b)
plt.title('Graf v/t')
plt.figure(3)
plt.plot(d, c)
plt.title('Graf x/t')
plt.show()
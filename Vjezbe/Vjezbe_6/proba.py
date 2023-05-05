import Harmonic as har
import matplotlib.pyplot as plt
import numpy as np

h1 = har.Harmonic_Oscilator(50, -10, 10, 0.01, 150, 5)

b = h1.Amplituda()
print(h1.Period(), h1.Period_ana())

#A = h.Amplituda()
#phase = h.faza()
#T = h.Period_ana()
disp = []
#for k in range(len(d)):
   # dis= A * np.sin(2*np.pi*d[k]/T + (T-phase))
    #disp.append(dis)
#(b) Napišite program pod (a) koristeći gotove module.

import numpy as np
t_list=[3,4,5,5,4,3,4,5,4,4]

print(np.mean(t_list))
print(np.std(t_list)/np.sqrt(len(t_list)-1)) #jer gotovi modul računa samo 1/N jer pretpostavlja rad s velikim iznosima

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os

#Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate unesene koordinate i pravac 
#koji prolazi kroz njih. Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi
#kao PDF. Dopustite korisniku da bira ime pod kojim će se spremiti graf.

def funkcija(x1, y1, x2, y2):
    x=[x1,x2]
    y=[y1,y2]
    a=input('Zelite li spremiti graf kao PDF file?')
    if a == 'da' or a == 'Da':
        ime=input('Kako zelite nazvati graf?')
        plt.plot(x,y)
        plt.savefig(ime + '.pdf')
        plt.close()
    else:
        plt.plot(x,y)
        plt.show()
        plt.close()



funkcija(5,6,8,3)
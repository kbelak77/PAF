#Napišite modul "harmonic_oscillator.py" koji će sadržavati klasu HarmonicOscillator s raznim metodama
#potrebnim za opis gibanja jednostavnog harmoničkog oscilatora u jednoj dimenziji. Koristeći razvijeni modul
#nacrtajte x − t, v − t i a − t graf za neke proizvoljno odabrane početne parametre. Ispitajte preciznost
#numeričkog rješenja za različite korake ∆t.
import numpy as np

class Harmonic_Oscilator:
    def __init__(self, m, x0, t, dt, k, v=0):
        self.v = v
        self.dt = dt
        self.t = t
        self.k = k
        self.x0 = x0
        self.x = self.x0
        self.m = m
        self.ts = []
        self.xs = []
        self.vs = []
        self.accelerations = []
        self.times=[]

    def __move(self):
        self.a = -(self.k/self.m)*self.x
        self.accelerations.append(self.a)
        self.v += self.a*self.dt
        self.vs.append(self.v)
        self.x += self.v * self.dt
        self.xs.append(self.x)
    
    def Oscilations(self):
        self.i = 0
        while self.i<=self.t:
            self.ts.append(self.i)
            self.__move()
            self.i+= self.dt

        return self.accelerations, self.vs, self.xs, self.ts
    
    def PrintInfo(self):
        print('Brzina', self.v)
        print('Položaj', self.x[-1])

    #Razvijenom modulu dodajte metodu koja za zadane početne uvjete numerički računa period titranja. 
    def Start_Point(self):
        return self.x0
    
    def Amplituda(self):
        self.t0=0
        self.list_x = []
        while self.t0<=self.t:
            self.__move()
            self.t0+= self.dt
            self.list_x.append(self.x)
        return (max(self.list_x)-min(self.list_x))/2

    def Period(self):
        self.x = self.Amplituda()
        self.v = 0
        self.xp = 0
        for i in np.arange(0, self.t, self.dt):
            self.xp = self.x
            self.__move()
            if (self.xp>0 and self.x<0) or (self.x>0 and self.xp<0):
                break
        return i*4
    
    def Period_ana(self):
        return 2*np.pi*(np.sqrt(self.m/self.k))
    
    def faza(self):
        return np.arccos(self.Start_Point()/self.Amplituda())
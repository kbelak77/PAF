import math
class Particle:
    def __init__(self, x, y, v, kut, dt):
        self.x = x
        self.dt = dt
        self.y = y
        self.v = v
        self.v_0 = v
        self.kut= math.radians(kut)
        self.vx = v * math.cos(self.kut)
        self.vy = v * math.sin(self.kut)
        self.g = -9.81
        #self.dt = 0.01
        self.xs = [x]
        self.ys = [y]

    def __move(self): #metoda koja ju pomice za dt
        self.x += self.vx*self.dt
        self.y += self.vy*self.dt
        self.xs.append(self.x)
        self.ys.append(self.y)
        self.vy += self.g*self.dt
        self.v= math.sqrt(self.vx**2 + self.vy**2)


    def kosi_hitac(self): #u cijelosti gibanje
        while self.y>=0:
            self.__move()
        self.y = self.ys[-2]
    
    def printInfo(self):
        print('Brzina', self.v)
        print('Kut otklona', self.kut)
        print('Polozaj x', self.x)
        print('Polozaj y', 0)

    def reset(self):
        self.kut = 0
        self.x = 0
        self.y = 0
        self.v = 0
    
    #def pomak(self):
        #self.__move()
    #metodu range() koja numerički računa domet projektila
    #metodu plot_trajectory() koja crta putanju u x − y ravnini za trenutno stanje čestice
    def range(self):
        while self.y>=0:
            self.__move()
        return self.x
    
    def plot_trajectory(self):
        import matplotlib.pyplot as plt
        plt.plot(self.xs, self.ys) #ovisno gdje ju movam ce pokazat trenutno stanje
        plt.show()

#analitički domet
    def analit(self):
        return ((self.v_0**2)/(-1*self.g))*math.sin(2*self.kut)
        #print('Domet je:', ((self.v_0**2)/(-1*self.g))*math.sin(2*self.kut))

#p=Particle(0,0,10,60)
#p.printInfo()
#p.range()
#p.analit()
#p.printInfo()
#p.plot_trajectory()
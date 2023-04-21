#Prva metoda kao ulazne parametre prima funkciju i točku, a kao rezultat vraća vrijednost derivacije funkcije u toj točki.
#Druga prima kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije. Funkcija korisniku vraća listu točaka 
#u kojima će biti izvršena numerička derivacija na zadanom rasponu i iznose derivacije funkcije u tim istim točkama
import numpy as np

def derivacija(fja, t, d, m=0):
    if m==1:
        return (fja(t+d)- fja(t))/d
    else:
        return (fja(t+d)- fja(t-d))/(2*d)

def raspon(fja, d, g, dx, m=0):
    derivacije=[]
    tocke=[]
    for i in np.arange(d, g, dx*5):
        der= derivacija(fja, i, dx, m)
        tocke.append(i)
        derivacije.append(der)
    return derivacije, tocke

# funkciju, granice integracije i broj podjela za numeričku integraciju

def integracija(fja, d, g, N):
    dx= (g-d)/N
    i = 0
    donja = 0
    gornja = 0
    while i < N: #izvrsavat ce se za onoliko koraka
        donja+= fja(d)*dx
        gornja+=fja(d+dx) * dx
        d+=dx
        i+=1
    return donja, gornja

def trapezna(fja, d, g, N):
    dx = (g-d)/N
    trapez=0
    i=0
    while i< N:
        trapez += (fja(d) + fja(d+dx))*(dx/2)
        d+=dx
        i+=1
    return trapez

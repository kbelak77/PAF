#Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. Neka ta funkcija na
#ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu

def pravac(x1, y1, x2, y2):
    k=round(float((y2-y1)/(x2-x1)), 3)
    l=round(float(y1-k*x1), 3)
    print('Jednadzba pravca je: y=', k,'x +', l)


pravac(4,5,6,7)
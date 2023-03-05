#Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. Neka ta funkcija na
#ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu

def funkcija(x1, y1, x2, y2):
    l=float((y1-(x1/x2)*y2)/(1-(x1/x2)))
    k=float((y2*(1+(x1/x2))-y1)/(x2-x1))
    print('Jednadzba pravca je: y=', k,'x +', l)


funkcija(4,5,6,7)
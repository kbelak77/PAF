#Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. 
#Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate
#ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke

while True:
    try:
        x1,y1 = [int(x) for x in input('(x1, y1): ').split(',')]
        x2,y2 = [int(x) for x in input('(x2, y2): ').split(',')]
        if x1!=x2:
            break
        else:
            print('Molim ponovite upis.')
    except:
        print('Unijeli ste string')

k=round(float((y2-y1)/(x2-x1)), 3)
l=round(float(y1-k*x1), 3)

print('Jednadzba pravca je: y=', k,'x +', l)



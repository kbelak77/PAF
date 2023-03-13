#Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. 
#Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate
#ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke
listax=[]
listay=[]
i=0

while i<2:
    try:
        x=float(input())
        y=float(input())
        listax.append(x)
        listay.append(y)
    except:
         print('Molim unesite broj')
    x1,x2= listax
    y1,y2= listay
    try:
        x1!=x2
        i+=1
    except:
        print('Unijeli ste iste koord.')


k=round(float((y2-y1)/(x2-x1)), 3)
l=round(float(y1-k*x1), 3)

print('Jednadzba pravca je: y=', k,'x +', l)



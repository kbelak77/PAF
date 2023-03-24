#Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5.
#Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.

def funkc(N):
    b=5
    for i in range(N):
        b+=(1/3)
    for j in range(N):
        b-=(1/3)
    return b

print(funkc(200))
print(funkc(2000))
print(funkc(20000))

#Očekivani rezultat bi bio 5, jer smo jednako puta nadodali i oduzeli 1/3. Međutim, program ne vraća točno 5 već približno,
#iz razloga što ne može tretirati 1/3 kao točnu vrijednost već ju mora aproksimirati pa se pri zbrajanju/oduzimanju
#javlja određeno odstupanje.
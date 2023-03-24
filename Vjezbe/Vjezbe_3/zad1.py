#(a) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? Koji rezultat dobijete koristeći Python? Objasnite.
#(b) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. Objasnite rezultat koji ste dobili.


a=5.0
b=4.935

#Ocekivani rezultat je 0.065
print(a-b)
#Rezultat koji Python vraća je 0.06500000000000039
x=0.1
y=0.2
z=0.3

print(x+y+z == 0.6)
#Python vraća vrijednost False tj. tvrdi da 0.1+0.2+0.3 nije 0.6
#Python radi s decimalnim brojevima na način da ih pretvara u binarni zapis tj prikazuje ih preko baze 2. 
#Problem je u činjenici da se ne može svaki decimalni broj dobro prikazati preko baze 2, već dostojno može prikazati samo decimalne 
#bliske obliku 1/(2^n). Što decimalni zapis više odstupa od tog oblika, Python mora primjeniti veću aproksimaciju,
#što znači da se na određenom mjestu u zapisu neće pronaći jednake znamenke zbog čega će javiti da brojevi nisu jednaki.
#Python rezervira mjesto od 64 bita za float vrijednosti, stoga neki brojevi u memoriji imaju/nemaju identican zapis.

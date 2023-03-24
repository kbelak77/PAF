#(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2.
#(b) Napišite program pod (a) koristeći gotove module.
import math
t_list=[3,4,5,5,4,3,4,5,4,4]

#formula za sr vrijednost:
def aritm(lista):
    sr=0
    for el in lista:
        sr+=el
    return sr/len(lista)

a=aritm(t_list)
print(aritm(t_list))

#devijacija
def devijacija(lista):
    d=0
    for el in lista:
        d+=(el-a)**2
    return math.sqrt(d/(len(lista)*(len(lista)-1)))

print(devijacija(t_list))


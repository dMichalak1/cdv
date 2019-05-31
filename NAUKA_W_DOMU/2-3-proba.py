nazwisko = "Michalak"
print(nazwisko[len(nazwisko)-1])
print(nazwisko[0])
print(nazwisko[-1])
print(nazwisko[-2:])
print(nazwisko[2:4])
###########
print("\n")
tekst=("Daniel, Jagoda, Olek")
lista = tekst.split(", ")
print(tekst)
print(lista[1])
#print(type(lista))
imie1=lista[0]
print(imie1)
imieDuze=imie1.upper()
print(imieDuze)
imieMale=imie1.lower()
print(imieMale)
#print("Podaj nowe nazwisko: ",end="")
#nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
print(type(zawartosc))
tekst1="\nDaniel\n"
tekst2="Michalak"
print(tekst1 + tekst2)
tekst1=tekst1.rstrip()
print(tekst1 + tekst2)
print(tekst1 +" "+ tekst2)
dzien=12
miesiac="Marzec"
rok=2019
print("\nData: ",end="")
print(dzien,miesiac,rok,sep="-")
text ="%s, python, %s" % ("PHP","JAVA")
print(text)
text="{1}, JAVA,{0} " .format("Python","PHP")
print(text)
text=text.replace("PHP","C#")
print(text)
import math
pi=math.pi
print(pi)
pierwiastek=math.sqrt(9)
print(pierwiastek)
import random
losuj = random.random()
print(losuj)
losujz =random.choice([12,22,3,4,2])
print(losujz)

tekst = "Anna, paweł, JuLIa"
lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista)) #list
imie1 = lista[0]
print(imie1) #Anna
print("Twoje imie: ",imie1)

imieDuze = imie1.upper()
print(imieDuze) #ANNA

imieMale = imie1.lower()
print(imieMale) #anna
print(imie1) #Anna

#Sprawdzanie zawartosci
print("\nPodaj nowe nazwisko: ",end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
#Sprawdzic dlaczego przy liczbach jest false
nazwisko = ""
print(nazwisko.isalpha())
text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 +  " "  + text2)
#wyswietlanie łancucha znakow
#wszystkie wersje pythone
text = "%s, Java i %s" % ("PHP","Pythone")
print(text)
#nowsze wersje
text = "{1},Java i {0}".format("PHP","Pythone")
print(text)
#help(text.replace)
new = text.replace("PHP","C#")
print(new)
#wypisanie danych
rok = 2019
miesiac = "marzec"
dzien = 25

print("\nData: ", end="")
print(dzien,miesiac,rok,sep="-")
















print()

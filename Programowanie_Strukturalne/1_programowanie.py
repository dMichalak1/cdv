print("CDV")
#pobieranie danych z kl
#imie=input()

#print("Twoje imie podane z klawiatury: "+imie)
#nazwisko=input()
#print("Twoje nazwisko podane z klawiatury: "+nazwisko)

#dlugosc=len(nazwisko)

#dlugosc=len(dlugosc)
#print(type(dlugosc))
#print("DL nazwiska: ",dlugosc)

#dlugosc=str(dlugosc)
#print(type(dlugosc))
#print("DL nazwiska: "+dlugosc)
print("\nPodaj swoj wiek: ", end="")
wiek = input()
print(type(wiek)) #string
print("Twój wiek: ",wiek, "lata")

nazwisko = 'Kowalski'
pierwszyZnak = nazwisko[0];
print(pierwszyZnak) #K

ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak) #i

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

x = "5"
print(type(x)) #str
x = int(x)
print(type(x)) #int

text = "Jan" * 2
print(text)
print(type(text)) #str

y = 6
print(type(y)) #int
y = y / 2
print(type(y)) #flout
print(y) #3.0

wiek = 21
print("Twoj wiek: ",wiek)
wiek=str(wiek)
print("Twoj wiek: " +wiek)

nazwisko = "Jankowski"
print(nazwisko[0])   #J
print(nazwisko[0:3]) #Jan
print(nazwisko[-2])  #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Jankows
print(nazwisko[:-2:2]) #Jnos
print(nazwisko[::2]) #Jnosi

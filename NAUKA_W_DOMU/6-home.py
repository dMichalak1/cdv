'''
#sprawdzanie zawartosci
print("Podaj imie: ",end="")
imie = input()
zawartosc=imie.isalpha()
print(zawartosc)
'''
#listy
lista=["PHP","C#","PYTHON"]
lista.append("PHP")
lista.append("DANIEL")
print(lista)
ile = lista.count("PHP")
print(f'PHP wystapilo {ile} razy')
#tuple
imiona=("daniel","Julia","Kamil")
print(type(imiona))
print(imiona[0])
#slowniki
osoba = {
  'imie':'Janusz',
  'nazwisko':'Nowak',
  'miasto':'Poznan',
  'wiek':21,
  'UmowaOPrace':True
}
print(osoba)
print(type(osoba))
print(osoba['miasto'])
print(osoba['wiek'])
print(osoba.keys())

def wyswietl(num1,num2):
  print(f'liczba numer 1 to: {num1}')
  print(f'liczba numer 2 to: {num2}')
wyswietl(3,8)

def wyswietlargs(num1,*args):
  print(f'Pierwszy element z listy to: {num1}')
  for i in args:
    print(f'Nastepny element to : {i}')
number = ("a, da, ada, ad, da")
lista=number.split(", ")
print(lista[1])
wyswietlargs(2,3,32,32,32,3,1,23,32,4,23,233)
###############################
print()
imiona=['daniel','bartek','olek','janusz']
wyswietlargs(imiona)
wyswietlargs(*imiona)
print()
wyswietlargs(*lista)
############kwargs##############

def wyswietlkwargs(**kwargs):
  for key,val in kwargs.items():
    print(f'Klucz: {key} ma wartosc: {val}')

pracownik1 = {
  'imie':'daniel',
  'nazwisko':'michalak',
  'wiek':19,
  'miasto':'Poznan',
  'status':'student',
}
wyswietlkwargs(**pracownik1)

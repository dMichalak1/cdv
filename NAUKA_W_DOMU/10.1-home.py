#Podaj wartosc początkową i końcową,która będzie wypisana w porządku malejącym
'''
a = int(input('Podaj wartosc: '))
b = int(input('Podaj wartosc: '))
if a>b:
  x = b
  y = a
else:
  x = a
  y = b

for i in range(y,x-1,-1):
  print(i,end=' ')
znak = input('Podaj znak: ')
ile =int(input('ile wierszy :'))
j=1
for i in range(1,ile+1):
    print(znak*j)
    j+=1;
  '''
for letter in ('CDV POZNAN'):
    if letter=='V':
      continue
    print(letter,end="")
print()
x = 10
while x>0:
    x=x-1
    if x == 5:
      continue
    print(f'{x}',end=' ')
print('koniec')
#Użytkownik podaje z klawiatury hasło,jeśli poda hasło: 'okon'
#to na ekranie wyswietlamy mu komunikat: 'Poprawne haslo'
#Uzytkowanik ma na podanie hasla trzy proby ,Jesli przekroczy ilosc prob to na ekranie
#pojawi mu sie komunikat przekroczono limit prob podania hasla
'''
import os
os.system('cls')
for i in range(0,3):
    haslo = input(f'Podales haslo po raz {i+1}: ')
    if haslo =='okon' or haslo=='test':
      print("Poprawne")
      break
    else:
      print("Bledne haslo")
      if i==2:
        print("to była ostatnia proba")
print("koniec")
'''
haslo=""
while haslo!="okon":
  haslo = input('podaj haslo: ')

print('poprawne haslo')

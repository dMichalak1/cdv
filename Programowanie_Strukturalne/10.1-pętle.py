#pętle zadania
'''
Podaj wartosc początkową i końcową,która będzie wypisana w porządku malejącym

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
if y>x:
    pom = x
    x = y
    y = pom

for i in range(x,y-1,-1):
    print(i,end=" ")

print('\n\n')


*
**
***
****
*****

i=1
for i in range(0, 1):
    for i in range(1, 6):
        print(i * "*")
        i=i+1

for i in range(1,6):
    for j in range(1,i+1):
     print('*',end="")
    print()

i=1
ilosc = int(input('Ilosc wierszy: '))
znak = input('Znak: ')
for i in range(1,ilosc+1):
    print(znak * i)
    i=i+1
'''

#############################################
#oblicz wartosc wyrazenia
    #(a^2+b)/(a+b)^2

a = float(input('Podaj liczbe a: '))
b = float(input('Podaj liczbe b: '))
if (a*b)==0:
    print("BŁĄD")
wynik = (a*a+b)/((a+b)*(a+b))
print(f"Wynik to: ",wynik)
############ zadanie ############
suma = a + b
if suma==0:
    print('Proba dzielenia przez zero')
else:
        wynik = (a*a+b)/((a+b)*(a+b))
if suma!=0:
    print(f'wynik to: ',wynik)

#############  wyswietla bez litery V #############################
for letter in 'CDV Poznań':
    if letter== 'V':
        continue
    print(f'Litera: {letter}',end=" ")

############# WHILE  ##########################

x = 10
while x>0:
    x  = x-1
    if x == 6:
        continue
    print(f'{x} ')
print('Koniec programu')

######################### zadanie ##########
'''
Użytkownik podaje z klawiatury hasło,jeśli poda hasło: 'okon'
to na ekranie wyswietlamy mu komunikat: 'Poprawne haslo'
Uzytkowanik ma na podanie hasla trzy proby ,Jesli przekroczy ilosc prob to na ekranie pojawi mu sie komunikat przekroczono limit prob podania hasla
'''
#moja propozycja
for i in range(0,3):
    haslo = input(f'Podaj haslo: ')
    if haslo=='okon':
        print(f'Poprawne haslo!!!')
        break

if i+1 == 3:
    print('przekroczono limit prob podania hasla!!!')


#propozycja nauczyciela
'''
while password != 'okon' or password == 'test':
    print('ok')
    password = input('Podaj haslo: ')
'''
os.system('cls')
count = 1
password = input('Podaj haslo ')

while password != 'okon' and cout !=3
    count=count + 1
    password = input('Podaj haslo: ')
if password =='okon':
    print(f'haslo oddgadniete za {count} proba ')
if count ===3 and password != 'okon':
    print('przekroczono limit prob podania hasla!!!')
    ###############################







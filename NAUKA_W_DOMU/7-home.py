def Witaj():
  print("Witaj",end=" ")
  print("Janusz")
def wyswietlWiek(wiek):
  print(f'Wiek Janusza to: {wiek}')
Witaj()
wyswietlWiek(40)

def iloczyn(a,b):
  return a*b
x=int(input('Podaj x: '))
y=int(input('Podaj y: '))

print(f'iloczyn wynosi: {iloczyn(x,y)}')

def iloraz(a,b):
  return a/b

print("iloraz wynosi: ",iloraz(2,4))
print("iloraz wynosi: ",iloraz(b=2,a=4))

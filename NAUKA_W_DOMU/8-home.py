def plnToEuro(value,kurs):
  ile=value/kurs
  ile="{0:.3f}".format(ile)
  print(f'ilosc wynosi: {ile}')

value=float(input('Podaj ile zlotych: '))
kurs = float(input('Podaj kurs: '))
plnToEuro(value, kurs)

zmienaglobalna = 10
def spr():
  global zmienaglobalna
  zmienaglobalna = 20

spr()
print(zmienaglobalna)

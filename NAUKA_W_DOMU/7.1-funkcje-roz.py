def show(name):
      print(f'przed: {name}')
      print(f'id przed: {id(name)}')
      name[0]='Bogdan'
      name[1]='Kamila'
      name[2]='Jagoda'
      print(f'po: {name}')
      print(f'id po: {id(name)}')

data=["Daniel","Dawid","Bartek"]
print(f'przed: {data}')
print(f'id przed: {id(data)}')
#print(type(data))
show(data)
print(f'przed: {data}')
##slownik

data1 = {
  'imie':'Daniel',
  'nazwisko':'Michalak',
}

print(f'\nid przed: {id(data1)}')

show(data1)
##################################

print("\n\n")

def show1(city):
  print(f'przed modyfikacja: {city}')
  print(f'ID przed modyfikacja: {id(city)}')
  city[0]='Warszawa'
  city[1]='Krakow'
  print(f'PO modyfikacja: {city}')
  print(f'ID PO modyfikacja: {id(city)}')


miasta = ['Poznan','Gniezno']
print(f'przed Funkcja: {miasta}')
print(f'ID przed Funkcja: {id(miasta)}')
show1(list(miasta))
print(f'PO  funkcji: {miasta}')
print(f'ID Po funkcji: {id(miasta)}')

print('\n\n')

def show2(city):
  city[0] = 'Londyn'
  city[1] = 'Berlin'
  print(city)
miasto = {
  0:'Wolszyn',
  1:'Widziszewo',
}
print(miasto)
show2(list(miasto)
print(miasto)

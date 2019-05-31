programowanie = ['python','php','java','c#',"js"]
print(programowanie)
print(type(programowanie))
first = programowanie[0]
last = programowanie[-1]
threelist = programowanie[:3]
print(f'1 element: {first}')
print(f'ostatni element: {last}')
print(f'trzy elementy: {threelist}')
programowanie.append("R")
print(programowanie)
programowanie.append("python")
print(programowanie)
ile = programowanie.count("python")
print(f'ile razy python: {ile}')
ileele= len(programowanie)
print(f'ile elementow w liscie: {ileele}')
print("\n",programowanie)
newjezyk=["C","C++"]
programowanie.extend(newjezyk)
print(programowanie)

nowa=programowanie
print(id(nowa))
print(id(programowanie))
nowa.append("Go")
print(nowa)
print(programowanie)

nowa.clear()
print(programowanie)

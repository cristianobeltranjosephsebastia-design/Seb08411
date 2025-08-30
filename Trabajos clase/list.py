lista=['Jose','Miguel','Luis','Pedro','Pablo','Ivan','Juan']
print(lista[5])
print(lista[0])
print(lista[2:5])


for i in lista:
    print(i)


list2 = lista
print (list2) 

list2 = lista[2:4]
print (list2)

list2 = lista[:]
print (list2)

list2 = lista[:: -1]
print (list2)

list2 = lista[-3]
print (list2)

list2 = [1,2,5,7,9,8,10,12,15,20,30]
lista [6]="ElPepe"
print(lista)

lista.append("Pedro-Pablo")
print(lista)

lista.insert(6,"Juanito")
print(lista)

lista.extend(["Jose", "Carlos", "Karen"])
print(lista)

lista.remove("Pablo")
print(lista)

lista.pop(3)
print(lista)

for i in range (len(list2)):
    print(i, ":", list2[i])

list3= "Ivan" in lista
print(list3)

list4 = ["a","a","b","b","c","c","a"]
cantidad = list4.count("a")
print(cantidad)

cantidad = lista.count("Ivan")
print(cantidad)

print(lista.sort())

list5=(lista.sort())
print(lista)

list5=(list2.sort())
print(list2)

list6 = sorted(lista)
print(list6)

lista = sorted(lista)
print(lista)

lista.reverse()
print(lista)

list6=lista.copy()

list7=list(lista)
print(list6)
print(list7)


lista.clear()
print(lista)
###Datatyper

##Listor
# http://docs.python.org/3.1/tutorial/datastructures.html

minLista = [1,2,3,4,6]
print(minLista)

#lägger till 3 på slutet
minLista.append(3)
print(minLista)

#Tar bort tredje värdet (börjar räkna på 0) och returnerar detta värde
poppad = minLista.pop(2)
print(minLista)
print(poppad)

#Går genom minLista och lagrar varje position i nr
for nr in minLista:
	print(nr*nr)

#Gör det första på alla positioner i listan. Ges som returvärde i en lista
kvadratLista = [nr*nr for nr in minLista]
print(kvadratLista)

print("Längd:", len(minLista))
print("Var finns första tvåan: ", minLista.index(2))
print("vad finns på plats 2: ", minLista[2])

#Kontrollera om visst värde finns i listan
if 10 in minLista:
	print("woho")
else:
	print("ingen tia")
	
if 10 not in minLista:
	print("nope, fortfarande ingen tia")
#använda som stack - använd append och pop() <-- utan position. 
#använda som kö - använd append och popleft

#Slicing - hämta ut en del av en lista.
print("En slicad lista: ",minLista[1:3])

#Man kan också skapa en ordnad lista meed hjälp av range. Man får då först ange spannet och sen skicka in det i list()
print("Lista skapad med range:", list(range(1,10)))

#funkar också med loopar
for i in range(1,10):
	print(i**2)





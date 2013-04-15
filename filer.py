'''
Öppnar en fil. Kan ges extra parametrar

t.ex
open("lista.txt","r+") öppnar för läsa och skriva
r = läsa <- default
r+ = både läsa och skriva
w = bara skriva (skriver över redan existerande fil)
a = lägg till i slutet på existerande fil
'''
minLista = open("lista.txt")

print("skriv ut filens innehåll")
for rad in minLista:
	print(rad)

print("skriver ut första posten igen")
#Nollställer listans pekare
minLista.seek(0)
print(minLista.readline())

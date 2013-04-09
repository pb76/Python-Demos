##Dictionaries
#Som en array, men med nyckelord

minKatalog = {"Namn":"Ulf"}
minKatalog["Stad"]="Vanersborg"
minKatalog["Number"]="0520275059"
minKatalog["Age"]=39

print(minKatalog)
print(minKatalog["Namn"])

#Ger oss nycklarna i dictionarien
print(minKatalog.keys())

#ger oss alla enheterna i dictionarien
print(minKatalog.items())

#skapa en lista av ovanstående
print(list(minKatalog.items()))

#loopa över alla nycklar
for s in minKatalog.keys():
	print(s,": ",minKatalog[s])
	
#annat sätt att skapa
minAndraKatalog = dict([("Namn","Oskar"),("Stad","Lund"),("Nummer","0702347898")])

for s in minAndraKatalog.keys():
	print(s,": ",minAndraKatalog[s])
	
#Ytterliggare sätt
nycklar = ["namn","stad","nummer"]
fakta = ["Lisa","Malmö","040400851"]

kat3 = {n:f for n,f in zip(nycklar,fakta)} #bygger upp dictionarien position för position m.h.a zip. 
print(kat3)
	

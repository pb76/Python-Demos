'''
Ta en titt på dictionaries.py för att se hur python arbetar med dictionaries.

Grejen är att pythons directory-struktur ÄR json. Så raden

{'namn': 'Lisa', 'stad': 'Malmö', 'nummer': '040400851'}

som vi får i den filen, kan läsas in och arbetas med som en json-struktur. Dock måste vi tänka på att single-quotes inte fungerar, utan man måste använda sig av double-quotes, dvs ". I namnlista.json har jag gjort en enkel search and replace för att få rätt på det.
'''

import json

#öppna filen

minFil = open("namnlista.json")

#nästa steg är att läsa in filen som en json-struktur, dvs ett directory

minLista = json.load(minFil)

#Märk väl att det är ett kommando som faller under json-biblioteket. Därav json.load

for s in minLista.keys():
	print(s,": ",minLista[s])
	
'''
Jag kan förvandla mitt dictionary till en sträng med hjälp av dumps-kommandot
'''

minPerson = dict([("Namn","Oskar"),("Stad","Lund"),("Nummer","0702347898")])
print("Skriv ut variabel-typen hos minPerson")
print(type(minPerson))

minPerson_String = json.dumps(minPerson)
print("Skriv ut variabel-typen hos minPerson_String")
print(type(minPerson_String))

'''
På motsvarande sätt kan jag göra när jag vill skicka det till en fil
'''
minLista = open("annanNamnLista.json","w")  #öppna filen
json.dump(minPerson, minLista)         #dumpa minPerson till minLista
minLista.close()					   #stäng filen

'''
Frågan nu är då om jag inte kunde lägga in oskar och hans värden i samma fil som Lisa?

Jo, det skulle gå, MEN då måste jag ändra strukturen lite. Grejen är den att det måste vara ett JSON-objekt (vad jag förstått), och nu blir det två på raken. Det man skulle kunna göra är att man gör en directory av directories helt enkelt, och på det sättet lägga till fler namn i filen
'''

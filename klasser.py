'''i den här filen tänkte jag visa på hur man skapar en klass i python
Efter klass-beskrivningen finns det en instantiering som jag använder för att visa lite på hur egenskaper fungerar i python. Tråkigt, men ack så viktigt. 
'''

class enPerson(object):
	#Namnet på klassen är enPerson. Den ärver egenskaper av en generell object-klass.
	
	def __init__(self):
		#det här är konstruktorn. Den körs var gång ett nytt objekt skapas av klassen
		self.__namn = "Sine Nomine"   #Det här är en egenskap. Dubbla underscores = privat.
	
	#Egenskaper är variabler som kan nås utifrån. Det gör man med getters och setters i kombination med nedanstående kommandon.
	
	@property
	def namn(self):
		print("getter")
		return self.__namn
	
	@namn.setter
	def namn(self,namn):
		print("Nu sätts variablen __namn")
		self.__namn = namn
		
	#den här metoden är till för en liten demonstration
	def printNamn(self):
		print(self.__namn)
		


#Nu ska vi instantiera ett objekt av klassen enPerson

jag = enPerson()  #nu körs __init__-metoden och ett objekt skapas

'''
Det vi nu kommer att titta på är något som kan vara lite klurigt att förstå, och det är det här med privata egenskaper. I enPerson-klassen har vi egenskapen __namn. Vi når den egenskapen med hjälp av objektnamn.namn. Se nedan
'''

jag.namn = "Astrid"

print(jag.namn)
#Märk väl att det har lagts in print-rader i gettern och settern, så vi vet nu att dessa metoder körs.

#Vad händer då när vi försöker sätta __namn manuellt?
print("Försöker nå en privat variabel")
jag.__namn = "Oskar"
print(jag.namn)

'''
Det vi ser här är att även om det verkar som vi sätter __namn till något annat, så när vi försöker skriva ut egenskapen så skrivs det ursprungliga namnet ut

Om vi tittar på metoden printNamn så vet vi (i koden) att den skriver ut värdet på variablen __namn

'''
jag.printNamn()

#Vad händer då om vi försöker nå en variabel __namn direkt?

print(jag.__namn)

#Då får vi det värde vi satte till .__namn direkt tidigare. MEN, det verkar vara en ANNAN variabel, som inte går in och stör vår kod inne i klassen. Det blir därför riskfritt om vi råkar skriva fel namn


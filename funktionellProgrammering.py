''' 
Funktionell programmering bygger på samlingar (typ listor osv) som har en s.k iterator.
Mycket av koden här är hämtad från http://docs.python.org/3.4/howto/functional.html
'''
lista = [1,2,3,4]

minIterator = iter(lista)

# I de här raderna så flyttar vi fram iteratorn ett steg och skriver ut värdet på den positionen

print(minIterator.__next__())
print(minIterator.__next__())
print(minIterator.__next__())

#Vanligare är att man t.ex använder sig av en for-loo

for i in iter(lista):
	print(i)
	
#Det här är ekvivalent med
for i in lista:
	print(i)
	
'''
Vi kan nu göra saker med de olika typer som innehåller iterators (listor, dictionaries). 

Exempelvis kan vi utföra saker på varje position, eller filtrera ut en delmängd av listan
'''

resultat = [x**x for x in lista]
print(resultat)

#Vill vi bara göra det på vissa delar kan vi skriva det så här

resultat2 = [x**x for x in lista if x < 4]
print(resultat2)

'''
De två ovanstående exemplena arbetar på en redan existerande lista och skapar en ny lista utifrån den. Den är också statisk
Ett alternativ är en så kallad generator expression, där bara det som behövs räknas ut räknas ut.
När koden nedan körs så skrivs bara texten <generator object <genexpre> at...> ut. Det innebär att man måste använda en iterator eller liknande för att få ut information från den.
'''
genLista = (i**i for i in lista)
print(genLista)

#Däremot, nu skriver den ut resultatet, eftersom vi itererar över samlingen. En fördel med det här är att vi kan göra en oändlig lista och bara räkna ut det som behövs när det behövs.
for i in genLista:
	print(i)

'''
Generatorer är funktioner som skriver iterator-samlingar dynamiskt. Skillnaden mot en vanlig funktion är att vi inte har en return-sats, utan en yield-sats. 
När funktionen kommer fram till yield-satsen så avbryts funktionen (precis som vid en return), MEN funktionen nollställs inte, utan nästa gång den anropas så kör den ifrån där den slutade.

Funktionen generateBinary skapar en generator som, när den anropas, slår upp svarsvärdet för där den är just nu och plockar 2^iteratorns värde. 
'''

def generateBinary(n):
	for i in range(n):
		ii = 2**i
		yield ii
		
#minaHeltal blir här generatorn. Just nu vet den inte vad den har för värde, utan den har bara potentialen att räkna ut värden
minaHeltal = generateBinary(8)
#Resultatet av print-satsen blir ointressant. Säger bara <generator object osv>. minaHeltal vet inte vilka värden den har
print(minaHeltal)
#Nu anropas iteratorn i minaHeltal, och för varje steg så räknas rätt resultat ut. 
for i in minaHeltal:
	print(i)
	
'''
Istället för for-loopar som ovan kan man förenkla det ännu mer genom att använda metoderna Map och Filter.
'''
#Enkel funktion som tar indata och returnerar 2 upphöjt till indatan
def binary(x):
	return 2**x
	
#skapa en lista av talen 1-9
heltal = list(range(1,10))

#skapa ett map-objekt där funktionen binary körs på listan heltal
binarTal = map(binary,heltal)

#skriv ut en lista baserat på map-objektet binartal
print(list(binarTal))

#alternativ
print(list(map(lambda x:2**x,heltal)))
print(list(map(lambda x:2**x,range(1,10)))) #<--- här görs alla stegen på en rad (inkl. definierar funktionen tack vare lambda-funktionen

##Metoden Filter fungerar på ett liknande sätt, men returnerar en lista som uppfyller vissa vilkor. Exempelvis alla tal som är mindre än 5

def checkLessThan5(x):
	if x<5:
		return True
	else:
		return False
		
#ovanstående metod kan för övrigt komprimeras ganska rejält på följande sätt
def checkLessThan5Compressed(x):
	return x<5
	
#Så, om vi har en lista som tidigare

heltal2 = list(range(1,10))
#Nästa steg är att köra kontroll-funktionen på samma heltal2 och spara det i en ny lista
rensadLista = list(filter(checkLessThan5Compressed,heltal2))
print(rensadLista)

#komprimerad version med lambda-funktion

rensadLista2 = list(filter(lambda x:x<5, range(1,10)))

#För att förstå ovanstående rad, gå innifrån och ut: Det skapas en lista från 1 till 9, den körs genom filtret som kollar efter värden mindre än 5, och lagrar det i en ny lista

print(rensadLista2)



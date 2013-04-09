
###Funktioner

def minFunktion(a,b):
	#c=3
	return a+b
	
c = minFunktion(2,3)
print(c)

'''
Man kan göra ganska mycket med Pythons funktioner (inklusive lagra dem i listor, och då blir det riktigt klurigt att hålla reda på). Ett enkelt exempel är dock på sin plats. Vi ska här skicka in en funktion i en annan funktion
'''

def addera(x,y):
	return x+y
	
def subtrahera(x,y):
	return x-y
	
def multiplicera(x,y):
	return x*y
	
def dividera(x,y):
	return x/y
	

'''Nu har vi fyra metoder att använda oss av. Men, vi vet inte vilken av metoderna som ska användas när sen en uträkning görs. Då kan vi lagra funktionen i en variabel, och sen skicka in den variabeln i en annan metod.
Den metoden kan då se ut så här:
'''
def calculate (x,y,method):
	result = method(x,y)
	return result
	
currentMethod = addera
svar = calculate(2,3,currentMethod)
print("Metod:", currentMethod.__name__)
print("Svar: ", svar)

##Ändrar till multiplikation
currentMethod = multiplicera
svar = calculate(2,3,currentMethod)  #märk väl att den här raden är identisk!!
print("Metod:", currentMethod.__name__)
print("Svar: ", svar)








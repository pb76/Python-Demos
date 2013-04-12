'''
Ibland vill man göra "känsliga" operationer, där det finns en risk för fel. Ett vanligt exempel är att man råkar vilja dividera med 0 (något som är odefinierat i matematiken). I det läget kan man antingen göra en kontroll innan man gör divisionen (vilket är kanske det enklaste i division-med-0-varianten), eller så kan man FÖRSÖKA utföra ett kommando, men låta programmet reagera på fel. På det sättet förhindrar man att programmet kraschar och istället kan programmet hantera felet.

Andra sammanhang kan vara om man ska öppna en fil (som man inte vet om den finns), öppna en webb-anslutning osv.
'''

a = 10
b = 5

c = a/b

print(c)

#så långt är allt ok, men om vi vill vara säkra på att allt blir rätt kan vi istället FÖRSÖKA göra divisionen med hjälp av kommandot TRY

b = 0

try:
	c = a/b
except:
	print("Kunde inte göra division. Sätter c till 1")
	c=1
	

print(c)

#och vi avslutar med felmeddelandet om vi inte gör en try. När hela den här filens kod körs avslutas det med ett felmeddelande: DivisionBy Zero

c = a/b
print(c)
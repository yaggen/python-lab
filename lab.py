def diagnose():
	#Ställ första frågan
	print("Är du täppt i näsan? (j/n): ")
	tappt = input().lower() #Konvertera allt användaren skriver in till lowercase för att minska felmarginalen
	if tappt == 'j' or tappt == 'ja': #Om användaren är täppt, ta reda på om den även ha feber
		print("Har du feber? (j/n): ")
		feber = input().lower()
		if feber == 'j' or feber == 'ja':
			print("Du är förkyld. Stanna hemma och ta det lugnt!") # Utfall ifall användaren har feber
		elif feber == 'n' or feber == 'nej': # Utfall om användaren inte har feber
			print("Du har förmodligen hösnuva. Uppsök apotek!")
		# Skriver användaren något annat än j/ja eller n/nej får den börja om.
		else:
			print("Svara ja eller nej på frågorna!")  
			diagnose()
	elif tappt == 'n' or tappt == 'nej':
		print("Du är frisk. Gå och jobba eller studera!") #Är användaren inte ens täppt så avslutar vi här.
	else: 
		print("Svara ja eller nej på frågorna!")
		diagnose()




def sayHello():
	namn = input("Vad är ditt namn?: ")
	print("Hej", namn)

def printRecipe():

	antal = input("Hur många satser sockerkaka vill du baka?: ")
	antal = int(antal)

	#Lagra receptet i en dictionary för att enkelt kunna multiplicera det med antal satser användaren önskar baka.
	recipe = {
	'st ägg' : 3,
	'dl strösocker' : 3,
	'tsk vaniljsocker' : 2,
	'tsk bakpulver' : 2,
	'dl mjöl' : 3,
	'g smör' : 75,
	'dl vatten' : 1}

	print("Recept för " + str(antal) + " sockerkakor")

	# För alla värden och nycklar i min dictionary, skriv ut värdet och multiplicera nyckeln med antal satser.
	for value, key in recipe.items():
		print(key * antal, value)

# Simpel meny som ger tre alternativ och ett fjärde att avsluta programmet, variabeln choice bestäms alltid
# av användaren men "får" bara innehålla 1,2,3 eller 0.
def menu():	
	print('\n')
	print('\n')
	print("#################### H U V U D M E N Y ######################")
	print("#   Välj en siffra mellan 1-4 beroende på vad du vill göra: #")
	print("# 1. Hälsa                                                  #")
	print("# 2. Få recept på sockerkaka                                #")
	print("# 3. Ställa en sjukdomsdiagnos                              #")
	print("# 0. Avsluta programmet                                     #")
	print("#################### H U V U D M E N Y ######################")
	print('\n')
	print('\n')


	choice = int(input("Välj ett alternativ (1-3):"))

	if choice == 1:
		sayHello() #Kör/kalla på funktionen som matchar valet i menyn
		menu()
	elif choice == 2:
		printRecipe()
		menu()
	elif choice == 3:
		diagnose()
		menu()
	elif choice == 0:
		exit()
	else:
		print("Vänligen välj ett alternativ mellan 1-3!")
		menu()
	
#Kalla på / kör funktionen menu vid uppstart av programmet
menu()
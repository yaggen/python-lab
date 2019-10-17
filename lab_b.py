#Definiera listor för alla betyg med studenter
vg_students = []
g_students = []
u_students = []

#En variabelstyrd meny istället för "while True:"
i = 0

while i == 0:
	student = input("Ange studentens namn ('klar' för att gå vidare): ").capitalize()
	if student.lower() == "klar": #Om "klar" skrivs in (oavsett format med stora/små bokstäver) - Skriv ut listor och avsluta program
		print('\n' * 3)
		print("=" * 32)
		print("Studenter med betyget U:")
		print(*u_students, sep = '\n')
		print("=" * 32)
		print("Studenter med betyget G:")
		print(*g_students, sep = '\n')
		print("=" * 32)
		print("Studenter med betyget VG:")
		print(*vg_students, sep = "\n")
		print("=" * 32)
		i = 1
	else: #Så länge "klar" inte skrivs in, börja ta betyg på studenterna och lägg till i respektive lista.
		betyg = input("Ange betyg: ")
		if betyg.upper() == "VG":
			vg_students.append(student)
		elif betyg.upper() == "G":
			g_students.append(student)
		elif betyg.upper() == "U":
			u_students.append(student)

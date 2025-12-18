
N = int(input("donner un nombre: "))

solutions = []

# kanjrbu ge3 ayem
for J in range(1, 32):      
    for M in range(1, 13):  
        if 31 * J + 12 * M == N:
            solutions.append((J, M))

# ktbu les resultat
if solutions:
    print("Date de nessance:")
    for day, month in solutions:
        print(f"Day: {day}, Month: {month}")
else:
    print("pas de date valide.")

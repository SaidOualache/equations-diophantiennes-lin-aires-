# Programme : Résolution d’une équation diophantienne ax + by = c
# ki affichi les étapes dyal Euclide w Euclide étendu

def demander_entiers():
    # ntlbo mn user idir 2 nombres positifs et A > B wichof les conditions wach s7a7
    while True:
        try:
            A = int(input("Entrer le premier nombre (A) : "))
            B = int(input("Entrer le second nombre (B) : "))
        except ValueError:
            print("Entrées invalides")
            continue
        if A <= 0 or B <= 0:
            print("A et B doivent être positifs")
            continue
        if A < B:
            print("A doit être >= B")
            continue
        return A, B

def demander_c():
    while True:
        try:
            return int(input("Entrer la valeur de c (pour ax + by = c) : "))
        except ValueError:
            print("⛔ Entrée invalide")

def euclide_etendu_explications(a, b):
    print(f"\n--- Étapes de l'algorithme d'Euclide pour {a} et {b} ---")
    A, B = a, b
    divs = []
    while B != 0:
        q, r = A // B, A % B
        print(f"{A} = {B} × {q} + {r}")
        divs.append((A, B, q, r))
        A, B = B, r
    d = A
    print(f"➡️ PGCD({a}, {b}) = {d}\n")

    print("--- Substitutions pour Euclide Étendu ---")
    # kanktboh sous forme r = A - B×q
    eq = {r: f"{A1} - {B1}×{q}" for A1, B1, q, r in divs if r != 0}
    last_r = list(eq.keys())[-1]
    expr = eq[last_r]
    print(f"{last_r} = {expr}")

    for key in reversed(list(eq.keys())[:-1]):
        if str(key) in expr:   # <-- conversion en string
            print(f"=> Remplaçons {key} par ({eq[key]})")
            expr = expr.replace(str(key), f"({eq[key]})")
            print(f"{last_r} = {expr}")


    # Résultat dyal Euclide étendu
    def extended(a, b):
        if b == 0: return (a, 1, 0)
        d, x1, y1 = extended(b, a % b)
        return (d, y1, x1 - (a // b) * y1)

    d, x0, y0 = extended(a, b)
    print(f"\n➡️ Résultat final: {a}*({x0}) + {b}*({y0}) = {d}")
    return d, x0, y0

def resoudre_diophantienne(a, b, c):
    print(f"\n📘 On résout: {a}x + {b}y = {c}")
    d, x0, y0 = euclide_etendu_explications(a, b)

    print("\n--- Vérification si d | c ---")
    if c % d != 0:
        print(f"❌ d = {d} ne divise pas c = {c} → aucune solution entière.")
        return
    print(f"✅ d = {d} divise c = {c}, donc il existe des solutions entières.")
    mult = c // d
    xp, yp = x0 * mult, y0 * mult
    alpha, beta = b // d, -a // d
    print(f"\nSolution particulière: x = {xp}, y = {yp}")
    print(f"Forme générale: x = {xp} + {alpha}k,  y = {yp} + {beta}k  (k ∈ ℤ)")

def main():
    print("=== Équation diophantienne linéaire ax + by = c ===")
    A, B = demander_entiers()
    C = demander_c()
    resoudre_diophantienne(A, B, C)

if __name__ == "__main__":
    main()












# $$$$$$\            $$\       $$\        $$$$$$\                      $$\                     $$\                 
# $$  __$$\           \__|      $$ |      $$  __$$\                     $$ |                    $$ |                
# $$ /  \__| $$$$$$\  $$\  $$$$$$$ |      $$ /  $$ |$$\   $$\  $$$$$$\  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\  
# \$$$$$$\   \____$$\ $$ |$$  __$$ |      $$ |  $$ |$$ |  $$ | \____$$\ $$ | \____$$\ $$  _____|$$  __$$\ $$  __$$\ 
#  \____$$\  $$$$$$$ |$$ |$$ /  $$ |      $$ |  $$ |$$ |  $$ | $$$$$$$ |$$ | $$$$$$$ |$$ /      $$ |  $$ |$$$$$$$$ |
# $$\   $$ |$$  __$$ |$$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |$$  __$$ |$$ |      $$ |  $$ |$$   ____|
# \$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$ |       $$$$$$  |\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ 
#  \______/  \_______|\__| \_______|       \______/  \______/  \_______|\__| \_______| \_______|\__|  \__| \_______|
#                                                                                                                  
#                                                                                                                  
#             
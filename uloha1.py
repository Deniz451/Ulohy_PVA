# Funkce, hledajici stranu, na ktere lezi bod
def najdi_stranu_bodu(souradnice_bodu, hledana_hodnota):
    try:
        index = souradnice_bodu.index(hledana_hodnota)
        poradi = index + 1  # Přidáváme 1, protože indexy jsou od 0
        souradnice = None

        if index == 0:
            souradnice = 'x'
        elif index == 1:
            souradnice = 'y'
        elif index == 2:
            souradnice = 'z'

        return souradnice
    except ValueError:
        return None, None  # Hodnota nebyla nalezena v tuplu
    
# Input místnosti
a = input("Rozměr hrany pokoje: ")

# Input bodů
bod1 = input("#1: ")
bod2 = input("#2: ")


# Vradit spatny inputy místnosti
try:
    a = int(a)
except:
    print("Nesprávný vstup")
    exit()

if a <= 0:
    print("Nesprávný vstup")
    exit()

# Vradit neciselny inputy
# format() převede float na string split() je rozdělí, map() je převede zpátky na float a tuple() je převede na tuple do jendý proměnný
try:
    bod1 = tuple(map(float, format(bod1).split()))
    bod2 = tuple(map(float, format(bod2).split()))
except:
    print("Nesprávný vstup")
    exit()

# Vyradit inputy lezici mimo steny
# Vyradi inputy, ktere jsou mensi nez nula nebo vetsi nez hrana pokoje
if all(coord >= 0 for coord in bod1) and all(coord <= a for coord in bod1) and \
    all(coord >= 0 for coord in bod2) and all(coord <= a for coord in bod2):

    print("")
else:
    print("Nesprávný vstup")
    exit()

# Vyradi inputy, ne lezi na stene nebo ktere lezi na hrane
if sum(1 for coord in bod1 if coord == 0) == 1 or sum(1 for coord in bod1 if coord == a) == 1 and \
    sum(1 for coord in bod2 if coord == 0) == 1 or sum(1 for coord in bod2 if coord == a) == 1:

    # Zavola funkci, ktera vrati na ktere strane lezi bod
    strana_bod1 = najdi_stranu_bodu(bod1, 0) or najdi_stranu_bodu(bod1, a)
    strana_bod2 = najdi_stranu_bodu(bod2, 0) or najdi_stranu_bodu(bod2, a)

    # Vypise stranu, na ktere se body nachazeji
    print(f"V tuplu bod1 leží na straně: {strana_bod1}.")
    print(f"V tuplu bod1 leží na straně: {strana_bod2}.")
else:
    print("Nesprávný vstup")
    exit()

# Vyradi inputy prilis blizko hrane


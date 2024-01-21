# Funkce, hledajici stranu, na ktere lezi bod
def najdi_stranu_bodu(souradnice_bodu, hledana_hodnota1,  hledana_hodnota2):
    # Nejdriv hleda 0 v tuplu
    try:
        index = souradnice_bodu.index(hledana_hodnota1)
        poradi = index + 1  # Přidáváme 1, protože indexy jsou od 0
        souradnice = None

        if index == 0:
            souradnice = 'x'
        elif index == 1:
            souradnice = 'y'
        elif index == 2:
            souradnice = 'z'

        return poradi, souradnice
    
    # Pokud nenajde nulu snayi se najit hodnotu a
    except ValueError:
        index = souradnice_bodu.index(hledana_hodnota2)
        poradi = index + 1  # Přidáváme 1, protože indexy jsou od 0
        souradnice = None

        if index == 0:
            souradnice = 'x'
        elif index == 1:
            souradnice = 'y'
        elif index == 2:
            souradnice = 'z'

        return poradi, souradnice
    
# Input místnosti
a = input("Rozměr hrany pokoje: ")

# Input bodů
bod1 = input("#1: ")
bod2 = input("#2: ")


# Vradit spatny inputy místnosti
try:
    a = int(a)
except:
    print("Nesprávný vstup - Nečíselné zadání rozměru")
    exit()

if a <= 0:
    print("Nesprávný vstup - Záporné hodnota rozměru")
    exit()

# Vradit neciselny inputy
# format() převede float na string split() je rozdělí, map() je převede zpátky na float a tuple() je převede na tuple do jendý proměnný
try:
    bod1 = tuple(map(float, format(bod1).split()))
    bod2 = tuple(map(float, format(bod2).split()))
except:
    print("Nesprávný vstup - Nečíselné zadání hodnot")
    exit()

# Vyradit inputy lezici mimo steny
# Vyradi inputy, ktere jsou mensi nez nula nebo vetsi nez hrana pokoje
if all(coord >= 0 for coord in bod1) and all(coord <= a for coord in bod1) and \
    all(coord >= 0 for coord in bod2) and all(coord <= a for coord in bod2):

    print("")
else:
    print("Nesprávný vstup - Bod leží mimo stěny/strop/podlahu")
    exit()

# Vyradi inputy, ne lezi na stene nebo ktere lezi na hrane
if sum(1 for coord in bod1 if coord == 0) == 1 or sum(1 for coord in bod1 if coord == a) == 1 and \
    sum(1 for coord in bod2 if coord == 0) == 1 or sum(1 for coord in bod2 if coord == a) == 1:

    # Zavola funkci, ktera vrati na ktere strane lezi bod
    poradi_bod1, strana_bod1 = najdi_stranu_bodu(bod1, 0, a)
    poradi_bod2, strana_bod2 = najdi_stranu_bodu(bod2, 0, a)

    # Vyradi spatne zadane souradnice
    if poradi_bod1 == None and strana_bod1 == None or poradi_bod2 == None and strana_bod2 == None:
        print("Nesprávný vstup - Bod leží mimo stěny/strop/podlahu")
        exit()

    # Vypise stranu, na ktere se body nachazeji
    print(f"V tuplu bod1 leží na straně: {strana_bod1} a je na pozici {poradi_bod1}")
    print(f"V tuplu bod1 leží na straně: {strana_bod2} a je na pozici {poradi_bod2}")

    zbyva_bod1 = [coord for i, coord in enumerate(bod1) if i != poradi_bod1 - 1]
    zbyva_bod2 = [coord for i, coord in enumerate(bod2) if i != poradi_bod2 - 1]

    if all(coord <= a - 20 for coord in zbyva_bod1) and all(coord <= a - 20 for coord in zbyva_bod2):
        print("Všechny podmínky jsou splněny.")
    else:
        print("Nesprávný vstup - Bod je moc blízko hrany pokoje")
        exit()
        
else:
    print("Nesprávný vstup")
    exit()


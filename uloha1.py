
import math

# Hleda nejkratsi cestu na potrubi pro body na protilehlych stranach
def hleda_nejkratsi_cestu_potrubi():
    nejkratsi_cesta = []
    nejkratsi_cesta.append(bod1[1] + a + bod2[1] + abs(bod2[0] - bod1[0]))
    nejkratsi_cesta.append((a - bod1[1]) + a + (a - bod2[1]) + abs(bod2[0] - bod1[0]))
    nejkratsi_cesta.append(bod1[0] + a + bod2[0] + abs(bod2[1] - bod1[1]))
    nejkratsi_cesta.append((a - bod1[0]) + a + (a - bod2[0]) + abs(bod2[1] - bod1[1]))

    nejkratsi_cesta = min(nejkratsi_cesta)
    return nejkratsi_cesta

# Hleda nejkratsi cestu na hadice pro body na vedlejsich stranach
def hleda_nejkratsi_cestu_hadice_vedlejsi():
    nejkratsi_cesta = []

    return nejkratsi_cesta

# Hleda nejkratsi cestu na hadice pro body na protilehlych stranach
def hleda_nejkratsi_cestu_hadice_naproti():
    nejkratsi_cesta = []
    nejkratsi_cesta.append(math.sqrt((bod1[1] + a + bod2[1])**2 + (abs(bod2[0] - bod1[0]))**2))
    nejkratsi_cesta.append(math.sqrt(((a - bod1[1]) + a + (a - bod2[1]))**2 + (abs(bod2[0] - bod1[0]))**2))
    nejkratsi_cesta.append(math.sqrt((bod1[0] + a + bod2[0])**2 + (abs(bod2[1] - bod1[1]))**2))
    nejkratsi_cesta.append(math.sqrt(((a - bod1[0]) + a + (a - bod2[0]))**2 + (abs(bod2[1] - bod1[1]))**2))

    nejkratsi_cesta = min(nejkratsi_cesta)
    return nejkratsi_cesta


# Funkce, hledajici stranu, na ktere lezi bod
def najdi_stranu_bodu(souradnice_bodu, hledana_hodnota1,  hledana_hodnota2):
    # Nejdriv hleda 0 v tuplu
    try:
        index = souradnice_bodu.index(hledana_hodnota1)
        poradi = index + 1  # Pridavame 1, protoze indexy jsou od 0
        souradnice = None

        if index == 0:
            souradnice = 'x'
        elif index == 1:
            souradnice = 'y'
        elif index == 2:
            souradnice = 'z'

        return poradi, souradnice
    
    # Pokud nenajde nulu snazi se najit hodnotu a
    except ValueError:
        index = souradnice_bodu.index(hledana_hodnota2)
        poradi = index + 1  # Pridavame 1, protoze indexy jsou od 0
        souradnice = None

        if index == 0:
            souradnice = 'x'
        elif index == 1:
            souradnice = 'y'
        elif index == 2:
            souradnice = 'z'

        return poradi, souradnice
    
# Input mistnosti
a = input("Rozměr hrany pokoje: ")

# Input bodu
bod1 = input("#1: ")
bod2 = input("#2: ")

#Kontrola spatnych inputu
# Vradit spatny inputy mistnosti
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

# Vyradi inputy, ktere nelezi na stene nebo ktere lezi na hrane
if sum(1 for coord in bod1 if coord == 0) == 1 or sum(1 for coord in bod1 if coord == a) == 1 and \
    sum(1 for coord in bod2 if coord == 0) == 1 or sum(1 for coord in bod2 if coord == a) == 1:

    # Zavola funkci, ktera vrati na ktere strane lezi bod
    poradi_bod1, strana_bod1 = najdi_stranu_bodu(bod1, 0, a)
    poradi_bod2, strana_bod2 = najdi_stranu_bodu(bod2, 0, a)

    # Vyradi spatne zadane souradnice
    if poradi_bod1 == None and strana_bod1 == None or poradi_bod2 == None and strana_bod2 == None:
        print("Nesprávný vstup - Bod leží mimo stěny/strop/podlahu")
        exit()

    zbyva_bod1 = [coord for i, coord in enumerate(bod1) if i != poradi_bod1 - 1]
    zbyva_bod2 = [coord for i, coord in enumerate(bod2) if i != poradi_bod2 - 1]

    # Kontroluje, zda jsou body aspon 20cm od hrany
    if all(coord <= a - 20 for coord in zbyva_bod1) and all(coord <= a - 20 for coord in zbyva_bod2) and \
        all(coord >= 20 for coord in zbyva_bod1) and all(coord >= 20 for coord in zbyva_bod2):

        print("Všechny podmínky jsou splněny")
    else:
        print("Nesprávný vstup - Bod je moc blízko hrany pokoje")
        exit()
        
else:
    print("Nesprávný vstup - Bod leží mimo stěny/strop/podlahu")
    exit()

# Hledani nejkratsi cesty potrubi
# Podminka, ktera zjistuje, zda jsou body na sousednich stranach
# Pokud jsou na vedlejsich stranach tak se odectou souradnice bodu a sectou se jejich abs
if strana_bod1 != strana_bod2:
    nejkratsi_cesta = tuple(abs(x - y) for x, y in zip(bod1, bod2))

    sum_nejkratsi_cesta = sum(nejkratsi_cesta)

    print(f"Nejkratší cesta potrubí je:  {sum_nejkratsi_cesta} \nNejkratší cesta hadice je: {hleda_nejkratsi_cestu_hadice_vedlejsi()}")

# Pokud jsou body na stejne strane vypocita delku
elif strana_bod1 == strana_bod2 and bod1[poradi_bod1 - 1] == bod2[poradi_bod2 - 1]:
    nejkratsi_cesta = tuple(abs(x - y) for x, y in zip(bod1, bod2))

    sum_nejkratsi_cesta = sum(nejkratsi_cesta)

    print(f"Nejkratší cesta potrubí je:  {sum_nejkratsi_cesta} \nNejkratší cesta hadice je: {sum_nejkratsi_cesta}")
    
# Pokud jsou na stranach protilehlych zavolaji se podminky na vypocitani cesty potrubi a hadice
elif strana_bod1 == strana_bod2:
    print(f"Nejkratší cesta potrubí je:  {hleda_nejkratsi_cestu_potrubi()} \nNejkratší cesta hadice je: {hleda_nejkratsi_cestu_hadice_naproti()}")
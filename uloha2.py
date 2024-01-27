from decimal import Decimal

def find_middle_point(x1, y1, x2, y2, x3, y3):
    x_values = [x1, x2, x3]
    y_values = [y1, y2, y3]

    x_values.sort()
    y_values.sort()

    middle_x, middle_y = x_values[1], y_values[1]

    if (middle_x, middle_y) == (x1, y1):
        return "A"
    elif (middle_x, middle_y) == (x2, y2):
        return "B"
    elif (middle_x, middle_y) == (x3, y3):
        return "C"
    else:
        return "Unknown"

def are_points_merge(x1, y1, x2, y2, x3, y3):

    if x1 == x2 and y1 == y2 or x1 == x3 and y1 == y3 or x2 == x3 and y2 == y3:
        return True
    else:
        return False

def determinant(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2

def are_points_collinear(x1, y1, x2, y2, x3, y3):
    return determinant(x1, y1, x2, y2, x3, y3) == 0


# Bereme input
try:
    x1, y1 = map(float, input("Bod A: ").split())
    x2, y2 = map(float, input("Bod B: ").split())
    x3, y3 = map(float, input("Bod C: ").split())
# Dáváme pryč nečíselný input
except:
    print("\nNespravny vstup.")
    exit()


# Voláme funkce, který kotrolujou body
# Kontroluje, zda body splývají
if are_points_merge(x1, y1, x2, y2, x3, y3):
    print("\nNektere body splyvaji.")

# Kontroluje, zda body leží na jedné přímce
elif are_points_collinear(x1, y1, x2, y2, x3, y3):
    print("\nBody lezi na jedne primce.")
    # Hledáme prostřední bod
    middle_point = find_middle_point(x1, y1, x2, y2, x3, y3)
    print(f"Prostřední je bod {middle_point}.")

# Body neleží na stejné přímce
else:
    print("\nBody nelezi na jedne primce.")

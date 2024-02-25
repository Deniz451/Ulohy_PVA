import sys
from itertools import combinations

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

planes = []

for line_num, line in enumerate(sys.stdin, start=1):  
    if not line.strip():
        break

    parts = line.strip().split(':')
    if len(parts) != 2:
        print("Nespravny vstup.")
        sys.exit()

    coordinates, plane_name = parts

    if len(coordinates.split(',')) != 2:
        print("Nespravny vstup.")
        sys.exit()

    try:
        x, y = map(float, coordinates.split(','))
    except ValueError:
        print("Nespravny vstup.")
        sys.exit()

    planes.append((plane_name.strip(), (x, y)))  

if len(planes) < 2:
    print("Nespravny vstup.")
    sys.exit()

closest_distance = float('inf')
closest_pairs = []
for pair in combinations(planes, 2):
    plane1, plane2 = pair
    dist = distance(plane1[1], plane2[1])
    if dist < closest_distance:
        closest_distance = dist
        closest_pairs = [pair]
    elif dist == closest_distance:
        closest_pairs.append(pair)

print(f"Vzdalenost nejblizsich letadel: {closest_distance:.6f}")

if closest_pairs:
    print(f"Nalezenych dvojic: {len(closest_pairs)}")
    print("Planes:")
    for plane1, plane2 in closest_pairs:
        print(f"{plane1[0]} - {plane2[0]}")
else:
    print("No pairs of planes found with the same shortest distance.")

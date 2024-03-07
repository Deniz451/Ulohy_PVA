file_name = input("Zadejte název vstupního souboru: ")

try:
    with open(file_name, 'r') as file:
        obsah = file.read()

    shelves = {}
    shopping_list = []

    lines = obsah.split('\n')

    is_shopping_list = False

    for line in lines:
        line = line.strip()

        if not line:
            is_shopping_list = True
            continue

        if is_shopping_list:
            shopping_list.append(line)
        else:
            if line.startswith("#"):
                current_shelf = int(line[1:])
                shelves[current_shelf] = []
            else:
                shelves[current_shelf].append(line)

    optimized_shopping_list = []

    for shelf, shelf_items in shelves.items():
        for shelf_item in shelf_items:
            for item in shopping_list:
                if item in shelf_item or item.lower() in shelf_item.lower():
                    optimized_shopping_list.append(f"{item} -> #{shelf} {shelf_item}")
                    shopping_list.remove(item)
                    break

    for item in shopping_list:
        optimized_shopping_list.append(f"{item} -> N/A")

    print("Optimalizovaný nákupní seznam:")
    for index, item in enumerate(optimized_shopping_list):
        print(f"{index}. {item}")

except FileNotFoundError:
    print(f"Soubor '{file_name}' nebyl nalezen.")
except Exception as e:
    print(f"Došlo k chybě: {e}")
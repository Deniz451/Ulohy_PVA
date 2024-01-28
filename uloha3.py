def is_palindrome(num_str):
    return num_str == num_str[::-1]

def nextPalindrome(from_num, radix, next_palindrome):
    # Ověření platnosti číselné soustavy
    if radix < 2 or radix > 36:
        return 0  # Neplatná číselná soustava

    # Převod from_num do desítkové soustavy
    try:
        from_num_decimal = int(str(from_num), radix)
    except ValueError:
        return 0  # Chyba při převodu do desítkové soustavy

    # Hledání nejbližšího většího palindromu
    while True:
        from_num_decimal += 1
        next_palindrome_str = str(format(from_num_decimal, f'0{len(str(from_num))}d'))

        if is_palindrome(next_palindrome_str):
            try:
                next_palindrome[0] = int(next_palindrome_str, 10)
            except ValueError:
                return 0  # Chyba při převodu zpět do zadané soustavy

            return 1  # Úspěch

        # Ověření, zda se nevejde do rozsahu unsigned long long
        if from_num_decimal > 2**64 - 1:
            return 0  # Nebylo možné najít větší palindrom

# Příklad použití funkce
from_num = 123
radix = 20
next_palindrome = [0]

result = nextPalindrome(from_num, radix, next_palindrome)

if result:
    print(f"Next palindrome greater than {from_num} in radix {radix}: {next_palindrome[0]}")
else:
    print("Invalid radix or unable to find a palindrome greater than from_num.")

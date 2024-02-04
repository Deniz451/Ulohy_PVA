def is_palindrome(num_str):
    return num_str == num_str[::-1]

def convert_to_decimal(num_str, radix):
    try:
        return int(num_str, radix)
    except ValueError:
        return None

def convert_from_decimal(num, radix):
    return format(num, f'0{len(str(num))}d')

def nextPalindrome(from_num, radix, next_palindrome):
    if radix < 2 or radix > 36:
        return 0

    from_num_decimal = convert_to_decimal(str(from_num), radix)
    if from_num_decimal is None:
        return 0

    while True:
        from_num_decimal += 1
        next_palindrome_str = convert_from_decimal(from_num_decimal, 10)

        if is_palindrome(next_palindrome_str):
            next_palindrome[0] = convert_to_decimal(next_palindrome_str, 10)
            return 1


        if from_num_decimal > 2**64 - 1:
            return 0

from_num = 123
radix = 10
next_palindrome = [0]

result = nextPalindrome(from_num, radix, next_palindrome)

if result:
    print(f"Další palindrom od čísla {from_num} v soustavě {radix}: {next_palindrome[0]}")
else:
    print("Špatný input.")

def calculate_interval_sums(numbers):
    n = len(numbers)
    interval_sums = []

    for start in range(n):
        for end in range(start + 1, n + 1):
            interval_sum = sum(numbers[start:end])
            if end - start > 1:
                interval_sums.append(interval_sum)

    return interval_sums

def count_matching_sums(interval_sums):
    matching_count = 0

    for i in range(len(interval_sums)):
        current_sum = interval_sums[i]
        
        for j in range(i + 1, len(interval_sums)):
            if current_sum == interval_sums[j]:
                matching_count += 1

    return matching_count

def check_valid_inputs():
    if len(input_list) == 0:
        print("Vstupní posloupnost je prádná.")
        exit()
    elif len(input_list) > 2000:
        print("Vstupní posloupnost příliš dlouhá.")
        exit()


input_string = input("Zadejte posloupnost: ")

try:
    input_list = [int(num) for num in input_string.split()]
except:
    print("Hodnota na vstupu není platné celé číslo.")
    exit()

check_valid_inputs()

interval_sums = calculate_interval_sums(input_list)
matches = count_matching_sums(interval_sums)

print("Nalezeno", matches, "dvojic.")
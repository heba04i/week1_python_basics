def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers

def main():
    numbers = [5, 2, 8, 2, 3, 5, 1]
    result = remove_duplicates_and_sort(numbers)
    print(result)

main()
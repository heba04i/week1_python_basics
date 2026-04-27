def calculate_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)

    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]

    return minimum, maximum, average, median


def main():
    numbers = [10, 5, 8, 3, 7]
    result = calculate_stats(numbers)
    print("Min, Max, Avg, Median:", result)

main()
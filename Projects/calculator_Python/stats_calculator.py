def Calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return(sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    frequency={}
    for num in numbers:
        frequency[num]= frequency.get(num,0)+1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    return modes

def calculate_variance(numbers,mean):
    squared_diffs = [(x - mean)**2 for x in numbers]
    return sum(squared_diffs) / len(squared_diffs)

def calculate_standard_deviation(variance):
    return variance ** 0.5

def main():
    numbers = [1, 2, 2, 3, 4]
    mean = Calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_standard_deviation(variance)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
    
if __name__ == "__main__":
    main()
    
def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def main():
    numbers = [1, 2, 3, 4, 5]
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

main()
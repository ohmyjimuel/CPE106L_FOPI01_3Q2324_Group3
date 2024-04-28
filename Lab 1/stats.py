def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        return numbers[length // 2]

def mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_count = max(list(count.values()))
    return [num for num, freq in count.items() if freq == max_count]
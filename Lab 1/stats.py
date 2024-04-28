def mean(nums):
    total = sum(nums)
    mean_value = total / len(nums)
    return mean_value

def median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 0:
        mid = n // 2
        median_value = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median_value = sorted_nums[n // 2]
    return median_value

def mode(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

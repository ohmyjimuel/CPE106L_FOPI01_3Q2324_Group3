#function definition of mean value
def mean(nums):
    total = sum(nums)
    meanVal = total / len(nums)
    return meanVal

#function definition of median value
def median(nums):
    sortedNums = sorted(nums)
    n = len(sortedNums)
    if n % 2 == 0:
        mid = n // 2
        medianVal = (sortedNums[mid - 1] + sortedNums[mid]) / 2
    else:
        medianVal = sortedNums[n // 2]
    return medianVal

#function definition of mode value
def mode(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    maxCount = max(counts.values())
    modes = [num for num, count in counts.items() if count == maxCount]
    return modes[0] if len(modes) == 1 else modes

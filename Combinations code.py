def combinations(arr, length):
    if len(arr) < length:
        return []

    if length == 0:
        return [[]]

    if len(arr) == length:
        return [arr]

    last_element = arr[-1]

    combinations_without_last = combinations(arr[:-1], length)

    combinations_with_last = [
        combination + [last_element]
        for combination in combinations(arr[:-1], length - 1)
    ]
    return combinations_without_last + combinations_with_last
arr = [1, 2, 3, 4]
length = 3
result = combinations(arr, length)
print(result)
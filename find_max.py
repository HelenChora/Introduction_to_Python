def find_max(values):
    """Return the biggest value."""
    biggest = values[0]

    for num in values:
        if num > biggest:
            biggest = num

    return biggest


def count_occurrences(items, target):
    """Count how many times target appears."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def filter_by_value(d, minimum):
    """Return a new dictionary with values >= minimum."""
    result = {}

    for key, value in d.items():
        if value >= minimum:
            result[key] = value

    return result



print(find_max([4, 9, 2]))

print(count_occurrences(["a", "b", "a"], "a"))

print(filter_by_value({"Ana": 15, "Ben": 9}, 10))
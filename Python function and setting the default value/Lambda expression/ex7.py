def custom_reduce(function, sequence, initial=None):
    iterable = iter(sequence)
    for element in iterable:
        result = function(result, element)

    return result

# Example usage:
numbers = [1, 2, 3, 4]
product = custom_reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24

numbers = list(range(1, 11))

result1 = sum(map(lambda number: number * 3, filter(lambda digit: digit % 2 == 0, numbers)))
print("With filter/map:", result1)

result2 = sum(number * 3 for number in numbers if number % 2 == 0)
print("With comprehension:", result2)

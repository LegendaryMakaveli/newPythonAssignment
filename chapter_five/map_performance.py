numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def odd_test(number):
    print("filter called with:", number)
    return number % 2 != 0

def square(number):
    print("map called with:", number)
    return number ** 2

print("Filter → Map:")
list(map(square, filter(odd_test, numbers)))

print("\nMap → Filter:")
list(filter(odd_test, map(square, numbers)))

def unique_sorted(my_list):
    return sorted(set(my_list))

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
words   = ["pear", "apple", "orange", "pear", "banana", "apple"]

print("Unique numbers:", unique_sorted(numbers))
print("Unique words:", unique_sorted(words))

import random

letters = [random.choice("abcdef") for _ in range(20)]
print("Original:", letters)

print("Ascending:", sorted(letters))
print("Descending:", sorted(letters, reverse=True))
print("Unique sorted:", sorted(set(letters)))

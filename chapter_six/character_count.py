sentence = input("Enter a sentence: ").lower()

counter = {}
for char in sentence:
    counter[char] = counter.get(char, 0) + 1

print("Letter    Count")
for char in sorted(counter):
    print(f"{char:<8}{counter[char]}")

alphabet = set("abcdefghijklmnopqrstuvwxyz")
missing = alphabet - set(sentence)
print("Missing letters:", "".join(sorted(missing)))

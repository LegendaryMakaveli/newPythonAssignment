from itertools import permutations

def anagrams(sentence):
    return sorted(set(''.join(word) for word in permutations(sentence)))

print("Anagrams of 'come':", anagrams("come"))
print("Anagrams of 'aab':", anagrams("aab"))

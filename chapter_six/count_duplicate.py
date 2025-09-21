text = ('this is sample text with several words '
        'this is more sample text with some different words')

word_counts = {}
# count occurrences of each unique word
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(f'{"WORD":<12}COUNT (Duplicates Only)')
for word, count in sorted(word_counts.items()):
    if count > 1:   # show only duplicates
        print(f'{word:<12}{count}')

print('\nNumber of duplicate words:', sum(1 for c in word_counts.values() if c > 1))

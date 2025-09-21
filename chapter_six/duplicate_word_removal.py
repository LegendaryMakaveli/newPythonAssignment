def unique_words(sentence):
    words = sentence.lower().split()
    unique = set(words)
    for word in sorted(unique):
        print(word)


unique_words("you can only run run run")

synonyms = {
    "happy": ["joyful", "cheerful", "content"],
    "sad": ["unhappy", "sorrowful", "downcast"],
    "fast": ["quick", "speedy", "rapid"],
    "big": ["large", "huge", "gigantic"],
    "small": ["tiny", "little", "miniature"]
}

for word, syns in synonyms.items():
    print(word)
    for syn in syns:
        print(f"   {syn}")

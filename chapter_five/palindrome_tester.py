def is_palindrome(sentence):
    filtered = [char.lower() for char in sentence if char.isalnum()]
    stack = []
    for char in filtered:
        stack.append(char)
    for char in filtered:
        if char != stack.pop():
            return False
    return True

print(is_palindrome("radar"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Hello"))

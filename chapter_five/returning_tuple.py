def reposition(first, second, third):
    return third, first, second

a, b, c = 'Doug', 22, 1984

for count in range(1, 4):
    a, b, c = reposition(a, b, c)
    print(f"After call {count}: a = {a}, b = {b}, c = {c}")

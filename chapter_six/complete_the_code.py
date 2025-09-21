first = {1, 2, 4, 8, 16} | {1, 4, 16, 64, 256}
second = {1, 2, 4, 8, 16} & {1, 4, 16, 64, 256}
third = {1, 2, 4, 8, 16} - {1, 4, 16, 64, 256}
fourth = {1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256}
fifth = {1, 2, 4, 8, 16} > {1, 4, 16, 64, 256}


print(first)
print(second)
print(third)
print(fourth)
print(fifth)
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

print('Canada' in tlds)
print('France' in tlds)

for country, code in tlds.items():
    print(f"{country:<15}{code}")

tlds['Sweden'] = 'sw'
print(tlds)

tlds['Sweden'] = 'se'
print(tlds)

reversed_dict = {value: key for key, value in tlds.items()}
print(reversed_dict)

uppercase_dict = {value: key.upper() for key, value in tlds.items()}
print(uppercase_dict)
